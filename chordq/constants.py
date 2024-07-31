MODES: list[str] = ["maj", "min"]
MODE_FULL_NAME_MAP: str = {"maj": "Major", "min": "Minor"}
SCALES: dict[str, dict[str, list[str]]] = {
    "maj": {
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "G": ["G", "A", "B", "C", "D", "E", "F#"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
        "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
        "F": ["F", "G", "A", "Bb", "C", "D", "E"],
        "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"],
        "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
        "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
        "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
        "Gb": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
        "Cb": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"],
    },
    "min": {
        "A": ["A", "B", "C", "D", "E", "F", "G"],
        "E": ["E", "F#", "G", "A", "B", "C", "D"],
        "B": ["B", "C#", "D", "E", "F#", "G", "A"],
        "F#": ["F#", "G#", "A", "B", "C#", "D", "E"],
        "C#": ["C#", "D#", "E", "F#", "G#", "A", "B"],
        "G#": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
        "D#": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
        "A#": ["A#", "B#", "C#", "D#", "E#", "F#", "G#"],
        "D": ["D", "E", "F", "G", "A", "Bb", "C"],
        "G": ["G", "A", "Bb", "C", "D", "Eb", "F"],
        "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
        "F": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"],
        "Bb": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"],
        "Eb": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"],
        "Ab": ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb"],
    },
}


SHARPS: dict[str, str] = {
    "A": "A#",
    "Ab": "A",
    "A#": "B",
    "B": "C",
    "Bb": "B",
    "B#": "C#",
    "C": "C#",
    "Cb": "C",
    "C#": "D",
    "D": "D#",
    "Db": "D",
    "D#": "E",
    "E": "F",
    "Eb": "E",
    "E#": "F#",
    "F": "F#",
    "Fb": "F",
    "F#": "G",
    "G": "G#",
    "Gb": "G",
    "G#": "A",
}

FLATS: dict[str, str] = {
    "A": "G#",
    "Ab": "G",
    "A#": "A",
    "B": "A#",
    "Bb": "A",
    "B#": "B",
    "C": "B",
    "Cb": "Bb",
    "C#": "C",
    "D": "C#",
    "Db": "C",
    "D#": "D",
    "E": "D#",
    "Eb": "D",
    "E#": "E",
    "F": "E",
    "Fb": "D#",
    "F#": "F",
    "G": "F#",
    "Gb": "F",
    "G#": "G",
}

INTERVALS_BY_MODE: dict[str, list[str]] = {
    "maj": ["tonic", "major third", "perfect fifth"],
    "min": ["tonic", "minor third", "perfect fifth"],
    "dim": ["tonic", "minor third", "diminished fifth"],
    "aug": ["tonic", "major third", "augmented fifth"],
    "5": ["tonic", "perfect fifth"],
    "maj7": ["tonic", "major third", "perfect fifth", "major seventh"],
    "m7": ["tonic", "minor third", "perfect fifth", "minor seventh"],
    "7": ["tonic", "major third", "perfect fifth", "minor seventh"],
    "2": ["tonic", "major second", "major third", "perfect fifth"],
    "add9": ["tonic", "major third", "perfect fifth", "major second"],
    "m2": ["tonic", "major second", "minor third", "perfect fifth"],
    "madd9": ["tonic", "minor third", "perfect fifth", "major second"],
    "6": ["tonic", "major third", "perfect fifth", "major sixth"],
    "m6": ["tonic", "minor third", "perfect fifth", "major sixth"],
    "9": ["tonic", "major third", "perfect fifth", "minor seventh", "major second"],
    "maj9": ["tonic", "major third", "perfect fifth", "major seventh", "major second"],
    "m9": ["tonic", "minor third", "perfect fifth", "minor seventh", "major second"],
    "sus2": ["tonic", "major second", "perfect fifth"],
    "sus4": ["tonic", "perfect fourth", "perfect fifth"],
}


# ASCII PIANO

PIANO_ASCII: list[str] = [
    " ___________________________ ",
    "|  ||| |||  |  ||| ||| |||  |",
    "|  ||| |||  |  ||| ||| |||  |",
    "|  ||| |||  |  ||| ||| |||  |",
    "|  ||| |||  |  ||| ||| |||  |",
    "|   |   |   |   |   |   |   |",
    "|   |   |   |   |   |   |   |",
    "|___|___|___|___|___|___|___|",
]

PLAY_NOTE_SYMBOL: str = "#"
SHARP_ROW: int = 3
NATURAL_ROW: int = 6
PIANO_ASCII_MAP: dict[str, tuple[int, int]] = {
    # Includes all flats/sharps, even if it is another note.
    "Cb": (NATURAL_ROW, 26),
    "C": (NATURAL_ROW, 2),
    "C#": (SHARP_ROW, 4),
    "Db": (SHARP_ROW, 4),
    "D": (NATURAL_ROW, 6),
    "D#": (SHARP_ROW, 8),
    "Eb": (SHARP_ROW, 8),
    "E": (NATURAL_ROW, 10),
    "E#": (NATURAL_ROW, 14),
    "Fb": (NATURAL_ROW, 10),
    "F": (NATURAL_ROW, 14),
    "F#": (SHARP_ROW, 16),
    "Gb": (SHARP_ROW, 16),
    "G": (NATURAL_ROW, 18),
    "G#": (SHARP_ROW, 20),
    "Ab": (SHARP_ROW, 20),
    "A": (NATURAL_ROW, 22),
    "A#": (SHARP_ROW, 24),
    "Bb": (SHARP_ROW, 24),
    "B": (NATURAL_ROW, 26),
    "B#": (NATURAL_ROW, 2),
}

ROMAN_NUMERAL_SYSTEM: dict[str, list[str]] = {
    "maj": ["maj", "min", "min", "maj", "maj", "min", "dim"],
    "min": ["min", "dim", "maj", "min", "min", "maj", "maj"],
}

# Note: we're not completely randomizing...
CHORD_PROGRESSIONS: dict[str, list[list[str]]] = {
    "maj": [
        ["I", "IV", "V"],
        ["I", "vi", "IV", "V"],
        ["ii", "V", "I"],
        ["I", "vi", "ii", "V"],
        ["I", "V", "vi", "IV"],
        ["I", "IV", "vi", "V"],
        ["I", "iii", "IV", "V"],
        ["I", "IV", "I", "V"],
        ["I", "IV", "ii", "V"],
    ],
    "min": [
        ["i", "VI", "VII"],
        ["i", "iv", "VII"],
        ["i", "iv", "v"],
        ["i", "VI", "III", "VII"],
        # ["ii", "v", "i"],  # Don't know how to treat "ii" yet.
        ["i", "iv", "v", "i"],
        ["VI", "VII", "i", "i"],
        ["i", "VII", "VI", "VII"],
        ["i", "iv", "i"],
    ],
}

# Eventually make this a function?  Like map to int but then modify?
CHORD_PROGRESSION_TO_INDEX: dict[str, dict[str, int]] = {
    "maj": {"I": 0, "ii": 1, "iii": 2, "IV": 3, "V": 4, "vi": 5, "vii°": 6},
    "min": {"i": 0, "ii°": 1, "III": 2, "iv": 3, "v": 4, "VI": 5, "VII": 6},
}


SPACE_FROM_TOP_OF_TERMINAL: str = "\n" * 1
