# Tic-Tac-Toe

A command-line tic-tac-toe game written in Python. Play against the computer on a numbered 3×3 board in your terminal.
Final project for the course **Python Essentials 1** from Universidad Galileo and Cisco Networking Academy in collaboration with OpenEDG Python Institute.

## Features

- Numbered board (positions `1`–`9`) shown after every move
- Computer plays first as `X` (center square, then random free cells)
- You play as `O`
- Win and draw detection for rows, columns, and diagonals
- Input validation for occupied or invalid cells

## Requirements

- Python 3.13 or newer
- No third-party packages (standard library only)

## Installation

Clone or download this repository, then open the project directory:

```bash
cd tic-tac-toe
```

Optional — if you use [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

Or create a virtual environment with the standard library:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

## How to run

```bash
python main.py
```

With uv:

```bash
uv run python main.py
```

## How to play

1. The computer (`X`) moves first and always takes the center square on its opening move.
2. When prompted (`Enter your move (1-9):`), type a free cell number and press Enter.
3. Cells are numbered left to right, top to bottom:

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

4. The game ends when someone gets three in a row or the board is full (draw).

## Project structure

```
tic-tac-toe/
├── main.py          # Game entry point and logic
├── pyproject.toml   # Project metadata
└── README.md
```
