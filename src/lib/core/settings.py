import json
import os

def get_settings(name: str):
    try:
        with open(f"data/settings/{name}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def set_settings(name: str, values: dict):
    if not isinstance(values, dict):
        raise ValueError("Values must be a dictionary")
    
    os.makedirs("data/settings", exist_ok=True)
    with open(f"data/settings/{name}.json", "w") as f:
        json.dump(values, f, indent=4)
    
def update_settings(name: str, key: str, value):
    settings = get_settings(name)
    settings[key] = value
    set_settings(name, settings)

def delete_settings(name: str):
    try:
        os.remove(f"data/settings/{name}.json")
    except FileNotFoundError:
        pass

def get_setting(name: str, key: str):
    settings = get_settings(name)
    return settings.get(key, None)