from typing import Any

import click

from chordq.check_solution import check_solution
from chordq.note import Note
from chordq.piano_display import make_piano_with_notes
from chordq.quiz_maker import (
    quiz_exclude_one_in_scale,
    quiz_random_chord,
    quiz_random_progression,
    solution_output,
)

SPACE_FROM_TOP_OF_TERMINAL = "\n" * 1


@click.group()
def cli():
    """Main cli group for Click."""
    pass


@click.command()
def scale_quiz() -> None:
    """Output a random scale quiz for the user."""
    scale_quiz: tuple[str, str, list[Note], Note] = quiz_exclude_one_in_scale()

    key: str = scale_quiz[0]
    mode: str = scale_quiz[1]
    notes_with_missing_val: list[Note] = scale_quiz[2]
    notes_with_missing_val_str: str = " ".join(
        [str(note) for note in notes_with_missing_val]
    )
    missing_note_val: list[Note] = [
        scale_quiz[3]
    ]  # Singleton list for solution checker.

    click.clear()
    click.echo(SPACE_FROM_TOP_OF_TERMINAL)
    click.echo(f"{key}{mode}:")
    click.secho(f"{notes_with_missing_val_str}\n", fg="blue")
    user_guess: str = click.prompt("Missing note")
    correct_answer: str = str(missing_note_val[0])

    result: bool = check_solution(user_guess, missing_note_val)
    solution_output(result=result, correct_answer=correct_answer)


@click.command()
def chord_quiz() -> None:
    """Output a random chord quiz for the user."""
    chord_quiz: tuple[str, str, list[Note]] = quiz_random_chord()

    key: str = chord_quiz[0]
    mode: str = chord_quiz[1]
    chord_notes: list[Note] = chord_quiz[2]
    notes_with_missing_vals: str = f"{key} " + ("__ " * (len(chord_notes) - 1))

    click.clear()
    click.echo(SPACE_FROM_TOP_OF_TERMINAL)
    click.secho(f"{key}{mode}:", fg="green")
    click.secho(f"{notes_with_missing_vals}\n", fg="blue")
    user_answer: str = click.prompt("Missing notes").lower()

    result: bool = check_solution(user_answer=user_answer, answer=chord_notes)
    correct_answer: str = " ".join(
        [str(note) for note in chord_notes]
    )  # String of solution notes.

    solution_output(result=result, correct_answer=correct_answer)
    click.secho(make_piano_with_notes(notes=chord_notes))
    input("\n\nPress enter...")  # Waits for user input, anything.


@click.command()
def progression_quiz() -> None:
    """Output a random progression quiz for the user."""
    progression_quiz: tuple[str, str, list[Note]] = quiz_random_progression()

    key: str = progression_quiz[0]
    mode: str = progression_quiz[1]
    progression: list[str] = progression_quiz[2]
    chords: list[str] = progression_quiz[3]

    progression_spaces: str = "__ " * (len(progression))
    mode_full_name: str = {"maj": "Major", "min": "Minor"}[mode]

    click.clear()
    click.echo(SPACE_FROM_TOP_OF_TERMINAL)
    click.secho(f"{key} {mode_full_name} :: {' '.join(progression)}", fg="green")
    click.secho(f"{progression_spaces}\n", fg="blue")
    user_answer: str = click.prompt("Chords").lower()

    # TODO: Check sol for chords?
    # result: bool = check_solution(user_answer=user_answer, answer=chord_notes)
    correct_answer: str = " ".join(chords)  # String of solution notes.
    result: bool = correct_answer.lower() == user_answer.lower()

    solution_output(result=result, correct_answer=correct_answer)
    input("\n\nPress enter...")  # Waits for user input, anything.


@click.command()
@click.option(
    "-n", "--num-questions", default=3, type=int, help="Number of chord questions."
)
@click.pass_context
def chords_quiz(ctx: Any, num_questions: int) -> None:
    """Create a quiz with `n` chords."""
    for _ in range(num_questions):
        ctx.invoke(chord_quiz)


cli.add_command(scale_quiz)
cli.add_command(chord_quiz)
cli.add_command(chords_quiz)
cli.add_command(progression_quiz)

if __name__ == "__main__":
    cli()
