import re
import pandas as pd
import ast

"""
script per prendere da output hyperparameters e salvarli in un excel
"""


def function(input_path, output_path):
    with open(input_path, 'r',encoding='utf-8') as file:
        log_content = file.read()
    # Definisci il modello di regex per estrarre i valori di accuracy e i parametri
    pattern = re.compile(r'Trial (\d+) finished with value: ([\d.]+) and parameters: ({.+?}).*?')

    matches = pattern.findall(log_content)

   




    # Creazione delle liste per le colonne del dataframe
    trialid = []
    accuracy = []
    topK = []
    l1_ratio = []
    alpha = [] 
   

    # Estrazione dei dati dalle righe
    for row in matches:
        trialid.append(row[0])
        accuracy.append(row[1])
        params = ast.literal_eval(row[2])  # Convertire la stringa di parametri in un dizionario
        topK.append(params.get('topK', None))
        l1_ratio.append(params.get('l1_ratio', None))
        alpha.append(params.get('alpha', None))
        

    # Creazione del dataframe
    df = pd.DataFrame({
        'trialid': trialid,
        'accuracy': accuracy,
        'topK': topK,
        'l1_ratio': l1_ratio,
        'alpha': alpha
    })

    # Visualizza il dataframe
    df.to_csv(output_path, index=False)






