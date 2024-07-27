import attr

from chordq.constants import INTERVALS_BY_CHORD_TYPE
from chordq.note import Note
from chordq.scale import Scale


@attr.define()
class Chord:
    """Represent a Chord."""

    key: str
    chord_type: str

    def __attrs_post_init__(self) -> None:
        self.key = self.key[0].upper() + self.key[1:]  # Don't capitalize flats.
        self.chord_type = self.chord_type.lower()

    def notes(self) -> list[Note]:
        """Return notes from the current scale given the interval type."""
        # Make the scale values correspond to Python indices.
        # Base it on the major scale always.
        scale: Scale = Scale(key=self.key, scale_type="maj")
        intervals: list[str] = INTERVALS_BY_CHORD_TYPE[self.chord_type]
        chord_notes: list[Note] = scale.get_intervals(intervals=intervals)

        return chord_notes
