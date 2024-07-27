import attr

from chordq.constants import FLATS, SHARPS


@attr.define()
class Note:
    """Represent a note."""

    note: str

    def __attr_post_init__(self) -> None:
        self.note = self.note[0].upper() + self.note[1:]  # Don't capitalize flats.

    def sharp(self) -> str:  # no-qa
        """Return the sharpened note."""
        return SHARPS[self.note]

    def flat(self) -> str:
        """Return the flattened note."""
        return FLATS[self.note]
