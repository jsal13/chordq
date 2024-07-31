import random

import attrs

from chordq.constants import MODES, SCALES
from chordq.note import Note


@attrs.define()
class Scale:
    """Represent a Scale."""

    key: str
    mode: str
    notes: list[Note]
    intervals: dict[str, Note] = attrs.field(init=False)

    def __attrs_post_init__(self) -> None:
        self.intervals = Scale.generate_all_intervals(notes=self.notes)

    @staticmethod
    def generate_all_intervals(notes: list[Note]) -> list[Note]:
        """Get note names given an list of intervals and a scale."""
        # Various note names for Chord construction.
        interval_notes = {
            "tonic": notes[0],
            "minor second": notes[1].flat(),
            "major second": notes[1],
            "minor third": notes[2].flat(),
            "major third": notes[2],
            "perfect fourth": notes[3],
            "diminished fifth": notes[4].flat(),
            "perfect fifth": notes[4],
            "augmented fifth": notes[4].sharp(),
            "minor sixth": notes[5].flat(),
            "major sixth": notes[5],
            "minor seventh": notes[6].flat(),
            "major seventh": notes[6],
        }

        return interval_notes

    @classmethod
    def generate_scale(cls, key: str, mode: str) -> "Scale":
        """Generate a random Scale."""
        notes: list[Note] = [Note(note) for note in SCALES[mode][key]]
        return cls(key=key, mode=mode, notes=notes)

    @classmethod
    def generate_random_scale(cls) -> "Scale":
        """Generate a random Scale."""
        mode = random.choice(MODES)
        key = random.choice(list(SCALES[mode].keys()))
        notes: list[Note] = [Note(note) for note in SCALES[mode][key]]
        return cls(key=key, mode=mode, notes=notes)

    def get_notes_from_intervals(self, intervals: list[str]) -> list[Note]:
        """Get notes from list of intervals."""
        return [self.intervals[interval] for interval in intervals]
