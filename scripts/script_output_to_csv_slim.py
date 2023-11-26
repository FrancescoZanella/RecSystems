import re
import pandas as pd
import ast

"""
script per prendere da output hyperparameters e salvarli in un excel
"""


def function(input_path, output_path):
    with open(input_path, 'r') as file:
        log_content = file.read()
    # Definisci il modello di regex per estrarre i valori di accuracy e i parametri
    pattern = re.compile(r'Trial (\d+) finished with value: ([\d.]+) and parameters: ({.+?}).*?')

    matches = pattern.findall(log_content)




    # Creazione delle liste per le colonne del dataframe
    trialid = []
    accuracy = []
    topk = []
    l1_ratio = []
    alpha = [] 
   

    # Estrazione dei dati dalle righe
    for row in matches:
        trialid.append(row[0])
        accuracy.append(row[1])
        topk.append(row[2])
        l1_ratio.append(row[3])
        alpha.append(row[4])
        

    # Creazione del dataframe
    df = pd.DataFrame({
        'trialid': trialid,
        'accuracy': accuracy,
        'topk': topk,
        'l1_ratio': l1_ratio,
        'alpha': alpha
    })

    # Visualizza il dataframe
    df.to_csv(output_path, index=False)




