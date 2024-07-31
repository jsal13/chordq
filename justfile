set shell := ["zsh", "-cu"]

default:
  just --list

venv: 
  python -m venv .venv
  # Use uv package to pip install.
  # Ref: https://github.com/astral-sh/uv?tab=readme-ov-file#highlights
  source .venv/bin/activate \
    && pip install uv \
    && uv pip install -r requirements.txt \
    && uv pip install -r requirements-dev.txt \
    && pip install -e .

test:
  python -m pytest --doctest-modules ./tests

# Playing
chord: 
  @python ./chordq/cli.py chord-quiz

chords: 
  @python ./chordq/cli.py chords-quiz -n 5

scale: 
  @python ./chordq/cli.py scale-quiz

progression: 
  @python ./chordq/cli.py progression-quiz

progressions: 
  @python ./chordq/cli.py progression-quiz -n 5