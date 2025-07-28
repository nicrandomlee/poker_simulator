import json

def save_simulation_results(results_dict, filename="simulation_results.json"):
    results_dict_str_keys = {"-".join(key): value for key, value in results_dict.items()}
    with open(filename, "w") as f:
        json.dump(results_dict_str_keys, f, indent=4)

def load_simulation_results(filename="simulation_results.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        # Convert string keys back to tuple keys
        converted_data = {}
        for key_str, value in data.items():
            # Split the key string by "-" to get the cards as tuple
            tuple_key = tuple(key_str.split("-"))
            converted_data[tuple_key] = value
        return converted_data
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn’t exist

