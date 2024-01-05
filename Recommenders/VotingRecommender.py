import numpy as np
import scipy.sparse as sps
from Recommenders.BaseRecommender import BaseRecommender

class VotingRecommender(BaseRecommender):
    """ VotingRecommender
    Voting recommender
    """

    RECOMMENDER_NAME = "VotingRecommender"

    def __init__(self, URM_train, recommenders_list,cutoffs_list):
        super(VotingRecommender, self).__init__(URM_train)

        self.URM_train = sps.csr_matrix(URM_train)
        self.recommenders_list=recommenders_list
        self.cutoffs_list=cutoffs_list
        
        

    def recommend(self,user_id,cutoff):
        results_array = np.array([])
        items1=self.recommenders_list[0].recommend(user_id,self.cutoffs_list[0])
        items2=self.recommenders_list[1].recommend(user_id,self.cutoffs_list[1])
        items3=self.recommenders_list[2].recommend(user_id,self.cutoffs_list[2])
        common_elements = np.intersect1d(np.intersect1d(items1, items2), items3)
        results_array = np.append(results_array, common_elements)
    
        common_elements = np.intersect1d(items1, items2)
        common_elements= np.setdiff1d(common_elements,results_array)
        results_array = np.append(results_array, common_elements)
    
        common_elements = np.intersect1d(items1, items3)
        common_elements= np.setdiff1d(common_elements,results_array)
        results_array = np.append(results_array, common_elements)
    
        common_elements = np.intersect1d(items2, items3)
        common_elements= np.setdiff1d(common_elements,results_array)
        results_array = np.append(results_array, common_elements)
    
        common_elements=np.setdiff1d(items1,results_array)
        results_array=np.append(results_array,common_elements)
    
        common_elements=np.setdiff1d(items2,results_array)
        results_array=np.append(results_array,common_elements)
    
        common_elements=np.setdiff1d(items3,results_array)
        results_array=np.append(results_array,common_elements)
    
        results_array=results_array[:cutoff]
        result_list = results_array.tolist()
        return result_list
        
