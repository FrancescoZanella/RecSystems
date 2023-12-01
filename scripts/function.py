import re
import pandas as pd

def extract_and_save_data(log_file_path, output_csv_path):
    # Read log text from the file
    with open(log_file_path, 'r') as file:
        log_text = file.read()

    # Extract data between curly braces using regular expression
    pattern = re.compile(r"\{([^}]+)\}")
    matches = pattern.findall(log_text)

    # Create a list of dictionaries
    data = [eval(match) for match in matches]

    # Create a Pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_path, index_label='index')

# Example usage:
input_log_file_path = 'path/to/your/input/log.txt'
output_csv_file_path = 'path/to/your/output/output.csv'
extract_and_save_data(input_log_file_path, output_csv_file_path)
