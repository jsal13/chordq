import attr

from chordq.constants import SCALES
from chordq.note import Note


@attr.define()
class Scale:
    """Represent a Scale."""

    key: str
    scale_type: str
    notes: list[Note] = attr.field(init=False)
    intervals: dict[str, Note] = attr.field(init=False)

    def __attrs_post_init__(self) -> None:
        self.key = self.key[0].upper() + self.key[1:]  # Don't capitalize flats.
        self.notes = SCALES[self.scale_type][self.key]

        # Various note names for Chord construction.
        self.intervals = {
            "root": Note(note=self.notes[0]),
            "minor third": Note(note=self.notes[2]).flat(),
            "major third": Note(note=self.notes[2]),
            "perfect fifth": Note(note=self.notes[4]),
            "diminished fifth": Note(note=self.notes[4]).flat(),
            "augmented fifth": Note(note=self.notes[4]).sharp(),
            "major seventh": Note(note=self.notes[6]),
            "minor seventh": Note(note=self.notes[6]).flat(),
        }

    def get_intervals(self, intervals: list[str]) -> list[Note]:
        """Given a list of string interval names, return the associated notes."""
        return [self.intervals[interval] for interval in intervals]
