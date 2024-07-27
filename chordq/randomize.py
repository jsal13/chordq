import random

from chordq.chord import Chord
from chordq.constants import CHORD_TYPES, SCALE_TYPES, SCALES
from chordq.note import Note


def random_scale(scale_type: str | None = None) -> tuple[str, str, list[Note]]:
    """
    Get random scale and return (key, scale_type, scale_as_list).

    Args:
        scale_type (str | None, optional): Either "maj" or "min".
            If None, picks at random.  Defaults to None.

    Returns:
        tuple[str, str, list[str]]: Tuple of (key, scale_type, scale_as_list).

    Examples:
        >>> print(random_scale())
        ('D#', 'min', ['D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'])
    """
    scale: tuple[str, list[Note]]
    if scale_type in ("maj", "min"):
        scale = random.choice(list(SCALES[scale_type].items()))
    elif scale_type is None:
        scale_type = random.choice(SCALE_TYPES)
        scale = random.choice(list(SCALES[scale_type].items()))
    else:
        msg = f"`scale_type` must be 'maj', 'min', or Null.  Cannot be {scale_type}."
        raise ValueError(msg)

    scale_notes: list[Note] = [Note(note=note) for note in scale[1]]
    print(scale_notes)
    return (scale[0], scale_type, scale_notes)


def random_chord() -> tuple[str, str, list[Note]]:
    """
    Generate a random chord.

    Returns:
        tuple[str, list[str]]: Tuple of Key, Chord_Type, and List of Notes.
    """
    chord_type: str = random.choice(CHORD_TYPES)
    key: str = random.choice(list(SCALES["maj"].keys()))  # Random note.

    chord: Chord = Chord(key=key, chord_type=chord_type)
    chord_notes: list[Note] = chord.notes()
    return (key, chord_type, chord_notes)
