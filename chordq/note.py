import attr

from chordq.constants import FLATS, SHARPS


@attr.define()
class Note:
    """Represent a note."""

    note: str

    def __attrs_post_init__(self) -> None:
        self.note = self.note[0].upper() + self.note[1:]  # Don't capitalize flats.

    def sharp(self) -> str:  # no-qa
        """Return the sharpened note."""
        return Note(note=SHARPS[self.note])

    def flat(self) -> str:
        """Return the flattened note."""
        return Note(note=FLATS[self.note])

    def __str__(self) -> str:
        return self.note

    def __eq__(self, other: "Note") -> bool:
        if self.note == other.note:
            return True
        else:
            # If they have same-name notes.
            a_sharp_b_flat = self.note in ("A#", "Bb") and other.note in ("A#", "Bb")
            c_sharp_d_flat = self.note in ("C#", "Db") and other.note in ("C#", "Db")
            d_sharp_e_flat = self.note in ("D#", "Eb") and other.note in ("D#", "Eb")
            f_sharp_g_flat = self.note in ("F#", "Gb") and other.note in ("F#", "Gb")
            g_sharp_a_flat = self.note in ("G#", "Ab") and other.note in ("G#", "Ab")
            e_sharp_f_natr = self.note in ("E#", "F") and other.note in ("E#", "F")

            return (
                a_sharp_b_flat
                or c_sharp_d_flat
                or d_sharp_e_flat
                or f_sharp_g_flat
                or g_sharp_a_flat
                or e_sharp_f_natr
            )
