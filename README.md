# Health Symptom Checker Tool

## Overview

The **Health Symptom Checker Tool** is a beginner-friendly, offline Python command-line application designed to help users perform basic health self-assessments by entering symptoms and receiving likely conditions. This tool does **not replace** professional medical advice, but serves as an early indicator to seek timely care.

---

## Why We Built This

In Rwanda and similar regions, many people delay seeking treatment because they don't realize their symptoms could signal a serious illness. For example, someone with a headache might assume it’s from stress, when it could be something more serious like malaria or meningitis. Our app helps close this awareness gap.

---

## Features

- Menu-driven CLI for ease of use - in the main.py files
- Accepts and validates user-entered symptoms - in the user_input.py file
- Matches symptoms to diseases using internal logic - in the symptom_checker.py file
- Asks follow-up questions to refine diagnosis - in the symptom_checker.py file
- Modular Python code using OOP principles- in the symptom_checker.py files
- Help menu for first-time users - in the help_menu.py file
- Storage of the diseases - in the diseases.py file
- And finally the main.py files which combines all the files and shows the main menu

---

## How It Works

1. The user selects "Start Diagnosis"
2. They enter symptoms one by one (validated)
3. The system matches possible diseases
4. If multiple matches exist, it asks additional yes/no questions
5. A most probable diagnosis is shown, along with advice

---

## Installation

No special installation required.

### Requirements:
- Python 3.8+

### To Run:
python main.py
