import random

from chordq.constants import (
    CHORD_PROGRESSION_TO_INDEX,
    CHORD_PROGRESSIONS,
    MODES,
    ROMAN_NUMERAL_SYSTEM,
    SCALES,
)
from chordq.note import Note


def generate_roman_numeral_chords(key: str, mode: str) -> list[str]:
    """
    Generate Roman Numeral system for key and scale type.

    Args:
        key (str): Key of the scale.
        mode (str): `maj` or `min`.

    Returns:
        list[str]: List of chords in the sequence.
    """
    key_note = Note(note=key).note
    scale: list[str] = SCALES[mode][key_note][:-1]
    roman_numeral_modes: list[str] = ROMAN_NUMERAL_SYSTEM[mode]
    chords: list[str] = [
        f"{x[0] + x[1]}" for x in zip(scale, roman_numeral_modes, strict=True)
    ]

    return chords


def chord_progression_to_chords(
    key: str, mode: str, progression: list[str]
) -> list[str]:
    """Given a chord progression return a list of the associated chords."""
    prog_mapping: dict[str, int] = CHORD_PROGRESSION_TO_INDEX[mode]
    return [prog_mapping[val] for val in progression]


def generate_random_progression() -> tuple[str, str, list[str], list[str]]:
    """Generate random progression."""
    mode: str = random.choice(MODES)
    key: str = random.choice(list(SCALES[mode].keys()))
    random_progression: list[str] = random.choice(CHORD_PROGRESSIONS[mode])
    random_progression_indicies: list[int] = chord_progression_to_chords(
        key=key, mode=mode, progression=random_progression
    )
    chord_modes: list[str] = [
        ROMAN_NUMERAL_SYSTEM[mode][idx] for idx in random_progression_indicies
    ]
    chords_without_modes: list[str] = [
        SCALES[mode][key][idx] for idx in random_progression_indicies
    ]
    chords: list[str] = [
        f"{i[0]}{i[1]}" for i in zip(chords_without_modes, chord_modes, strict=True)
    ]
    return (key, mode, random_progression, chords)
