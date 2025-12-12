
import time
from typing import List, Dict, Any

class Attempt:
    def __init__(self, question: str, correct_answer: int, user_answer: str,
                 difficulty: str, time_taken: float):
        self.question = question
        self.correct_answer = correct_answer
        self.user_answer = user_answer
        self.difficulty = difficulty
        self.time_taken = time_taken
        self.correct = self._evaluate()

    def _evaluate(self) -> bool:
        try:
            u = float(self.user_answer)
            return abs(u - float(self.correct_answer)) < 1e-6
        except Exception:
            return False

    def as_dict(self) -> Dict[str, Any]:
        return {
            "question": self.question,
            "correct_answer": self.correct_answer,
            "user_answer": self.user_answer,
            "difficulty": self.difficulty,
            "time_taken": self.time_taken,
            "correct": self.correct
        }

class SessionTracker:
    def __init__(self):
        self.attempts: List[Attempt] = []
        self.start_time = time.time()

    def log_attempt(self, attempt: Attempt):
        self.attempts.append(attempt)

    def total_questions(self) -> int:
        return len(self.attempts)

    def correct_count(self) -> int:
        return sum(1 for a in self.attempts if a.correct)

    def accuracy(self) -> float:
        total = self.total_questions()
        if total == 0:
            return 0.0
        return 100.0 * self.correct_count() / total

    def average_time(self) -> float:
        if not self.attempts:
            return 0.0
        return sum(a.time_taken for a in self.attempts) / len(self.attempts)

    def recent_attempts(self, n: int = 3):
        return self.attempts[-n:]

    def summary(self) -> Dict[str, Any]:
        return {
            "total": self.total_questions(),
            "correct": self.correct_count(),
            "accuracy_percent": round(self.accuracy(), 2),
            "avg_time_sec": round(self.average_time(), 2)
        }
