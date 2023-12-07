import numpy as np
from numpy import linalg as LA
import scipy.sparse as sps
from Recommenders.BaseRecommender import BaseRecommender

class ScoresHybridRecommender(BaseRecommender):
    """ ScoresHybridRecommender
    Hybrid of two prediction scores R = R1*alpha + R2*(1-alpha)

    """

    RECOMMENDER_NAME = "ScoresHybridRecommender"

    def __init__(self, URM_train, recommenders_list):
        super(ScoresHybridRecommender, self).__init__(URM_train)

        self.URM_train = sps.csr_matrix(URM_train)
        self.recommenders_list=recommenders_list
        
        
    def fit(self,norm=None,weights= None):
        try:
            assert len(weights) == len(self.recommenders_list)
        except AssertionError:
            print(f"Error: Weights list size is {len(weights)}, but expected size is {len(self.recommenders_list)}")
            
        try:
            assert sum(weights) == 1.0
        except AssertionError:
            print(f"Error: Weights sum is {sum(weights)}, but must be 1.0")
            
        self.weights = weights 
        self.norm=norm

    def _compute_item_score(self, user_id_array, items_to_compute):
        score=0.0
        for recommender,weight in zip(self.recommenders_list, self.weights):
            item_weight = recommender._compute_item_score(user_id_array)
            if self.norm is not None:
                norm_item_weight = LA.norm(item_weight, self.norm)
                if norm_item_weight == 0:
                    #raise ValueError("Norm {} of item weights for recommender is zero. Avoiding division by zero".format(self.norm))
                    score=score + item_weight * weight
                else:
                    score=score + item_weight/norm_item_weight * weight
            else:
                score=score + item_weight * weight
        return score