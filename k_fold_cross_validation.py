from random import seed
from random import randrange

def k_fold_cross_validation_split(dataset,folds=10):
    basket_splitted_data=list()
    #函数会缺失
    fold_size=int(len(dataset)/folds)
    dataset_copy=list(dataset)
    
    for i in range(folds):
        basket_random_choosen=list()
        while len(basket_random_choosen)<fold_size:
            random_choose_element=randrange(len(dataset_copy))
            basket_random_choosen.append(dataset_copy.pop(
                    random_choose_element))
        basket_splitted_data.append(basket_random_choosen)
    return  basket_splitted_data


seed(1)

dataset1=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]] 

#fold一般会选择5，10
k_folds_split=k_fold_cross_validation_split(dataset1,folds=5)

print(k_folds_split)