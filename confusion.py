def confusion_matrix(actual_data,predicted_data):
    unique_class=set(actual_data)
    matrix=[list() for x in range(len(unique_class))]
    for i in range(len(unique_class)):
        matrix[i]=[0 for x in range(len(unique_class))]
#    print(unique_class)
#    print(matrix)
    index_class=dict()
    for i,class_value in enumerate(unique_class):
        index_class[class_value]=i
#    print(index_class)
    for i in range(len(actual_data)):
        col=index_class[actual_data[i]]
        row=index_class[predicted_data[i]]
        matrix[row][col]+=1
#        print(matrix)
#    print(matrix)
    return unique_class,matrix

def pretty_confusion_matrix(unique_class,matrix) :
    print('(Actual)'+' '.join(str(x) for x in unique_class))
    print('(Predicted)-----------------')
    for i,x in enumerate(unique_class):
        print("{}   |   {}".format(x,' '.join(str(x) for x in matrix[i])))
      
    #print(matrix)
    
actual_data=[4,7,0,8,1,2,1,5]
predicted_data=[5,1,0,1,2,1,0,1]

unique_class,matrix=confusion_matrix(actual_data,predicted_data)
pretty_confusion_matrix(unique_class,matrix) 
