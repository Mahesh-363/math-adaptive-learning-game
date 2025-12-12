

from typing import List
from tracker import Attempt

LEVELS = ["easy", "medium", "hard"]


TIME_THRESHOLDS = {
    "easy": 8.0,
    "medium": 12.0,
    "hard": 20.0
}

def _index(level: str) -> int:
    try:
        return LEVELS.index(level)
    except ValueError:
        return 0

def decide_next_level(current_level: str, recent_attempts: List[Attempt]) -> str:
    
    if not recent_attempts:
        return current_level

    corrects = sum(1 for a in recent_attempts if a.correct)
    avg_time = sum(a.time_taken for a in recent_attempts) / len(recent_attempts)

    idx = _index(current_level)

    
    if corrects >= 2 and avg_time <= TIME_THRESHOLDS.get(current_level, 10.0):
        
        if idx < len(LEVELS) - 1:
            return LEVELS[idx + 1]
        return current_level

   
    if corrects <= 1:
        if idx > 0:
            return LEVELS[idx - 1]
        return current_level

   
    return current_level
