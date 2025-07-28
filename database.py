disease_db = {
    "Influenza (Flu)": {
        "symptoms": ["fever", "cough", "headache"],
        "key_symptoms": ["fever", "cough"],
        "advice": "Stay hydrated and rest. Seek help if symptoms worsen.",
        "source": "WHO"
    },
    "Meningitis": {
        "symptoms": ["fever", "headache", "vomiting", "stiff neck"],
        "key_symptoms": ["stiff neck", "fever"],
        "advice": "Seek immediate medical attention.",
        "source": "CDC"
    },
    "Migraine": {
        "symptoms": ["headache", "nausea", "sensitivity to light"],
        "key_symptoms": ["headache"],
        "advice": "Lie in a dark room. Consider migraine medication if diagnosed.",
        "source": "Mayo Clinic"
    },
    "Common Cold": {
        "symptoms": ["sneezing", "cough", "sore throat", "runny nose", "headache"],
        "key_symptoms": ["runny nose", "sneezing"],
        "advice": "Rest, stay hydrated, and use over-the-counter remedies. Seek help if symptoms worsen.",
        "source": "NHS.uk"
    },
    "Flu": {
        "symptoms": ["fever", "chills", "muscle aches", "cough", "fatigue", "headache"],
        "key_symptoms": ["fever", "muscle aches"],
        "advice": "Rest, drink plenty of fluids, and take paracetamol. Seek help for breathing issues.",
        "source": "CDC"
    },
    "Malaria": {
        "symptoms": ["fever", "chills", "sweating", "headache", "nausea", "vomiting"],
        "key_symptoms": ["fever", "chills"],
        "advice": "Seek immediate medical treatment. Do not self-medicate.",
        "source": "WHO"
    },
    "Typhoid": {
        "symptoms": ["fever", "abdominal pain", "fatigue", "loss of appetite", "headache"],
        "key_symptoms": ["fever", "abdominal pain"],
        "advice": "Drink clean water and consult a doctor for antibiotics.",
        "source": "NHS.uk"
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "loss of smell", "fatigue", "shortness of breath"],
        "key_symptoms": ["loss of smell", "cough"],
        "advice": "Isolate and monitor symptoms. Seek help if breathing becomes difficult.",
        "source": "CDC"
    },
    "Community‑acquired Pneumonia": {
        "symptoms": [
            "fever", "cough", "shortness of breath", "sharp chest pain",
            "muscle aches", "headache", "fatigue", "loss of appetite",
            "nausea", "diarrhea", "rapid heartbeat"
        ],
        "key_symptoms": ["cough", "fever", "shortness of breath"],
        "advice": (
            "Seek medical evaluation. Often requires antibiotics if bacterial; "
            "stay hydrated and rest."
        ),
        "source": "American Lung Association"
    },
    "Legionnaires' Disease": {
        "symptoms": [
            "fever", "high fever", "cough", "shortness of breath",
            "muscle pain", "headache", "nausea", "vomiting", "diarrhea"
        ],
        "key_symptoms": ["high fever", "cough", "shortness of breath"],
        "advice": (
            "Seek urgent medical care. Treated with specific antibiotics; "
            "ensure water systems are well maintained."
        ),
        "source": "CDC"
    },
    "Q Fever": {
        "symptoms": [
            "fever", "severe headache", "muscle pain", "joint pain",
            "fatigue", "dry cough", "nausea", "vomiting", "diarrhea",
            "loss of appetite"
        ],
        "key_symptoms": ["fever", "severe headache", "muscle pain"],
        "advice": (
            "Consult a doctor promptly—acute Q fever may require antibiotics; "
            "monitor for prolonged fatigue."
        ),
        "source": "CDC"
    },
    "Yellow Fever": {
        "symptoms": ["fever", "chills", "headache", "muscle pain", "nausea", "loss of appetite", "jaundice"],
        "key_symptoms": ["fever", "jaundice"],
        "advice": ("Seek medical attention immediately. Prevention via vaccination is critical; "
                   "avoid mosquito exposure."),
        "source": "WHO"
    },
    "Whooping Cough (Pertussis)": {
        "symptoms": ["runny nose", "fever", "severe cough", "vomiting", "fatigue"],
        "key_symptoms": ["severe cough", "whooping sound"],
        "advice": ("Isolate infected individuals, seek antibiotic treatment early, "
                   "ensure vaccination."),
        "source": "CDC"
    },
    "Hand, Foot, and Mouth Disease": {
        "symptoms": ["fever", "blisters on hands", "blisters on feet", "blisters in mouth", "rash"],
        "key_symptoms": ["fever", "blisters on hands/feet"],
        "advice": ("Provide supportive care; maintain hydration, treat pain with children’s analgesics, "
                   "practice good hygiene to prevent spread."),
        "source": "CDC"
    },
    "Shigellosis": {
        "symptoms": ["abdominal cramps", "diarrhea (may include blood/mucus)", "fever", "vomiting"],
        "key_symptoms": ["bloody diarrhea", "abdominal cramps"],
        "advice": ("Seek medical care for rehydration and antibiotics if severe; practice handwashing "
                   "and safe food handling."),
        "source": "WHO"
    },
    "Yersiniosis": {
        "symptoms": ["fever", "abdominal pain", "bloody diarrhea", "vomiting"],
        "key_symptoms": ["bloody diarrhea", "abdominal pain"],
        "advice": ("Seek medical evaluation; drink fluids and treat symptoms; antibiotics may be needed "
                   "in severe cases."),
        "source": "CDC"
    },
    "Adenovirus Infection": {
        "symptoms": ["fever", "cough", "sore throat", "conjunctivitis", "gastroenteritis"],
        "key_symptoms": ["fever", "cough"],
        "advice": ("Practice good hand hygiene and avoid contact with sick people; "
                   "treatment is supportive and symptoms often resolve on their own."),
        "source": "CDC / WHO"
    },
    "Infectious Mononucleosis": {
        "symptoms": ["fever", "sore throat", "swollen lymph nodes", "fatigue", "headache"],
        "key_symptoms": ["sore throat", "fatigue"],
        "advice": ("Get plenty of rest, stay hydrated, avoid strenuous activities; "
                   "contact a doctor if symptoms persist."),
        "source": "Mayo Clinic"
    },
    "Rocky Mountain Spotted Fever": {
        "symptoms": ["fever", "headache", "rash", "muscle pain", "vomiting"],
        "key_symptoms": ["rash", "fever", "headache"],
        "advice": ("Seek urgent medical care; treatment with doxycycline should begin early."),
        "source": "CDC"
    },
    "West Nile Fever": {
        "symptoms": ["fever", "headache", "muscle aches", "rash", "vomiting", "diarrhea"],
        "key_symptoms": ["fever", "headache", "muscle aches"],
        "advice": ("Prevent mosquito bites; seek medical care if neurologic symptoms develop."),
        "source": "CDC"
    },
    "Measles": {
        "symptoms": ["fever", "cough", "runny nose", "red eyes", "rash"],
        "key_symptoms": ["fever", "rash", "runny nose"],
        "advice": ("Supportive care only; vaccination prevents disease; isolate and monitor for complications."),
        "source": "WHO"
    },
    "Lyme Disease": {
        "symptoms": ["fever", "chills", "headache", "tick‑bite rash", "fatigue", "joint pain"],
        "key_symptoms": ["tick‑bite rash", "fever"],
        "advice": ("Remove ticks carefully; early treatment with antibiotics is critical; seek doctor."),
        "source": "CDC"
    },
    "Dengue Fever": {
        "symptoms": ["fever", "severe headache", "pain behind the eyes", "joint pain", "rash", "nausea"],
        "key_symptoms": ["high fever", "severe headache", "joint pain"],
        "advice": ("Avoid mosquito exposure; stay hydrated and seek medical care for warning signs."),
        "source": "WHO"
    },
    "Zika Virus Infection": {
        "symptoms": ["mild fever", "rash", "joint pain", "conjunctivitis", "muscle aches", "headache"],
        "key_symptoms": ["rash", "joint pain", "fever"],
        "advice": ("Avoid mosquito bites; pregnant women should avoid exposure; supportive care only."),
        "source": "CDC"
    },
    "Trichomoniasis": {
        "symptoms": ["genital itching", "thin vaginal discharge", "burning with urination", "pain during sex"],
        "key_symptoms": ["itching", "abnormal discharge"],
        "advice": ("Seek medical evaluation; treat with metronidazole or tinidazole."),
        "source": "CDC"
    },
    "Hand, Foot, and Mouth Disease": {
        "symptoms": ["fever", "blisters on hands", "blisters on feet", "blisters in mouth", "rash"],
        "key_symptoms": ["fever", "blisters on hands/feet"],
        "advice": ("Supportive care; maintain hydration and hygiene; avoid contact with infected."),
        "source": "CDC"
    },
    "Systemic Lupus Erythematosus": {
        "symptoms": ["joint pain", "fatigue", "fever", "butterfly rash", "photosensitivity"],
        "key_symptoms": ["butterfly rash", "joint pain"],
        "advice": "Consult a rheumatologist for diagnosis and management. Avoid sun exposure.",
        "source": "Wikipedia / Mayo Clinic"
    },
    "Multiple Sclerosis": {
        "symptoms": ["fatigue", "numbness", "balance issues", "vision loss", "muscle weakness"],
        "key_symptoms": ["numbness", "vision issues"],
        "advice": "See a neurologist; treatments can slow progression and relieve symptoms.",
        "source": "Wikipedia / Mayo Clinic"
    },
    "Rheumatoid Arthritis": {
        "symptoms": ["joint swelling", "joint stiffness", "fatigue", "low-grade fever"],
        "key_symptoms": ["joint swelling", "stiffness"],
        "advice": "Early diagnosis and treatment by a rheumatologist can prevent joint damage.",
        "source": "Wikipedia / NIAMS"
    },
    "Celiac Disease": {
        "symptoms": ["abdominal pain", "diarrhea", "fatigue", "weight loss"],
        "key_symptoms": ["abdominal pain", "diarrhea"],
        "advice": "Seek medical testing for gluten sensitivity; maintain a strict gluten-free diet.",
        "source": "Wikipedia / PubMed Health"
    },
    "Type 1 Diabetes": {
        "symptoms": ["increased thirst", "frequent urination", "weight loss", "fatigue"],
        "key_symptoms": ["thirst", "frequent urination"],
        "advice": "Consult a physician; insulin therapy is required for blood glucose control.",
        "source": "Wikipedia / NIH"
    },
    "Fibromyalgia": {
        "symptoms": ["widespread pain", "fatigue", "sleep issues", "headache", "stiffness"],
        "key_symptoms": ["widespread pain", "fatigue"],
        "advice": "Seek help from a pain specialist; management includes medication, exercise, and therapy.",
        "source": "Wikipedia"  # symptoms described :contentReference[oaicite:1]{index=1}
    },
    "Cholera": {
        "symptoms": ["severe diarrhea", "vomiting", "dehydration", "leg cramps", "low blood pressure"],
        "key_symptoms": ["severe diarrhea", "vomiting"],
        "advice": "Immediate rehydration therapy; antibiotics may be needed in severe cases.",
        "source": "WHO"
    },
    "Chagas Disease": {
        "symptoms": ["fever", "fatigue", "swelling at infection site", "heart issues"],
        "key_symptoms": ["fever", "swelling at site"],
        "advice": "See an infectious disease specialist; antiparasitic treatment effective if started early.",
        "source": "WHO"
    },
    "Onchocerciasis": {
        "symptoms": ["skin itching", "skin nodules", "vision loss"],
        "key_symptoms": ["skin nodules", "itching"],
        "advice": "Mass drug administration programs are effective; consult public health services.",
        "source": "WHO"
    },
    "Leishmaniasis": {
        "symptoms": ["skin ulcers", "fever", "weight loss", "enlarged spleen"],
        "key_symptoms": ["skin ulcers", "fever"],
        "advice": "Specialist diagnosis and antiparasitic therapy are needed.",
        "source": "WHO"
    },
    "Measles": {
        "symptoms": ["fever", "cough", "runny nose", "red eyes", "rash"],
        "key_symptoms": ["fever", "rash"],
        "advice": "Supportive care; vaccination prevents disease and stops spread.",
        "source": "WHO / CDC"
    },
    "Lyme Disease": {
        "symptoms": ["fever", "headache", "tick‑bite rash", "joint pain", "fatigue"],
        "key_symptoms": ["tick‑bite rash", "joint pain"],
        "advice": "Early antibiotic treatment after tick removal; avoid ticks.",
        "source": "CDC"
    },
    "Dengue Fever": {
        "symptoms": ["high fever", "severe headache", "pain behind eyes", "joint pain", "rash"],
        "key_symptoms": ["high fever", "severe headache"],
        "advice": "Hydration and medical monitoring; severe forms need hospitalization.",
        "source": "WHO / CDC"
    },
    "Zika Virus Infection": {
        "symptoms": ["mild fever", "rash", "joint pain", "red eyes", "muscle aches"],
        "key_symptoms": ["rash", "joint pain"],
        "advice": "Pregnant women should avoid exposure; supportive care only.",
        "source": "CDC"
    },
    "West Nile Fever": {
        "symptoms": ["fever", "headache", "muscle aches", "rash", "fatigue"],
        "key_symptoms": ["fever", "headache"],
        "advice": "Prevent mosquito bites; see a physician if neurologic symptoms occur.",
        "source": "CDC / Wikipedia"  # :contentReference[oaicite:2]{index=2}
    },
    "Rocky Mountain Spotted Fever": {
        "symptoms": ["fever", "headache", "rash", "muscle pain", "vomiting"],
        "key_symptoms": ["rash", "fever"],
        "advice": "Seek urgent medical care; early doxycycline treatment is critical.",
        "source": "CDC"
    },
    "Q Fever": {
        "symptoms": ["fever", "severe headache", "muscle pain", "fatigue"],
        "key_symptoms": ["fever", "headache"],
        "advice": "Seek medical evaluation; acute cases require antibiotics.",
        "source": "CDC"
    },
    "Pertussis (Whooping Cough)": {
        "symptoms": ["runny nose", "fever", "severe cough", "vomiting", "fatigue"],
        "key_symptoms": ["severe cough", "whooping sound"],
        "advice": "Early antibiotics; vaccination and isolation recommended.",
        "source": "CDC"
    },
    "Hand, Foot, and Mouth Disease": {
        "symptoms": ["fever", "blisters on hands", "blisters on feet", "rash", "mouth ulcers"],
        "key_symptoms": ["fever", "blisters"],
        "advice": "Hydration and hygiene; self‑limiting in children.",
        "source": "CDC"
    },
    "Mononucleosis": {
        "symptoms": ["fever", "sore throat", "swollen lymph nodes", "fatigue"],
        "key_symptoms": ["sore throat", "fatigue"],
        "advice": "Rest, hydration, avoid contact sports; seek care if persistent.",
        "source": "Mayo Clinic / Wikipedia"
    },
    "RSV Infection": {
        "symptoms": ["fever", "cough", "wheezing", "runny nose", "difficulty breathing"],
        "key_symptoms": ["cough", "wheezing"],
        "advice": "Maintain airway, hydration; seek urgent care in infants and elderly.",
        "source": "CDC"
    },
    "Strep Throat": {
        "symptoms": ["sore throat", "fever", "headache", "swollen glands"],
        "key_symptoms": ["sore throat", "fever"],
        "advice": "Throat culture + antibiotics; rest and fluids.",
        "source": "CDC"
    },
    "Gastroenteritis (Stomach Flu)": {
        "symptoms": ["vomiting", "diarrhea", "abdominal cramps", "fever"],
        "key_symptoms": ["vomiting", "diarrhea"],
        "advice": "Oral rehydration solutions; seek care if dehydration occurs.",
        "source": "CDC"
    },
    "Ringworm": {
        "symptoms": ["round itchy rash", "scaly skin", "nail discoloration"],
        "key_symptoms": ["round rash", "itchiness"],
        "advice": "Apply antifungal creams; seek care if widespread or nails involved.",
        "source": "CDC / Mayo Clinic"
    },
    "Scabies": {
        "symptoms": ["intense itching", "rash", "small burrow tracks"],
        "key_symptoms": ["itching", "burrows"],
        "advice": "Prescription cream; wash bedding; treat close contacts.",
        "source": "CDC"
    },
    "Pinworm Infection": {
        "symptoms": ["anal itching (especially at night)", "restlessness", "abdominal discomfort"],
        "key_symptoms": ["anal itching at night"],
        "advice": "Over-the-counter treatments; wash hands and bedding frequently.",
        "source": "CDC"
    },
    "Giardiasis": {
        "symptoms": ["diarrhea", "abdominal cramps", "nausea", "weight loss"],
        "key_symptoms": ["diarrhea", "abdominal cramps"],
        "advice": "Seek medical testing; treat with prescribed antiparasitics.",
        "source": "CDC / WHO"
    },
    "Shigellosis": {
        "symptoms": ["bloody diarrhea", "abdominal cramps", "fever", "vomiting"],
        "key_symptoms": ["bloody diarrhea", "abdominal cramps"],
        "advice": "Hydration; antibiotics if severe; practice hand hygiene.",
        "source": "WHO / CDC"
    },
    "Yersiniosis": {
        "symptoms": ["bloody diarrhea", "abdominal pain", "fever", "vomiting"],
        "key_symptoms": ["bloody diarrhea", "abdominal pain"],
        "advice": "Medical evaluation; treat with antibiotics if needed.",
        "source": "CDC"
    },
    "Yellow Fever": {
        "symptoms": ["fever", "jaundice", "muscle pain", "nausea", "headache"],
        "key_symptoms": ["fever", "jaundice"],
        "advice": "Immediate medical care; vaccination and mosquito control.",
        "source": "WHO"
    },
    "Q Fever": {
        "symptoms": ["fever", "severe headache", "fatigue", "muscle pain"],
        "key_symptoms": ["fever", "headache"],
        "advice": "See healthcare provider; antibiotics required in many cases.",
        "source": "CDC"
    },
}