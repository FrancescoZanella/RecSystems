import csv
import re

def parse_txt_to_csv(input_path, output_path):
    with open(input_path, 'r') as file:
        content = file.read()

    blocks = re.findall(r'\[I.*?Trial (\d+).*?value: (.*?). Best.*?\n([\s\S]*?)(?=\[I|$)', content)

    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['trial_id', 'accuracy', 'num_factors', 'confidence_scaling', 'alpha', 'epsilon', 'reg']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for block in blocks:
            trial_id, accuracy, rest_of_block = block
            params = re.search(r"parameters: \{(.*?)\}", rest_of_block).group(1)
            params_dict = dict(map(str.strip, param.split(':')) for param in params.split(','))

            writer.writerow({
                'trial_id': trial_id,
                'accuracy': accuracy,
                'num_factors': params_dict['num_factors'],
                'confidence_scaling': params_dict['confidence_scaling'],
                'alpha': params_dict['alpha'],
                'epsilon': params_dict['epsilon'],
                'reg': params_dict['reg']
            })

# Example usage:
parse_txt_to_csv('input.txt', 'output.csv')
