""" this file is where all the files will meet and we create the ui for implementing the project """

# Import logic class and functions.

from symptom_checker import SymptomChecker
from help_menu import display_help


checker = SymptomChecker()

# Start the main program looping.
while True:
    print("\nWelcome to the Health Symptom Checker!")
    print("-" * 80)
    print("[1] Check Symptoms")
    print("[2] View Help")
    print("[3] Exit")
    print("-" * 80)

    choice = input("> ")

    if choice == "1":
        checker.run()
    elif choice == "2":
        display_help()
    elif choice == "3":
        print("Exiting... Stay healthy!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

        