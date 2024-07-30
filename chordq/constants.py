SCALE_TYPES = ["maj", "min"]
SCALES = {
    "maj": {
        "C": ["C", "D", "E", "F", "G", "A", "B", "C"],
        "G": ["G", "A", "B", "C", "D", "E", "F#", "G"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#", "D"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#", "A"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#", "E"],
        "B": ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"],
        "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"],
        "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#", "C#"],
        "F": ["F", "G", "A", "Bb", "C", "D", "E", "F"],
        "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A", "Bb"],
        "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D", "Eb"],
        "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G", "Ab"],
        "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
        "Gb": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"],
        "Cb": ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb", "Cb"],
    },
    "min": {
        "A": ["A", "B", "C", "D", "E", "F", "G", "A"],
        "E": ["E", "F#", "G", "A", "B", "C", "D", "E"],
        "B": ["B", "C#", "D", "E", "F#", "G", "A", "B"],
        "F#": ["F#", "G#", "A", "B", "C#", "D", "E", "F#"],
        "C#": ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"],
        "G#": ["G#", "A#", "B", "C#", "D#", "E", "F#", "G#"],
        "D#": ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"],
        "A#": ["A#", "B#", "C#", "D#", "E#", "F#", "G#", "A#"],
        "D": ["D", "E", "F", "G", "A", "Bb", "C", "D"],
        "G": ["G", "A", "Bb", "C", "D", "Eb", "F", "G"],
        "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"],
        "F": ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"],
        "Bb": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
        "Eb": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db", "Eb"],
        "Ab": ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb", "Ab"],
    },
}


SHARPS = {
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

FLATS = {
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


CHORD_TYPES = ["maj", "min", "dim", "aug", "maj7", "m7", "7"]

INTERVALS_BY_CHORD_TYPE = {
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

PIANO_ASCII = [
    " ___________________________ ",
    "|  ||| |||  |  ||| ||| |||  |",
    "|  ||| |||  |  ||| ||| |||  |",
    "|  ||| |||  |  ||| ||| |||  |",
    "|  ||| |||  |  ||| ||| |||  |",
    "|   |   |   |   |   |   |   |",
    "|   |   |   |   |   |   |   |",
    "|___|___|___|___|___|___|___|",
]

PLAY_NOTE_SYMBOL = "#"
SHARP_ROW = 3
NATURAL_ROW = 6
PIANO_ASCII_MAP = {  # Includes all flats/sharps, even if it is another note.
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
