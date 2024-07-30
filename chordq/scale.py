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
            "tonic": Note(note=self.notes[0]),
            "minor second": Note(note=self.notes[1]).flat(),
            "major second": Note(note=self.notes[1]),
            "minor third": Note(note=self.notes[2]).flat(),
            "major third": Note(note=self.notes[2]),
            "perfect fourth": Note(note=self.notes[3]),
            "diminished fifth": Note(note=self.notes[4]).flat(),
            "perfect fifth": Note(note=self.notes[4]),
            "augmented fifth": Note(note=self.notes[4]).sharp(),
            "minor sixth": Note(note=self.notes[5]).flat(),
            "major sixth": Note(note=self.notes[5]),
            "minor seventh": Note(note=self.notes[6]).flat(),
            "major seventh": Note(note=self.notes[6]),
        }

    def get_intervals(self, intervals: list[str]) -> list[Note]:
        """Given a list of string interval names, return the associated notes."""
        return [self.intervals[interval] for interval in intervals]
