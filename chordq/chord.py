import attr

from chordq.constants import INTERVALS_BY_MODE
from chordq.note import Note
from chordq.scale import Scale


@attr.define()
class Chord:
    """Represent a Chord."""

    key: str
    mode: str

    def __attrs_post_init__(self) -> None:
        self.key = self.key[0].upper() + self.key[1:]  # Don't capitalize flats.
        self.mode = self.mode.lower()

    def notes(self) -> list[Note]:
        """Return notes from the current scale given the interval type."""
        # Make the scale values correspond to Python indices.
        # Base it on the major scale always.
        scale: Scale = Scale(key=self.key, mode="maj")
        intervals: list[str] = INTERVALS_BY_MODE[self.mode]
        chord_notes: list[Note] = scale.get_intervals(intervals=intervals)

        return chord_notes
