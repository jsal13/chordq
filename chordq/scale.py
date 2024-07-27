import attr
from constants import SCALES
from note import Note


@attr.define()
class Scale:
    """Represent a Scale."""

    key: str
    scale_type: str
    notes: list[str] = attr.field(init=False)
    intervals: dict[str, str] = attr.field(init=False)

    def __attrs_post_init__(self) -> None:
        self.key = self.key[0].upper() + self.key[1:]  # Don't capitalize flats.
        self.notes = SCALES[self.scale_type][self.key]

        # Various note names for Chord construction.
        self.intervals = {
            "root": self.notes[0],
            "minor third": Note(note=self.notes[2]).flat(),
            "major third": self.notes[2],
            "perfect fifth": self.notes[4],
            "diminished fifth": Note(note=self.notes[4]).flat(),
            "augmented fifth": Note(note=self.notes[4]).sharp(),
            "major seventh": self.notes[6],
            "minor seventh": Note(note=self.notes[6]).flat(),
        }

    def get_intervals(self, intervals: list[str]) -> list[str]:
        """Given a list of string interval names, return the associated notes."""
        return [self.intervals[interval] for interval in intervals]
