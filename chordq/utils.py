import readline  # noqa : readline modifies `input()` directly.

import click

from chordq.constants import (
    PIANO_ASCII,
    PIANO_ASCII_MAP,
    PLAY_NOTE_SYMBOL,
    SPACE_FROM_TOP_OF_TERMINAL,
)
from chordq.note import Note


def check_solution(user_answer: Note | list[Note], answer: Note | list[Note]) -> bool:
    """
    Check a user solution against the actual solution.

    Args:
        user_answer (str): User's string answer.
        answer (list[Note]): Answer as a list of Notes, including the tonic.

    Returns:
        bool: True if the answer is correct.
    """
    if isinstance(answer, Note):
        return answer == user_answer

    if isinstance(answer, list):
        if not isinstance(user_answer, list):
            msg: str = f"{user_answer} is not of type `list[Note]."
            raise TypeError(msg)

        # Includes the tonic...?
        if len(user_answer) + 1 == len(answer):
            user_answer.insert(0, answer[0])

    return user_answer == answer


def make_piano_with_notes(notes: list[Note]) -> str:
    """Make an ASCII piano with notes labeled."""
    notes_list = [PIANO_ASCII_MAP[note.note] for note in notes]

    piano = PIANO_ASCII.copy()
    for val in notes_list:
        piano[val[0]] = (
            piano[val[0]][: val[1]] + PLAY_NOTE_SYMBOL + piano[val[0]][val[1] + 1 :]
        )

    return "\n".join(piano)


def solution_output(result: bool, correct_answer: str) -> None:
    """
    Generate a "Correct/Incorrect" text answer.

    Args:
        result (bool): If the user got the question correct or not.
        correct_answer (str): The correct answer, as a string.
    """
    if result:
        click.secho(
            f"\nCorrect! The answer was: {correct_answer}.",
            fg="green",
        )
    else:
        click.secho(
            f"\nIncorrect! The answer was: {correct_answer}.",
            fg="red",
        )


def quiz_ui(msgs: list[tuple[str, str | None]]) -> str:
    """Generate quiz text with click; list of (msg, color); return user answer."""
    click.clear()
    click.echo(SPACE_FROM_TOP_OF_TERMINAL)
    for msg in msgs:
        click.secho(msg[0], fg="white" if msg[1] is None else msg[1])
    click.echo()
    user_answer: str = input("> ")

    # NOTE: "s" will be replaced by "#" in `user_answer` for convenience of the user.
    user_answer = user_answer.replace("s", "#")

    return user_answer
