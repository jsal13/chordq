import random
from typing import Any

import click

from chordq.chord import Chord
from chordq.constants import MODE_FULL_NAME_MAP
from chordq.note import Note
from chordq.progression import Progression
from chordq.scale import Scale
from chordq.utils import check_solution, make_piano_with_notes, quiz_ui, solution_output


@click.group()
def cli():
    """Main cli group for Click."""
    pass


@click.command()
def scale_quiz() -> None:
    """Output a random scale quiz for the user."""
    scale: Scale = Scale.generate_random_scale()
    mode_full_name: str = MODE_FULL_NAME_MAP[scale.mode]
    notes: list[Note] = scale.notes

    missing_note_idx: int = random.randint(1, 6)  # Don't make it the tonic or octave.
    missing_note_val: int = notes[missing_note_idx]

    notes_with_missing_val_str: str = " ".join(
        [
            "__" if idx == missing_note_idx else str(note)
            for idx, note in enumerate(notes)
        ]
    )

    msgs: list[tuple[str, str]] = [
        (f"{scale.key} {mode_full_name}:", "green"),
        (f"{notes_with_missing_val_str}", "blue"),
    ]

    user_answer_note: Note
    while True:
        user_answer: str = quiz_ui(msgs=msgs).strip().lower()
        try:
            user_answer_note = Note(note=user_answer)
            break
        except KeyError as _:
            click.secho(f"P{user_answer} is not a valid Note.")

    result: bool = check_solution(user_answer_note, missing_note_val)
    solution_output(result=result, correct_answer=missing_note_val)


@click.command()
def chord_quiz() -> None:
    """Output a random chord quiz for the user."""
    chord: Chord = Chord.generate_random_chord()
    notes_with_missing_vals: str = f"{chord.key} " + ("__ " * (len(chord.notes) - 1))

    msgs: list[tuple[str, str]] = [
        (f"{chord.key}{chord.mode}:", "green"),
        (f"{notes_with_missing_vals}", "blue"),
    ]
    user_answer: str = quiz_ui(msgs=msgs)
    user_answer_notes = [Note(note=note) for note in user_answer.split()]

    result: bool = check_solution(user_answer=user_answer_notes, answer=chord.notes)

    solution_output(result=result, correct_answer=chord.get_notes_str())
    click.secho(make_piano_with_notes(notes=chord.notes))
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


@click.command()
def progression_quiz() -> None:
    """Output a random progression quiz for the user."""
    progression: Progression = Progression.generate_random_progression()

    progression_spaces: str = "__ " * (len(progression.chords))
    mode_full_name: str = MODE_FULL_NAME_MAP[progression.mode]

    msgs: list[tuple[str, str]] = [
        (
            f"{progression.key} {mode_full_name}: {progression.get_progression_str()}",
            "green",
        ),
        (f"{progression_spaces}\n", "blue"),
    ]
    user_answer: str = quiz_ui(msgs)

    # TODO: Check sol for chords?  This is gross, to check the string values.
    # result: bool = check_solution(user_answer=user_answer, answer=chord_notes)
    correct_answer: str = " ".join(progression.chords)  # String of solution notes.
    result: bool = correct_answer.lower() == user_answer.lower()

    solution_output(result=result, correct_answer=correct_answer)
    input("\n\nPress enter...")  # Waits for user input, anything.


@click.command()
@click.option(
    "-n",
    "--num-questions",
    default=3,
    type=int,
    help="Number of progression questions.",
)
@click.pass_context
def progressions_quiz(ctx: Any, num_questions: int) -> None:
    """Create a quiz with `n` chords."""
    for _ in range(num_questions):
        ctx.invoke(progression_quiz)


cli.add_command(scale_quiz)
cli.add_command(chord_quiz)
cli.add_command(chords_quiz)
cli.add_command(progression_quiz)
cli.add_command(progressions_quiz)

if __name__ == "__main__":
    cli()
