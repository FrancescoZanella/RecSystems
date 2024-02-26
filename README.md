![Header](screenshots/download.jpg)
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


## Credits
This repository is based on [Maurizio Ferrari Dacrema Repository](https://github.com/MaurizioFD/RecSys_Course_AT_PoliMi).

