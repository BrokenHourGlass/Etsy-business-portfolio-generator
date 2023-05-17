import os
import json

# Specify the directory where your JSON files are
directory = 'catalog/'

# Loop over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"): # Ensure we're working with a JSON file
        filepath = os.path.join(directory, filename)
        
        # Open the file and load the JSON data
        with open(filepath, 'r') as file:
            data = json.load(file)

        # Go through the data and replace '\n' and multiple spaces
        for key, value in data.items():
            if isinstance(value, str):
                # Remove '\n'
                value = value.replace('\n', ' ')
                # Replace multiple spaces with a single space
                value = ' '.join(value.split())
                data[key] = value
        
        # Write the cleaned data back to the file
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
