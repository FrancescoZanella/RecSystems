import re
import csv

def function(log_file_path, output_csv_path):
    # Regular expression pattern to extract trial, topK, l2_norm, and accuracy from log lines
    pattern = re.compile(r'Trial (\d+) finished with value: (\d+\.\d+) and parameters: {\'topK\': (\d+), \'l2_norm\': ([\d.]+)}.')

    # Columns for the CSV file
    columns = ['trial', 'topK', 'l2_norm', 'accuracy']

    # List to store extracted data
    data = []

    # Read the log file
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = pattern.search(line)
            if match:
                trial, accuracy, topK, l2_norm = match.groups()
                data.append([int(trial), int(topK), float(l2_norm), float(accuracy)])

    # Sort the data based on the 'trial' column
    data.sort(key=lambda x: x[0])

    # Write data to CSV file
    with open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        writer.writerows(data)


