

import time
import sys
from puzzle_generator import generate_puzzle
from tracker import SessionTracker, Attempt
from adaptive_engine import decide_next_level

def choose_initial_level() -> str:
    choices = {"1": "easy", "2": "medium", "3": "hard"}
    print("Choose initial difficulty:")
    print("  1) Easy")
    print("  2) Medium")
    print("  3) Hard")
    while True:
        c = input("Enter 1/2/3 (default 1): ").strip() or "1"
        if c in choices:
            return choices[c]
        print("Please enter 1, 2 or 3.")

def safe_input(prompt: str) -> str:
    try:
        return input(prompt)
    except EOFError:
        return ""

def run_session():
    print("Welcome to Math Adventures (adaptive)!")
    name = safe_input("Enter learner name: ").strip() or "Learner"
    level = choose_initial_level()
    try:
        total_q = int(safe_input("How many questions this session? (default 10): ").strip() or "10")
    except ValueError:
        total_q = 10

    tracker = SessionTracker()
    print(f"\nHello {name}. Starting at '{level}' level. Let's go!\n")

    for i in range(1, total_q + 1):
        question, answer, cur_level = generate_puzzle(level)
        print(f"Q{i}/{total_q} [{level.title()}] : {question} = ?")
        start = time.time()
        user_ans = safe_input("Your answer: ").strip()
        end = time.time()
        elapsed = end - start

        attempt = Attempt(question=question, correct_answer=answer,
                          user_answer=user_ans, difficulty=level,
                          time_taken=elapsed)
        tracker.log_attempt(attempt)

        if attempt.correct:
            print(f"Nice! ✅ (time: {elapsed:.2f}s)\n")
        else:
            print(f"Oops. Correct answer: {answer}  (your time: {elapsed:.2f}s)\n")

       
        recent = tracker.recent_attempts(3)
        new_level = decide_next_level(level, recent)
        if new_level != level:
            print(f"Adaptive engine: level changed {level} -> {new_level}\n")
        level = new_level

    
    summary = tracker.summary()
    print("=" * 40)
    print(f"Session Summary for {name}")
    print(f"Total questions: {summary['total']}")
    print(f"Correct answers: {summary['correct']}")
    print(f"Accuracy: {summary['accuracy_percent']}%")
    print(f"Average time per question: {summary['avg_time_sec']} seconds")
    print("=" * 40)
    print("\nDetailed log (most recent first):")
    for a in reversed(tracker.attempts):
        status = "✓" if a.correct else "✗"
        print(f"[{a.difficulty}] {a.question} = {a.correct_answer} | you: {a.user_answer} | {status} | {a.time_taken:.2f}s")

    save = safe_input("\nSave detailed log to 'session_log.csv'? (y/N): ").strip().lower()
    if save == "y":
        try:
            import csv
            with open("session_log.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["question", "correct_answer", "user_answer", "difficulty", "time_taken", "correct"])
                writer.writeheader()
                for a in tracker.attempts:
                    writer.writerow(a.as_dict())
            print("Saved to session_log.csv")
        except Exception as e:
            print("Could not save file:", e)

if __name__ == "__main__":
    run_session()
