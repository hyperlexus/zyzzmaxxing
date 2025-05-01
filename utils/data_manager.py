import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data" / "gym_data.json"

def get_data():
    if not DATA_DIR.exists():
        save_data({})
    with open(DATA_DIR) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_DIR, "w") as f:
        json.dump(data, f, indent=4)

def get_user_data(data, user_id):
    return data.setdefault(str(user_id), {"workouts": [], "plan": [], "last_workout": None, "points": 0, "streak": 0})