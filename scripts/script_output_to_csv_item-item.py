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
    """
    similarity = []
    shrink = []
    asymmetric_alpha = []
    normalize = []
    tversky_alpha = []
    tversky_beta = []
    normalize_avg_row = []
    similarity_from_distance_mode = []"""
    alpha = []
    beta = []
    normalize_similarity = []

    # Estrazione dei dati dalle righe
    for row in matches:
        trialid.append(row[0])
        accuracy.append(row[1])
        params = ast.literal_eval(row[2])  # Convertire la stringa di parametri in un dizionario
        #similarity.append(params.get('similarity', None))
        topk.append(params.get('topK', None))
        """shrink.append(params.get('shrink', None))
        asymmetric_alpha.append(params.get('asymmetric_alpha', None))
        normalize.append(params.get('normalize', None))
        tversky_alpha.append(params.get('tversky_alpha', None))
        tversky_beta.append(params.get('tversky_beta', None))
        normalize_avg_row.append(params.get('normalize_avg_row', None))
        similarity_from_distance_mode.append(params.get('similarity_from_distance_mode', None))
"""
        alpha.append(params.get('alpha', None))
        beta.append(params.get('beta', None))
        normalize_similarity.append(params.get('normalize_similarity', None))
    # Creazione del dataframe
    df = pd.DataFrame({
        'trialid': trialid,
        'accuracy': accuracy,
        #'similarity': similarity,
        'topk': topk,
        'alpha': alpha,
        'beta': beta,
        'normalize_similarity': normalize_similarity,})
        

    # Visualizza il dataframe
    # Salva il dataframe su un file Excel
    df.to_csv(output_path, index=False)

function("C:\\Users\\franc\\Desktop\\prova.txt","C:\\Users\\franc\\Desktop\\step1.csv")




