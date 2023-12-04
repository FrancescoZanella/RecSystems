import plotly.express as px
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


def generate_random_forest(path_csv_file_to_analyze,columns_to_categorical = [], columns_to_drop = [], rows_to_skip=3, target = 'accuracy'):
    

    # Carica i dati da CSV
    data = pd.read_csv(path_csv_file_to_analyze, header = rows_to_skip)
    data = data[data['similarity'] != 'euclidean']


    #drop the target column
    X = data.drop(target, axis=1)
    #drop any empty column name
    X = X.dropna(axis=1, how='all')
    

    # convert into categorical
    for col in columns_to_categorical:
        X = pd.get_dummies(X, columns=[col], prefix=col)

    #drop columns to drop
    for col in columns_to_drop:
        X = X.drop(col, axis = 1)

    X = X.fillna(0)

    y = data[target]
    


    
    
    # Dividi i dati in set di addestramento e test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Crea il modello Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Addestra il modello
    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X_test)

    # Calcola l'accuracy (in questo caso, usiamo l'errore quadratico medio per valutare la performance)
    accuracy = 1 - mean_squared_error(y_test, y_pred)

    

    # Valuta l'importanza delle features
    feature_importances = rf_model.feature_importances_

    # Associa le importanze alle features
    feature_importance_dict = dict(zip(X.columns, feature_importances))

    # Ordina le feature in base all'importanza
    sorted_features = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)



    # Visualizza un grafico dell'importanza delle features
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(feature_importances)), feature_importances, align='center')
    plt.xticks(range(len(feature_importances)), X.columns, rotation=90)
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.title('Feature Importance in Random Forest Model')
    plt.show()
    
    

def create_3D_graph(path_input_csv, rows_to_skip=3, target_col = 'accuracy', dimensions = ['topK', 'l1_ratio', 'alpha'],threshold=None):
    

    # Load your dataset
    # Replace 'your_dataset.csv' with the actual path to your CSV file
    df = pd.read_csv(path_input_csv, header = rows_to_skip)
    if threshold is not None:
        df = df[df[target_col] >= threshold]
    # Create an interactive 3D scatter plot with color-coded points based on the 'result' column
    fig = px.scatter_3d(df, x=dimensions[0], y=dimensions[1], z=dimensions[2], color= target_col, opacity=0.7, color_continuous_scale='viridis')

    # Set axis labelsa
    fig.update_layout(scene=dict(xaxis_title=dimensions[0], yaxis_title=dimensions[1], zaxis_title=dimensions[2]))

    # Show the plot
    fig.show()


create_3D_graph("C:\\Users\\franc\\Desktop\\RecSys\\DATASETS\\RecSys_Course_AT_PoliMi\\MyTuning\\P3_alpha\\step2.csv",rows_to_skip=0,target_col='result',dimensions=["topK","alpha","alpha"])