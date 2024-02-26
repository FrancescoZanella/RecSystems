<p align="center">
  <img width="100%" src="https://i.imgur.com/tm9mSuM.png" alt="header" />
</p>
<p align="center">
    <img src="https://i.imgur.com/mPb3Qbd.gif" width="180" alt="Politecnico di Milano"/>
</p>


# Recommender System Challenge 2023/2024 Polimi 
This repository contains the data and the code used in [Polimi Kaggle competition](https://www.kaggle.com/competitions/recommender-system-2023-challenge-polimi).
The application domain is book recommendation. The datasets provided contains interactions of users with books, in particular, if the user attributed to the book a rating of at least 4. 
The main goal of the competition is to discover which items (books) a user will interact with.

## Dataset
The datasets includes around 600k interactions, 13k users, 22k items (books).
The training-test split is done via random holdout, 80% training, 20% test.
The goal is to recommend a list of 10 potentially relevant items for each user. MAP@10 is used for evaluation. You can use any kind of recommender algorithm you wish written in Python.

## Results
Deadline 2 (final):
 - Public leaderboard: 2th
 - Private leaderboard: 3th
Deadline 1:
 - Public leaderboard: 2th
 - Private leaderboard: 2th

There were 63 teams in competition.

## Recommender

The recommender system that we used to achieve the third position in the challenge was a model composed of a hybrid approach where we combined:
  - **Slim Elastic Net**
  - **Item KNN**
  - **Rp3Beta**
 We integrated the similarity matrices by assigning different weights to each recommender based on hyperparameter tuning conducted in [Optuna](https://optuna.org/).

## XGBoost

We used XGB to further improve the performances of our model.
We used as features:
  - **Top Popular**
  - **RP3beta** 
  - **SLIMen**
  - **SLIMbpr**
  - **ItemKNN**
  - **The best hybrid (SLIMen + ItemKNN + RP3b)**
  - **P3alpha**
  - **User profile length**
  - **Item popularity**

This is a representation of the architecture:

<p align="center">
<img src="https://github.com/FrancescoZanella/RecSystems/blob/master/screenshoots/Immagine1.png" width="600" height="400">
</p>

N.B. the candidate generator we have used is strongly optimized on recall, no more on MAP.


## Hyperparameters tuning

The hyperparameters tuning was done using:
  - **Kaggle** free GPU plan
  - **Asus Zenbook**

## Contributors

[Francesco Zanella](https://github.com/FrancescoZanella)

[Federico CIliberto](https://github.com/FedericoCiliberto)

## Credits
This repository is based on [Maurizio Ferrari Dacrema Repository](https://github.com/MaurizioFD/RecSys_Course_AT_PoliMi).

