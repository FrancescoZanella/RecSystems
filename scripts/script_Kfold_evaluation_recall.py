from tqdm import tqdm
import numpy as np

from Data_manager.split_functions.split_train_validation_random_holdout import split_train_in_two_percentage_global_sample

def create_folds(URM_all, k):
    n_el=URM_all.nnz
    URM_train_list=[]
    URM_validation_list=[]
    URM_remaining=URM_all
    for i in range(k):
        URM_remaining, URM_validation = split_train_in_two_percentage_global_sample(URM_remaining, train_percentage = ((n_el-(i+1)*n_el/k)/URM_remaining.nnz) )
        URM_train_list.append(URM_all - URM_validation)
        URM_validation_list.append(URM_validation)

    return URM_train_list, URM_validation_list


def recall(recommended_items, relevant_items):

    is_relevant = np.in1d(recommended_items, relevant_items, assume_unique=True)

    recall_score = np.sum(is_relevant, dtype=np.float32) / relevant_items.shape[0]

    return recall_score

def evaluate_algorithm(URM_test, recommender_object, at=10):

    cumulative_recall = 0.0

    num_eval = 0


    for user_id in range(URM_test.shape[0]):

        relevant_items = URM_test.indices[URM_test.indptr[user_id]:URM_test.indptr[user_id+1]]

        if len(relevant_items)>0:

            recommended_items = recommender_object.recommend(user_id,cutoff=at)
            num_eval+=1


            cumulative_recall += recall(recommended_items, relevant_items)



    cumulative_recall /= num_eval


    return cumulative_recall 

def kFold_evaluation(URM_all, model, parameters_dict_list, k=10):
    URM_train_list,URM_validation_list = create_folds(URM_all,k)
    res=0
    acc=0
    for j in range(len(parameters_dict_list)):
        print("COMBINATION " + str(j) + ":")
        for key, value in parameters_dict_list[j].items():
            print(f"{key}: {value}")
        acc=0
        for i in range(k):
            recommender=model(URM_train_list[i])
            recommender.fit(**parameters_dict_list[j])
            res=evaluate_algorithm(URM_validation_list[i],recommender, at=10)
            acc=acc+res
            print("Fold" + str(i)+" evaluation ended with value " + str(res))
        print("Evaluation on all folded ended. Average recall is: "+ str(acc/k))


def Kfold_hybrid(URM_all, k):
    URM_train_list = []
    URM_validation_list = []
    for i in range(k):
        URM_train,URM_validation = split_train_in_two_percentage_global_sample(URM_all,train_percentage=0.85)
        URM_train_list.append(URM_train)
        URM_validation_list.append(URM_validation)
        

    return URM_train_list,URM_validation_list
  
