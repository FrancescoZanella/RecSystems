from tqdm import tqdm
import numpy as np

def evaluate_algorithm(URM_test, recommender_object, at=10):
    
    cumulative_AP = 0.0
    
    num_eval = 0

    # we look for all the users
    for user_id in tqdm(range(URM_test.shape[0])):
        
        # we get the relevant items for this user
        relevant_items = URM_test.indices[URM_test.indptr[user_id]:URM_test.indptr[user_id+1]]
        
        # if the user have something in the test data we evaluate it
        if len(relevant_items)>0:
            
            recommended_items = recommender_object.recommend(user_id)
            num_eval+=1

            cumulative_AP += AP(recommended_items, relevant_items)
            
    MAP = cumulative_AP / num_eval
    
    return MAP

def AP(recommended_items, relevant_items):
   
    is_relevant = np.in1d(recommended_items, relevant_items, assume_unique=True)
    
    # Cumulative sum: precision at 1, at 2, at 3 ...
    p_at_k = is_relevant * np.cumsum(is_relevant, dtype=np.float32) / (1 + np.arange(is_relevant.shape[0]))
    
    ap_score = np.sum(p_at_k) / np.min([relevant_items.shape[0], is_relevant.shape[0]])

    return ap_score

def recall(recommended_items, relevant_items):

    is_relevant = np.in1d(recommended_items, relevant_items, assume_unique=True)

    recall_score = np.sum(is_relevant, dtype=np.float32) / relevant_items.shape[0]

    return recall_score
def evaluate_algorithm_recall(URM_test, recommender_object, at=10):

    
    cumulative_recall = 0.0
    

    num_eval = 0


    for user_id in range(URM_test.shape[0]):

        relevant_items = URM_test.indices[URM_test.indptr[user_id]:URM_test.indptr[user_id+1]]

        if len(relevant_items)>0:

            recommended_items = recommender_object.recommend(user_id,cutoff=10)
            num_eval+=1


            cumulative_recall += recall(recommended_items, relevant_items)



    cumulative_recall /= num_eval


    return cumulative_recall 