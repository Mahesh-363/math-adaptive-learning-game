# Math-Adaptive-Prototype

Small, rule-based adaptive math practice prototype for ages ~5-10.

## What it does
- Generates math puzzles at 3 difficulty levels: Easy / Medium / Hard
- Tracks correctness and response time
- Automatically adjusts difficulty based on recent performance (simple rules)
- Shows end-of-session summary and can export a CSV log

## Project structure
math-adaptive-prototype/
├─ README.md
├─ requirements.txt
└─ src/
├─ main.py
├─ puzzle_generator.py
├─ tracker.py
└─ adaptive_engine.py


## How to run
1. Make sure you have Python 3.8+ installed.
2. From project root:
```bash
python src/main.py

Follow prompts in the terminal.