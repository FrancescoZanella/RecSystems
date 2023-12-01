import csv
import re

def function(input_path, output_path):
    with open(input_path, 'r') as file:
        content = file.read()

    blocks = re.findall(r'\[I.*?Trial (\d+).*?value: (.*?)(?=\[I|$)([\s\S]*?)(?=\[I|$)', content)

    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['trial_id', 'accuracy', 'num_factors', 'confidence_scaling', 'alpha', 'epsilon', 'reg']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for block in blocks:
            trial_id, accuracy, rest_of_block = block
            params_match = re.search(r"'num_factors': (\d+).*?'confidence_scaling': '(.*?)'.*?'alpha': ([\d.]+).*?'epsilon': ([\d.]+).*?'reg': ([\d.e+-]+)", rest_of_block)

            if params_match:
                writer.writerow({
                    'trial_id': trial_id,
                    'accuracy': accuracy,
                    'num_factors': params_match.group(1),
                    'confidence_scaling': params_match.group(2),
                    'alpha': params_match.group(3),
                    'epsilon': params_match.group(4),
                    'reg': params_match.group(5)
                })

