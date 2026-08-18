# Simple Python Debugger
A **beginner-friendly Python debugging tool** built to answer one simple question:
“What went wrong in my code, and how can I fix it?”

## The Journey
**Week 1** — Understanding Errors
I started by studying common Python errors such as SyntaxError, NameError, TypeError, IndexError, and ZeroDivisionError. I also planned what a beginner-friendly debugger should provide.

**Week 2** — Building the Analyzer
I created the first analyzer.py and used Python's compile() function to detect syntax errors and identify their line numbers.

**Week 3** — Runtime Errors
I added runtime error detection using exec(), try-except, and Python's traceback module.

**Week 4** — Finding the Exact Line
I improved traceback handling so the debugger could identify the error line from the user's code instead of the debugger itself.

**Week 5** — Building the Web App
I connected the analyzer to Flask and created a simple webpage where users could enter Python code and analyze it.

**Week 6** — Adding Suggestions
I created suggestions.py to provide simple explanations and possible fixes instead of only showing Python's error message.

**Week 7** — Designing the Interface
I created the CSS and developed a dark, terminal-inspired interface with error highlighting and beginner-friendly results.

**Week 8** — Testing & GitHub
I tested the debugger using larger Python programs, fixed issues, cleaned the project structure, and uploaded the completed project to GitHub.

## Features
 Runtime error detection
Error type identification
Python syntax checking
Error line detection
Problematic code display
Beginner-friendly explanations
Fix suggestions
Simple web interface

## Technologies
Python
Flask
HTML
CSS
Git & GitHub

## Project Structure
Simple-Python-Debugger/

│

├── app.py

├── analyzer.py

├── suggestions.py

├── requirements.txt

├── Procfile

├── .gitignore

│

├── templates/

│   └── index.html

│

└── static/
     style.css


**Run Locally**
git clone https://github.com/gokul307-tech/Simple-Python-Debugger.git
cd Simple-Python-Debugger
pip install -r requirements.txt
python app.py
Then open:
http://127.0.0.1:5000


## Author
Gokulavasan

# Website link 
[Click to check my debugger..!!](https://simple-python-debugger.vercel.app/)
