import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Carica i dati da CSV
data = pd.read_csv('C:\\Users\\franc\\Desktop\\RecSys\DATASETS\\RecSys_Course_AT_PoliMi\\MyTuning\\output.csv')

# Dividi i dati in input (X) e output (y)
X = data.drop(['trialid', 'accuracy'], axis=1)  # Rimuovi trialid e accuracy dalle features
y = data['accuracy']

# Dividi i dati in set di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea il modello Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Addestra il modello
rf_model.fit(X_train, y_train)

# Valuta l'importanza delle features
feature_importances = rf_model.feature_importances_

# Associa le importanze alle features
feature_importance_dict = dict(zip(X.columns, feature_importances))

# Ordina le feature in base all'importanza
sorted_features = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)

# Stampa le feature ordinate per importanza
for feature, importance in sorted_features:
    print(f"{feature}: {importance}")

# Visualizza un grafico dell'importanza delle features
plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importances)), feature_importances, align='center')
plt.xticks(range(len(feature_importances)), X.columns, rotation=90)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance in Random Forest Model')
plt.show()
