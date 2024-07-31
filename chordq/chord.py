import random

import attrs

from chordq.constants import INTERVALS_BY_MODE, SCALES
from chordq.note import Note
from chordq.scale import Scale


@attrs.define()
class Chord:
    """Represent a Chord."""

    key: str
    mode: str
    notes: list[Note] = attrs.field(init=False)

    def __attrs_post_init__(self) -> None:
        self.key = self.key[0].upper() + self.key[1:]  # Don't capitalize flats.
        self.mode = self.mode.lower()

        # Always go with the major scale to figure out the notes via intervals.
        scale: Scale = Scale.generate_scale(key=self.key, mode="maj")
        intervals_in_chord: list[str] = INTERVALS_BY_MODE[self.mode]
        self.notes = scale.get_notes_from_intervals(intervals=intervals_in_chord)

    def get_notes_str(self) -> str:
        """Return `notes` as a string."""
        return " ".join([str(note) for note in self.notes])

    @classmethod
    def generate_random_chord(cls) -> "Chord":
        """
        Generate a random chord.

        Returns:
            Chord object.
        """
        key: str = random.choice(list(SCALES["maj"].keys()))  # Random note.
        mode: str = random.choice(list(INTERVALS_BY_MODE.keys()))

        return cls(key=key, mode=mode)
