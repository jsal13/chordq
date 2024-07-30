import random

from chordq.chord import Chord
from chordq.constants import INTERVALS_BY_MODE, MODES, SCALES
from chordq.note import Note


def random_scale(mode: str | None = None) -> tuple[str, str, list[Note]]:
    """
    Get random scale and return (key, mode, scale_as_list).

    Args:
        mode (str | None, optional): Either "maj" or "min".
            If None, picks at random.  Defaults to None.

    Returns:
        tuple[str, str, list[str]]: Tuple of (key, mode, scale_as_list).

    Examples:
        >>> print(random_scale())
        ('D#', 'min', ['D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'])
    """
    scale: tuple[str, list[Note]]
    if mode in ("maj", "min"):
        scale = random.choice(list(SCALES[mode].items()))
    elif mode is None:
        mode = random.choice(MODES)
        scale = random.choice(list(SCALES[mode].items()))
    else:
        msg = f"`mode` must be 'maj', 'min', or Null.  Cannot be {mode}."
        raise ValueError(msg)

    scale_notes: list[Note] = [Note(note=note) for note in scale[1]]
    print(scale_notes)
    return (scale[0], mode, scale_notes)


def random_chord() -> tuple[str, str, list[Note]]:
    """
    Generate a random chord.

    Returns:
        tuple[str, list[str]]: Tuple of Key, mode, and List of Notes.
    """
    mode: str = random.choice(list(INTERVALS_BY_MODE.keys()))
    key: str = random.choice(list(SCALES["maj"].keys()))  # Random note.

    chord: Chord = Chord(key=key, mode=mode)
    chord_notes: list[Note] = chord.notes()
    return (key, mode, chord_notes)
