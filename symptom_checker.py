from database import disease_db
from user_input import get_input, ask_followup
import time

class SymptomChecker:
    def __init__(self,disease_db):
        self.disease_db = disease_db
        self.user_data = {}
        self.result = {}

    def run(self):
        print("\nWelcome to the Symptom Checker Tool!")
        self.user_data = get_input()

        if not self.user_data.get("symptoms"):
            print("No symptoms entered. Exiting.")
            return

        candidates = self.match_symptoms(self.user_data["symptoms"])
        candidates = self.narrow_down(candidates, self.user_data["symptoms"])

        # Limit to top 2 diagnoses based on matched key symptoms
        candidates = self.get_top_diagnoses(candidates, self.user_data["symptoms"])

        self.result = candidates
        self.show_result()

    def match_symptoms(self, symptoms):
        matched = {}
        for disease, info in self.disease_db.items():
            if any(symptom in info["symptoms"] for symptom in symptoms):
                matched[disease] = info
        return matched

    def narrow_down(self, candidates, known_symptoms):
        question_limit = 6
        followups_asked = 0

        for disease, data in list(candidates.items()):
            for symptom in data["symptoms"]:
                if symptom not in known_symptoms:
                    while True:
                        answer = ask_followup(symptom)
                        if answer not in ["y", "n"]:
                            print("Please respond with 'y' for yes or 'n' for no.")
                            continue
                        break

                    followups_asked += 1

                    if answer == "y":
                        known_symptoms.append(symptom)
                    elif symptom in data.get("key_symptoms", []):
                        candidates.pop(disease)
                        break

                    if followups_asked >= question_limit:
                        choice = input("Would you like to answer 2–3 more questions to improve accuracy? (y/n): ").strip().lower()
                        if choice != "y":
                            return candidates
                        else:
                            question_limit += 3
        return candidates

    def get_top_diagnoses(self, candidates, user_symptoms, max_results=2):
        scored = []
        for disease, info in candidates.items():
            key_syms = set(info.get("key_symptoms", []))
            matched_syms = key_syms.intersection(set(user_symptoms))
            score = len(matched_syms)
            scored.append((disease, info, score))

        scored.sort(key=lambda x: (-x[2], x[0]))  # Sort by score descending

        top = scored[:max_results]
        return {disease: info for disease, info, _ in top}

    def show_result(self):
        if not self.result:
            print("\nWe could not determine a condition based on your symptoms. Please consult a healthcare provider.")
            return

        print("\nPossible Diagnosis:")
        print("-" * 60)
        for disease, info in self.result.items():
            print(f"Disease: {disease}")
            print(f"Recommended Advice: {info.get('advice', 'No advice provided.')}")
            print(f"Source: {info.get('source', 'N/A')}")
            print("-" * 60)

        print("Note: This is not a medical diagnosis. Please consult a professional for medical advice.")
