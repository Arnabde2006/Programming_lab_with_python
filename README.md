# Programming Lab with Python

**Course Code:** BCACC393
**Institute of Engineering and Management**

Solutions for the Python programming lab assignments, covering Python fundamentals, data types, core data structures (lists, tuples, dictionaries), conditional logic, iteration, functions, functional programming, object-oriented programming, exception and file handling, NumPy / Pandas / Matplotlib, data analysis, and introductory AI search and knowledge representation.

## Contents

| File | Topics Covered |
|---|---|
| [`Assignment 1.py`](./Assignment%201.py) | Hello World, user input, arithmetic operations, area/temperature calculations, type casting, averages, lists, tuples |
| [`Assignment 2.py`](./Assignment%202.py) | String methods, f-strings, list & tuple methods (append, insert, remove, pop, sort, count, index), nested lists & tuples |
| [`Assignment 3.py`](./Assignment%203.py) | Lists & tuples (max/min/sum/avg, indexing, set operations, rotation), nested lists, dictionaries (frequency counters, lookups, updates), grading logic with if-elif-else |
| [`Assignment 4.py`](./Assignment%204.py) | Conditional logic (if-elif-else: billing slabs, ticket pricing, ATM checks, fine calculation, grading), `for` loops (attendance, savings tracker, counters, fruit/water/book lists), `while` loops (guessing game, PIN security), do-while simulation, nested loops (bank deposits), combined lists + dictionary + loops + if-else (shopping system with discounts) |
| [`Assignment 5.py`](./Assignment%205.py) | Functions (no-argument, positional, keyword, default arguments, void vs fruitful, multiple return values), lambda functions, `map()`, `filter()`, `reduce()`, iterators (`iter()`/`next()`, custom `CountDown` iterator), generators (`yield`, generator + filtering) |
| [`Assignment 6.py`](./Assignment%206.py) | Recursion (factorial, Fibonacci, sum of n, reverse number), closures (simple, power, counter), decorators (basic, execution timer, arguments), classes & objects, class vs instance attributes, private methods, constructors & destructors, inheritance (single, multilevel, multiple), overloading (default args, `__add__`), method overriding, abstract base classes, metaclasses |
| [`Assignment 7.py`](./Assignment%207.py) | **Part A:** OOP (constructors, instance/class attributes, private members, inheritance types, overriding, operator overloading, ABC, polymorphism, metaclass). **Part B:** exception handling (`try-except-else-finally`, multiple exceptions, user-defined `InvalidAgeError`) and file handling (create/read/write, count lines-words-characters, copy files, file operations with exception handling) |
| [`Assignment 8.py`](./Assignment%208.py) | **Part A:** `array` module (create, access, insert/delete, sort/reverse, search/count). **Part B:** NumPy (creation, indexing/slicing, arithmetic, statistics, reshaping, matrix operations, Boolean indexing, math functions, stack/split, NaN handling). **Part C:** Pandas (Series, DataFrame, filtering, sorting/ranking, missing data, `groupby`). **Part D:** Matplotlib (line, bar, subplots, combined Pandas + NumPy + Matplotlib visualization) |
| [`Assignment 9.py`](./Assignment%209.py) | Data analytics on the UCI Automobile dataset: loading & exploration, missing values (`?` to NaN), price cleaning, frequency counts (make, body style, fuel type, drive wheels), group-wise average prices, histograms, scatter plots, correlation analysis, and a complete price analytics report with conclusion |
| [`Assignment 10.py`](./Assignment%2010.py) | AI lab (menu-driven, Q1-Q10): Tic-Tac-Toe GUI with Minimax, 8-Puzzle GUI solver (BFS vs A*), BFS route finding, DFS maze solving, A* with Manhattan distance, Greedy Best-First Search vs BFS, propositional-logic knowledge base, semantic network (IS-A / HAS-A / CAN), PEAS description generator, and an intelligent grid navigation agent (BFS, DFS, Greedy, A*) with a Tkinter visualizer and algorithm comparison |

## How to Run

Each file is self-contained. Run with:

```bash
python "Assignment 1.py"
python "Assignment 2.py"
python "Assignment 3.py"
python "Assignment 4.py"
python "Assignment 5.py"
python "Assignment 6.py"
python "Assignment 7.py"
python "Assignment 8.py"
python "Assignment 9.py"
python "Assignment 10.py"
```

Programs that require input will prompt for it in the terminal.

**Notes**

- **Assignment 7:** Part B programs prompt for input; `student.txt`, `source.txt` and `destination.txt` are created in the working directory.
- **Assignment 8 & 9:** plots open in Matplotlib windows - close each window to continue to the next question.
- **Assignment 9:** requires the UCI Automobile dataset file `imports-85.data` in the same folder ([download](https://archive.ics.uci.edu/dataset/10/automobile)). If the file is missing, the program tries to fetch it from the UCI repository.
- **Assignment 10:** shows a menu - enter a question number (1-10) or `0` to exit. Q1, Q2 and Q10 open Tkinter windows; close the window to return to the menu.

## Requirements

- Python 3.x
- `numpy`, `pandas`, `matplotlib` (Assignments 8, 9)
- `tkinter` (Assignment 10 - bundled with the standard Python installer on Windows)

```bash
pip install numpy pandas matplotlib
```

---
**Name:** Arnab De
