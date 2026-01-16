import requests

AMOUNT = 10
TYPE = "boolean"
URL = "https://opentdb.com/api.php"

def fetch_questions():
    parameters = {
        "amount": AMOUNT,
        "type": TYPE
    }

    try:
        response = requests.get(URL, params=parameters)
        response.raise_for_status()
        data = response.json()
        return data["results"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

question_data = fetch_questions()