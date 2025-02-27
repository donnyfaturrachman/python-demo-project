import json
import os

def split_birth_records(input_file, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the input JSON file
    with open(input_file, "r", encoding="utf-8") as file:
        records = json.load(file)

    # Dictionary to store categorized records
    state_records = {}

    for record in records:
        state = record.get("birth_state", "Unknown")  # Handle missing states
        if state not in state_records:
            state_records[state] = []
        state_records[state].append(record)

    # Write separate JSON files for each state
    for state, data in state_records.items():
        state_filename = f"{output_dir}/{state.replace(' ', '_')}.json"
        with open(state_filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"Saved {len(data)} records to {state_filename}")

# Example usage
input_json = "birth_records.json"  # Change this to your actual JSON file
output_folder = "output_states"
split_birth_records(input_json, output_folder)
