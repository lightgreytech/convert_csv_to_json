import argparse
import csv
import json
import os

def csv_to_json(csv_file, output_folder):
    # Initialize an empty list to store the data
    data = []

    # Open the CSV file for reading
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append each row as a dictionary to the data list
            data.append(row)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate the output JSON file path within the output folder
    json_file = os.path.join(output_folder, os.path.splitext(os.path.basename(csv_file))[0] + ".json")

    # Open the JSON file for writing
    with open(json_file, 'w') as file:
        # Write the data list to the JSON file
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Convert CSV to JSON")
    parser.add_argument("csv_file", type=str, help="Path to the input CSV file")

    # Parse the command line arguments
    args = parser.parse_args()

    # Determine the output folder based on the input CSV file
    output_folder = os.path.join(os.path.dirname(args.csv_file), "output")

    # Call the function to convert CSV to JSON
    csv_to_json(args.csv_file, output_folder)