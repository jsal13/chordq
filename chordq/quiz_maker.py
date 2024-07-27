import random

from chordq.randomize import random_chord, random_scale


def quiz_exclude_one_in_scale() -> tuple[str, str, list[str], str]:
    """
    Excludes one value in the list of notes in a `scale`.

    Returns:
        tuple[str, str, list[str], str]: Tuple with key, scale_type,
            list_of_notes_with_missing_note, missing_note.

    Examples:
        >>> scale_example = (
        ...   "D#", "min", ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"]
        ... )
        >>> print(quiz_exclude_one_in_scale(scale=scale_example))
        ('D#', 'min', ['D#', 'E#', 'F#', 'G#', 'A#', 'B', '__', 'D#'], 'C#')


    """
    scale = random_scale()
    n: int = len(scale[2])
    rand_note_idx: int = random.randint(1, n - 2)  # Don't make it the tonic or octave.
    missing_note_list: list[str] = scale[2].copy()
    missing_note_val: int = scale[2][rand_note_idx]
    missing_note_list[rand_note_idx] = "__"

    return (scale[0], scale[1], missing_note_list, missing_note_val)


def quiz_random_chord() -> tuple[str, str, list[str]]:
    """
    Quiz the user on a random maj chord.

    Returns:
        tuple[str, list[str]]: Tuple of Chord_Type and List of Values.
    """
    chord: tuple[str, str, list[str]] = random_chord()
    key: str = chord[0]
    chord_type: str = chord[1]
    chord_notes: list[str] = chord[2]
    return (key, chord_type, chord_notes[1:])
