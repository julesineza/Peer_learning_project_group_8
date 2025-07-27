import json
import time
#1 Symptom input validation

def get_input():

    diagnosis = {}

    # input  prompt of name variable

    name = input("Please enter your name: ")

    print(f"Hello {name} can you tell us about your health? ")
    print('-'*80)
    time.sleep(0.5)

    count = 1
    while True:

        try:
            symptom = input(f"Enter your symptom #{count} (press q to quit): ").lower().strip()
            if symptom == "q":
                break
            if not symptom.isalpha() or len(symptom) < 3:
                print("Invalid symptom. Please enter alphabetic text with at least 3 characters.")
                continue
            diagnosis.setdefault("symptoms", []).append(symptom)
            count += 1
        except ValueError:
            print("Invalid input . PLEASE TRY AGAIN")

    diagnosis["name"] = name

    return diagnosis


def ask_followup(symptom):
    return input(f"Do you also have '{symptom}'? (y/n): ").strip().lower()