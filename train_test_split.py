from random import seed
from random import randrange

def train_test_split(dataset,train=0.6):
    train_box=list()
    train_size=train*len(dataset)
    dataset_copy=list(dataset)
    
    while len(train_box)<train_size:
        random_choose_element=randrange(len(dataset_copy))
        train_box.append(dataset_copy.pop(random_choose_element))
    return train_box,dataset_copy

#seed固定时random数就固定了
#思考这个问题，会发现每次抽取都是靠运气的，而且存在magic number切分的比例是人工指定的，难道只能通过手动抽取很多次？
#因此，简单的切分是存在问题的。
seed(1)

dataset1=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]] 

train,test=train_test_split(dataset1)

print(train)
print(test)