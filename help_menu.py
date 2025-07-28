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
- Type your symptoms separated by commas (e.g., fever, headache)

IMPORTANT:
- This tool is NOT a medical diagnosis
- For serious symptoms, always consult a licensed healthcare provider
    """)
    print("-" * 95)
    input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    display_help()
