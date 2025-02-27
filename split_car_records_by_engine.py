import json
import os

def split_car_records_by_engine(input_file, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the input JSON file
    with open(input_file, "r", encoding="utf-8") as file:
        car_records = json.load(file)

    # Dictionary to store categorized records by engine type
    engine_records = {}

    for record in car_records:
        engine_type = record.get("engine", "Unknown")  # Handle missing engine types
        if engine_type not in engine_records:
            engine_records[engine_type] = []
        engine_records[engine_type].append(record)

    # Write separate JSON files for each engine type
    for engine, cars in engine_records.items():
        engine_filename = f"{output_dir}/{engine.replace(' ', '_')}.json"
        with open(engine_filename, "w", encoding="utf-8") as file:
            json.dump(cars, file, indent=4)
        print(f"Saved {len(cars)} records to {engine_filename}")

# Example usage
input_json = "car_records.json"  # Change this to your actual JSON file
output_folder = "output_engines"
split_car_records_by_engine(input_json, output_folder)
