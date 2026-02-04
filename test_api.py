import requests
import json

url = "http://127.0.0.1:8001/predict"
payload = {
    "person_age": 28,
    "person_gender": "male",
    "person_education": "Bachelor",
    "person_income": 550000,
    "person_emp_exp": 4,
    "person_home_ownership": "RENT",
    "loan_amnt": 120000,
    "loan_intent": "EDUCATION",
    "loan_int_rate": 11.5,
    "loan_percent_income": 0.22,
    "cb_person_cred_hist_length": 6,
    "credit_score": 720,
    "previous_loan_defaults_on_file": "NO"
}

try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")
