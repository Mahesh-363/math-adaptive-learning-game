

import random
from typing import Tuple

Difficulty = str  

def _rand_int(a: int, b: int) -> int:
    return random.randint(a, b)

def generate_puzzle(difficulty: Difficulty) -> Tuple[str, int, Difficulty]:
    """
    Return (question_text, correct_answer, difficulty)
    difficulty: "easy" | "medium" | "hard"
    """
    if difficulty == "easy":
       
        a = _rand_int(1, 9)
        b = _rand_int(0, 9)
        if random.random() < 0.6:
            question = f"{a} + {b}"
            answer = a + b
        else:
            
            a, b = max(a, b), min(a, b)
            question = f"{a} - {b}"
            answer = a - b
    elif difficulty == "medium":
        
        r = random.random()
        if r < 0.4:
            a = _rand_int(10, 99)
            b = _rand_int(10, 99)
            question = f"{a} + {b}"
            answer = a + b
        elif r < 0.8:
            a = _rand_int(10, 99)
            b = _rand_int(0, 99)
            a, b = max(a, b), min(a, b)
            question = f"{a} - {b}"
            answer = a - b
        else:
            a = _rand_int(2, 9)
            b = _rand_int(2, 9)
            question = f"{a} * {b}"
            answer = a * b
    else:  
        
        r = random.random()
        if r < 0.4:
            a = _rand_int(100, 999)
            b = _rand_int(100, 999)
            question = f"{a} + {b}"
            answer = a + b
        elif r < 0.8:
            a = _rand_int(10, 99)
            b = _rand_int(2, 9)
            question = f"{a} * {b}"
            answer = a * b
        else:
            b = _rand_int(2, 10)
            q = _rand_int(10, 99)
            a = q * b
            question = f"{a} ÷ {b}"
            answer = q

    return question, answer, difficulty

def next_difficulty_label(label: str) -> str:
    return label  
