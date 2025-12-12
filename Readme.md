# 🎯 Math Adaptive Learning Game

A small, modular, and cleanly designed adaptive math game for kids (ages 5–10).  
The game automatically adjusts question difficulty based on the learner’s recent performance, creating a personalized learning experience without needing any external libraries or heavy ML models.

This project focuses on the core idea of adaptive learning:  
**keep the learner in their optimal challenge zone.**

---

## 🌟 Features

- Three difficulty levels: **Easy**, **Medium**, **Hard**
- Automatic difficulty adjustment using a simple, transparent rule-based engine
- Tracks:
  - correctness  
  - response time  
  - recent performance trends  
- End-of-session summary with:
  - total questions  
  - accuracy  
  - average time  
  - full attempt log  
- Option to export the session log as a CSV file
- Lightweight and fully modular Python codebase

---

## 🧩 Project Structure

math-adaptive-prototype
├── README.md
├── Technical_Note.md
├── requirements.txt
└── src/
├── main.py # Entry point for the game
├── puzzle_generator.py # Creates math questions for each difficulty
├── tracker.py # Logs attempts & calculates stats
└── adaptive_engine.py # Rule-based difficulty adjustment


Each module focuses on one responsibility, making the system easy to extend or modify.

---

## 🚀 Getting Started

### 1. Install Python
Make sure you have **Python 3.8+** installed.

### 2. Clone or download the repository

### bash 
git clone https://github.com/yourusername/math-adaptive-learning-game && cd math-adaptive-prototype
python src/main.py

Follow the on-screen instructions to start practicing.


🧠 How the Adaptive Engine Works:-

The game observes the last 3 attempts and adjusts difficulty using simple rules:

1.If the learner gets 2 or more correct AND answers fast, difficulty goes up

2.If the learner gets 0 or 1 correct, difficulty goes down

3.Otherwise, difficulty stays the same

Time thresholds per level are defined in adaptive_engine.py and can be tuned.
This makes the system transparent, explainable, and reviewer-friendly.

📊 Example Output (End-of-Session)
Session Summary for Mahesh
Total questions: 10
Correct answers: 7
Accuracy: 70%
Average time per question: 4.12 seconds

The learner also gets a detailed log of each attempt.


👨‍💻 Author

Built as part of an adaptive learning prototype assignment.
Designed to be simple, understandable, and easy to evaluate.


---










