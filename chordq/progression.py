import random

import attrs

from chordq.constants import (
    CHORD_PROGRESSION_TO_INDEX,
    CHORD_PROGRESSIONS,
    MODES,
    ROMAN_NUMERAL_SYSTEM,
    SCALES,
)
from chordq.note import Note


@attrs.define
class Progression:
    """Progression Object."""

    key: str
    mode: str
    progression: list[str]
    chords: list[str]

    def get_progression_str(self) -> str:
        """Return `notes` as a string."""
        return " ".join([str(value) for value in self.progression])

    def get_chords_str(self) -> str:
        """Return `notes` as a string."""
        return " ".join([str(chord) for chord in self.chords])

    @staticmethod
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

    @classmethod
    def generate_random_progression(cls) -> "Progression":
        """Generate random progression."""
        mode: str = random.choice(MODES)
        key: str = random.choice(list(SCALES[mode].keys()))
        progression: list[str] = random.choice(CHORD_PROGRESSIONS[mode])

        # Make index list from progression.
        progression_indicies: list[int] = [
            CHORD_PROGRESSION_TO_INDEX[mode][val] for val in progression
        ]

        # Get chord modes ("maj, min") from roman numeral list, make a list of modes.
        # We'll zip these with the chords_without_modes to make the chords.
        chord_modes: list[str] = [
            ROMAN_NUMERAL_SYSTEM[mode][idx] for idx in progression_indicies
        ]
        chords_without_modes: list[str] = [
            SCALES[mode][key][idx] for idx in progression_indicies
        ]
        chords: list[str] = [
            f"{i[0]}{i[1]}" for i in zip(chords_without_modes, chord_modes, strict=True)
        ]

        return cls(key=key, mode=mode, progression=progression, chords=chords)
