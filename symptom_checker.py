from database import disease_db
from user_input import get_input, ask_followup
import time

class SymptomChecker:

    def find_possible_conditions(self, symptoms):
        possible = {}
        for disease, data in disease_db.items():
            if any(sym in data['symptoms'] for sym in symptoms):
                possible[disease] = data
        return possible

    def narrow_down(self, candidates, known_symptoms):
        for disease, data in list(candidates.items()):
            for symptom in data["symptoms"]:
                if symptom not in known_symptoms:
                    answer = ask_followup(symptom)
                    if answer == "y":
                        known_symptoms.append(symptom)
                    else:
                        if symptom in data.get("key_symptoms", []):
                            candidates.pop(disease)
                            break
        return candidates

    def show_result(self, matches):
        if len(matches) == 1:
            disease, info = next(iter(matches.items()))
            print(f"\n>>> Most likely condition: {disease}")
            print(f">>> Advice: {info['advice']}")
            print(f">>> Source: {info['source']}")
        elif len(matches) > 1:
            print("\n>>> Multiple possible conditions:")
            for disease in matches:
                print(f"- {disease}")
                
            print("Please consult a healthcare provider for a proper diagnosis.")
        else:
            print(">>> No confident match found. Please monitor your symptoms or seek professional help.")

    def run(self):
        user_data = get_input()
        name = user_data["name"]
        user_symptoms = user_data.get("symptoms", [])

        if not user_symptoms:
            print("No symptoms entered. Returning to menu...")
            return

        print("\nProcessing symptoms...\n")
        possible_conditions = self.find_possible_conditions(user_symptoms)
        final_diagnosis = self.narrow_down(possible_conditions, user_symptoms)
        time.sleep(0.5)
        self.show_result(final_diagnosis)        