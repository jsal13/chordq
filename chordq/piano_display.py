from chordq.constants import PIANO_ASCII, PIANO_ASCII_MAP, PLAY_NOTE_SYMBOL
from chordq.note import Note


def make_piano_with_notes(notes: list[Note]) -> str:
    """Make an ASCII piano with notes labeled."""
    notes_list = [PIANO_ASCII_MAP[note.note] for note in notes]

    piano = PIANO_ASCII.copy()
    for val in notes_list:
        piano[val[0]] = (
            piano[val[0]][: val[1]] + PLAY_NOTE_SYMBOL + piano[val[0]][val[1] + 1 :]
        )

    return "\n".join(piano)
