#Calculate accuracy of prediction

def calculation_accuracy(actual_data,predict_data):
    correct_num=0
    for i in range(len(actual_data)):
        if actual_data[i] == predict_data[i]:
            correct_num+=1
        return correct_num/float(len(actual_data))
    
    
actual_data=[0,0,0,0,0,1,1,1,1,1]
predict_data=[0,0,0,1,0,1,1,0,1,0]

accuracy= calculation_accuracy(actual_data,predict_data)
print(accuracy)
