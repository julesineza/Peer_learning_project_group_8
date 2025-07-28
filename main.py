from symptom_checker import SymptomChecker
from help_menu import display_help

def main():
    from database import disease_db
    checker = SymptomChecker(disease_db)

    while True:
        print("\nWelcome to the Health Symptom Checker!")
        print("----------------------------------------------------")
        print("[1] Check Symptoms")
        print("[2] View Help")
        print("[3] Exit")
        print("----------------------------------------------------")
        choice = input("> ").strip()

        if choice == "1":
            checker.run()

        elif choice == "2":
            display_help()

        elif choice == "3":
            print("Thank you for using Health Symptom Checker. Stay safe!")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()