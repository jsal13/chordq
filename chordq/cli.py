import click

from chordq.check_solution import check_solution
from chordq.note import Note
from chordq.quiz_maker import quiz_exclude_one_in_scale, quiz_random_chord


@click.group()
def cli():
    """Main cli group for Click."""
    pass


@click.command()
def scale_quiz() -> None:
    """Output a random scale quiz for the user."""
    scale_quiz: tuple[str, str, list[Note], Note] = quiz_exclude_one_in_scale()

    key: str = scale_quiz[0]
    scale_type: str = scale_quiz[1]
    notes_with_missing_val: list[Note] = scale_quiz[2]
    notes_with_missing_val_str: str = " ".join(
        [str(note) for note in notes_with_missing_val]
    )
    missing_note_val: list[Note] = [
        scale_quiz[3]
    ]  # Singleton list for solution checker.

    click.secho("=" * 20, fg="white")
    click.echo(f"{key} {scale_type.title()}:")
    click.secho(f"{notes_with_missing_val_str}\n", fg="blue")
    user_guess: str = click.prompt("Missing note")

    if check_solution(user_guess, missing_note_val):
        click.secho(
            f"Correct!  The missing note was {missing_note_val[0]}.", fg="green"
        )
    else:
        click.secho(
            f"Incorrect!  The missing note was {missing_note_val[0]}.", fg="red"
        )


@click.command()
def chord_quiz() -> None:
    """Output a random chord quiz for the user."""
    chord_quiz: tuple[str, str, list[Note]] = quiz_random_chord()

    key: str = chord_quiz[0]
    chord_type: str = chord_quiz[1]
    chord_notes: list[Note] = chord_quiz[2]
    notes_with_missing_vals: str = f"{key} " + ("__ " * (len(chord_notes) - 1))

    click.secho("=" * 20, fg="white")
    click.secho(f"{key}{chord_type}:", fg="green")
    click.secho(f"{notes_with_missing_vals}\n", fg="blue")
    user_answer: str = click.prompt("Missing notes").lower()

    result: bool = check_solution(user_answer=user_answer, answer=chord_notes)
    sol_str: str = " ".join(
        [str(note) for note in chord_notes]
    )  # String of solution notes.

    if result:
        click.secho(
            f"Correct!  The notes are {sol_str}.",
            fg="green",
        )
    else:
        click.secho(
            f"Incorrect!  The notes are {sol_str}.",
            fg="red",
        )


cli.add_command(scale_quiz)
cli.add_command(chord_quiz)

if __name__ == "__main__":
    cli()
