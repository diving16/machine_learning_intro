#自己写函数找到最大值最小值
from math import sqrt
import diabetes_test

#dataset=[[1,2,3],[3,4,9],[7,8,8],[5,6,4]]

# =============================================================================
# def find_max_min():
#     max_min=[]
#     for i in range(len(dataset[0])):
#         col_value=[row[i] for row in dataset]
# 
# =============================================================================
# =============================================================================
# 
# def find_max_min(dataset):
#     max_min=list()
#     for i in range(len(dataset[0])):
#         col_values=[row[i] for row in dataset]
#         value_max=max(col_values)
#         value_min=min(col_values)
#         max_min.append([value_max,value_min])
#     return max_min
# 
# max_min=find_max_min(dataset)
# #print(max_min)
# =============================================================================
        
    
# =============================================================================
# #自己写的
# def find_max_min(dataset):
#     max_data=[]
#     min_data=[]
#     values=[]
#     for row in dataset:
#         for i in range(len(row)):
#             values.append(row[i])
#             max_data.append(max(values))
#             min_data.append(min(values))
#          
#     return max_data,min_data
# 
# print(find_max_min(dataset))
# 
# =============================================================================

# =============================================================================
# #不是函数里面调用函数，而是函数里面直接传入得到的函数值
# def max_min_normalization(dataset,max_min):
#     for row in dataset:
#         for i in range(len(dataset[0])):
#             row[i]=(row[i]-max_min[i][1])/(max_min[i][0]-max_min[i][1])
#             
#     
# max_min_normalization(dataset,max_min)
# print(dataset)
# 
# =============================================================================

#平均数函数实现
#目前一般的想法是先在函数里给一个空列表，然后进行操作，再把操作后的数据放在列表里
def find_mean(dataset):
    means=list()
    for i in range(len(dataset[0])):
        col_values=[row[i] for row in dataset]
        mean=sum(col_values)/float(len(dataset))
        means.append(mean)
    return means

#dataset_mean=find_mean(dataset)
#
#print(dataset_mean)


#占位小技巧精简代码
#a=[888 for i in range(len(dataset[0]))]

#平均数函数实现,使用占位小技巧精简代码
#目前一般的想法是先在函数里给一个空列表，然后进行操作，再把操作后的数据放在列表里。
#相当于find_mean是空盒子放东西，find_mean_2是放了东西再扔掉
def find_mean_2(dataset):
    means=[888 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        col_values=[row[i] for row in dataset]
        means[i]=sum(col_values)/float(len(dataset))
    return means

#dataset_mean_2=find_mean_2(dataset)

#print(dataset_mean_2)

#计算标准差
def calculate_stddev(dataset,means):
    stddevs=['sit' for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        variance=[pow(row[i]-means[i],2) for row in dataset]
        stddevs[i]=sum(variance)
    stddevs=[sqrt(element/float(len(dataset)-1)) for element in stddevs]
    return stddevs

#print(calculate_stddev(dataset,dataset_mean_2))

#把未知变成已知是一种好思路
#means_list=find_mean_2(dataset)
#stddevs_list=calculate_stddev(dataset,means_list)
#print(dataset)
#print(means_list)
#print(stddevs_list)


def standerdization_data(dataset,means_list,stddevs_list):
    for row in dataset:
        for i in range(len(dataset[0])):
            row[i]=(row[i]-means_list[i])/stddevs_list[i]
    
#standerdization_data(dataset,means_list,stddevs_list)

#print(dataset)

#对diabetes.csv文件操作特征缩放
        

dataset=diabetes_test.read_csv('diabetes.csv')
#print(dataset)

for i in range(len(dataset[0])):
    diabetes_test.convert_string2float(dataset,i)
dataset=dataset[1:]    
#print(dataset)

means_list=find_mean(dataset)
stddevs_list=calculate_stddev(dataset,means_list)
standerdization_data(dataset,means_list,stddevs_list)
print(dataset)
    
    

