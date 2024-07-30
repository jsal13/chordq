import random

import click

from chordq.note import Note
from chordq.progression import (
    generate_random_progression,
)
from chordq.randomize import random_chord, random_scale


def quiz_exclude_one_in_scale() -> tuple[str, str, list[Note], Note]:
    """
    Excludes one value in the list of notes in a `scale`.

    Returns:
        tuple[str, str, list[str], str]: Tuple with key, mode,
            list_of_notes_with_missing_note, missing_note.

    Examples:
        >>> scale_example = (
        ...   "D#", "min", ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"]
        ... )
        >>> print(quiz_exclude_one_in_scale(scale=scale_example))
        ('D#', 'min', ['D#', 'E#', 'F#', 'G#', 'A#', 'B', '__', 'D#'], 'C#')


    """
    scale = random_scale()
    notes = scale[2]
    n: int = len(notes)
    rand_note_idx: int = random.randint(1, n - 2)  # Don't make it the tonic or octave.
    missing_note_val: int = notes[rand_note_idx]
    notes[rand_note_idx] = "__"

    return (scale[0], scale[1], notes, missing_note_val)


def quiz_random_chord() -> tuple[str, str, list[Note]]:
    """
    Quiz the user on a random chord.

    Returns:
        tuple[str, list[str]]: Tuple of mode and List of Values.
    """
    chord: tuple[str, str, list[Note]] = random_chord()
    key: str = chord[0]
    mode: str = chord[1]
    chord_notes: list[Note] = chord[2]

    return (key, mode, chord_notes)


def quiz_random_progression() -> tuple[str, str, list[str], list[str]]:
    """Quiz the user on a random progression."""
    key: str
    mode: str
    progression: list[str]
    chords: list[str]
    key, mode, progression, chords = generate_random_progression()

    return (key, mode, progression, chords)


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
