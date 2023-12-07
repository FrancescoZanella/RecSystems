import re
import pandas as pd
import ast

def function(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        log_content = file.read()

    pattern = re.compile(r'alpha: ([\d.]+), beta: ([\d.]+), gamma: ([\d.]+), delta:([\d.]+) e MAP: ([\d.]+)')

    matches = pattern.findall(log_content)

    # Lists for DataFrame columns
    alpha = []
    beta = []
    gamma = []
    delta = []
    accuracy = []
    

    # Extract data from the log
    for row in matches:
        alpha.append(row[0])
        beta.append(row[1])
        gamma.append(row[2])
        delta.append(row[3])
        accuracy.append(row[4])
        

    # Create the DataFrame
    df = pd.DataFrame({
        'alpha': alpha,
        'beta': beta,
        'gamma': gamma,
        'delta': delta,
        'accuracy': accuracy,
    })

    # Save the DataFrame to a CSV file
    df.to_csv(output_path, index=False)

function("C:\\Users\\franc\\Desktop\\RecSystems\\scripts\\prova.txt","C:\\Users\\franc\\Desktop\\RecSystems\\MyTuning\\HYBRID\\merge_similarities\\grid_search.csv")

