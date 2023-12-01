import re
import ast
import pandas as pd

def function(log_file_path, output_csv_path):
    # Read log text from the file
    with open(log_file_path, 'r') as file:
        log_text = file.read()

    # Extract data between curly braces using regular expression
    pattern = re.compile(r"\{([^}]+)\}")
    matches = pattern.findall(log_text)

    # Create a list of dictionaries using ast.literal_eval
    data = []
    for match in matches:
        # Remove line breaks and whitespaces
        clean_match = match.replace('\n', '').replace(' ', '')
        # Evaluate the cleaned string
        evaluated_dict = ast.literal_eval(clean_match)
        data.append(evaluated_dict)

    # Create a Pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_path, index_label='index')
