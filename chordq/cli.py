import click

from chordq.quiz_maker import quiz_exclude_one_in_scale, quiz_random_chord
from chordq.randomize import random_scale


@click.group()
def cli():
    """Main cli group for Click."""
    pass


@click.command()
@click.option(
    "--scale-type",
    "-s",
    default=None,
    help='"maj" or "min" to force one type of scale.',
)
def scale_quiz(scale_type: str) -> None:
    """Output a random scale quiz for the user."""
    scale: tuple[str, str, list[str]] = random_scale(scale_type=scale_type)
    scale_quiz: tuple[str, str, list[str]] = quiz_exclude_one_in_scale(scale=scale)

    key: str = scale_quiz[0]
    scale_type: str = scale_quiz[1]
    notes_with_missing_val: str = " ".join(scale_quiz[2])
    missing_note_val: str = scale_quiz[3]

    click.secho("=" * 20, fg="white")
    click.echo(f"{key} {scale_type.title()}:")
    click.secho(f"{notes_with_missing_val}\n", fg="blue")
    user_guess: str = click.prompt("Missing note")

    if user_guess.lower().strip() == missing_note_val.lower():
        click.secho(f"Correct!  The missing note was {missing_note_val}.", fg="green")
    else:
        click.secho(f"Incorrect!  The missing note was {missing_note_val}.", fg="red")


@click.command()
def chord_quiz() -> None:
    """Output a random chord quiz for the user."""
    chord_quiz: tuple[str, str, list[str]] = quiz_random_chord()

    key: str = chord_quiz[0]
    chord_type: str = chord_quiz[1]
    notes_with_missing_vals: str = f"{key} " + ("__ " * len(chord_quiz[2]))

    # Include the tonic in the missing notes.
    missing_notes_vals = [s.lower() for s in chord_quiz[2].copy()]
    missing_notes_vals.insert(0, key)

    click.secho("=" * 20, fg="white")
    click.secho(f"{key}{chord_type}:", fg="green")
    click.secho(f"{notes_with_missing_vals}\n", fg="blue")
    user_guess: str = click.prompt("Missing notes").lower().strip().split()

    # If they include the tonic...
    if len(user_guess) == len(missing_notes_vals):
        pass
    # If they do not include the tonic...
    elif len(user_guess) == len(missing_notes_vals) - 1:
        user_guess.insert(0, key)

    if user_guess == missing_notes_vals:
        click.secho(
            f"Correct!  The notes are {' '.join(missing_notes_vals)}.", fg="green"
        )
    else:
        click.secho(
            f"Incorrect!  The notes are {' '.join(missing_notes_vals)}.", fg="red"
        )


cli.add_command(scale_quiz)
cli.add_command(chord_quiz)

if __name__ == "__main__":
    cli()
