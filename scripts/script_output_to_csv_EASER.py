import re
import ast
import pandas as pd

def function(input_path, output_path):
    with open(input_path, 'r') as file:
        log_content = file.read()

    # Define the regex pattern to extract trial information and parameters
    pattern = re.compile(r'Trial (\d+) finished with value: ([\d.]+) and parameters: {\'topK\': (\d+), \'l2_norm\': ([\d.]+), \'normalize_matrix\': (True|False)}.*?')

    matches = pattern.findall(log_content)

    # Lists for DataFrame columns
    trialid = []
    accuracy = []
    topK = []
    l2_norm = []
    normalize_matrix = []

    # Extract data from rows
    for row in matches:
        trialid.append(row[0])
        accuracy.append(row[1])
        topK.append(row[2])
        l2_norm.append(row[3])
        normalize_matrix.append(row[4] == 'True')

    # Create the DataFrame
    df = pd.DataFrame({
        'trialid': trialid,
        'accuracy': accuracy,
        'topK': topK,
        'l2_norm': l2_norm,
        'normalize_matrix': normalize_matrix
    })

    # Save the DataFrame to a CSV file
    df.to_csv(output_path, index=False)


