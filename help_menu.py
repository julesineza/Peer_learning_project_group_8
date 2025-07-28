def display_help():
    print("\n" + "-" * 40 + " HELP MENU " + "-" * 40)
    print("""
Welcome to the Health Symptom Checker!

This application allows you to:
- Enter symptoms like fever, cough, headache
- Receive basic advice on possible common illnesses
- Decide whether to self-manage or seek professional help

How to Use:
- Choose option [1] to check symptoms
- Type your symptoms one by one e.g : 
            > Enter symptom: fever
            > Enter symptom: headache
            > Enter symptom: q(quit)

IMPORTANT:
- This tool is NOT a medical diagnosis
- For serious symptoms, always consult a licensed healthcare provider
    """)
    print("- Do not enter numbers or random symbols as symptoms.")
    print("- Use common names for symptoms (e.g., 'nausea' instead of 'feeling sick').")
    print("- This tool does NOT store your personal data.")
    print("- If symptoms persist, seek professional medical help.\n")
    print("-" * 95)
    input("Press Enter to return to the main menu...")


