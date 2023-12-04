best_pars_dict = {
  'SLIMElasticNetRecommender': {
      'topK': 7223, 
      'l1_ratio': 0.06907809571101771, 
      'alpha': 0.001247929408227769
    },
  'RP3betaRecommender': {
      'topK': 35,
      'alpha': 0.3640454616932409,
      'beta': 0.24726782706950345
    },
  'EASE_R_Recommender': {
      'topK': 17599, 
      'l2_norm': 94.71018506892186
    },
  'P3alphaRecommender': {
    'topk': 48,
    'alpha': 0.30190506275582196,
    'normalize_similarity' : True,
  },
  'ItemKNNCFRecommender': {
    'similarity': tversky,
    'topK': 36,
    'shrink': 29,
    'tversky_alpha': 1.741341923073262,
    'tversky_beta': 2.9148336121214324,
  },
  'SLIM_BPR_Recommender: {
    'epochs': 445,
    'lambda_i':0.00357814405695588,
    'lambda_j':0.0000517456087547006,
    'learning_rate' : 0.0110299013052305,
    'topK':18
  }
}
