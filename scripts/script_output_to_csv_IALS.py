import re
import pandas as pd
import ast

def function(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        log_content = file.read()

    pattern = re.compile(r'Trial (\d+) finished with value: ([\d.]+) and parameters: ({.+?}).*?')

    matches = pattern.findall(log_content)

    # Lists for DataFrame columns
    trialid = []
    accuracy = []
    num_factors = []
    confidence_scaling = []
    alpha = []
    epsilon = []
    reg = []

    # Extract data from the log
    for row in matches:
        trialid.append(row[0])
        accuracy.append(row[1])
        params = ast.literal_eval(row[2])  # Convert the parameter string to a dictionary
        num_factors.append(params.get('num_factors', None))
        confidence_scaling.append(params.get('confidence_scaling', None))
        alpha.append(params.get('alpha', None))
        epsilon.append(params.get('epsilon', None))
        reg.append(params.get('reg', None))

    # Create the DataFrame
    df = pd.DataFrame({
        'trialid': trialid,
        'accuracy': accuracy,
        'num_factors': num_factors,
        'confidence_scaling': confidence_scaling,
        'alpha': alpha,
        'epsilon': epsilon,
        'reg': reg
    })

    # Save the DataFrame to a CSV file
    df.to_csv(output_path, index=False)



