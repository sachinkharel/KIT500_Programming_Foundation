import json

def save_dict_to_json(data_dict, output_file):
    """
    Saves a dictionary to a JSON file.

    Args:
        data_dict (dict): The dictionary to be saved.
        output_file (str): The path to the output JSON file.

    Returns:
        None
    """
    try:
        # Open the file in write mode and dump the dictionary as JSON
        with open(output_file, 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
        print(f"Data has been successfully written to {output_file}")
    except (TypeError, IOError) as e:
        # Handle exceptions related to JSON serialization or file I/O
        print(f"An error occurred while saving the dictionary to JSON: {e}")
