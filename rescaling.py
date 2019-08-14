#自己写函数找到最大值最小值

dataset=[[1,2],[3,4]]

# =============================================================================
# def find_max_min():
#     max_min=[]
#     for i in range(len(dataset[0])):
#         col_value=[row[i] for row in dataset]
# 
# =============================================================================

def find_max_min(dataset):
    max_min=list()
    for i in range(len(dataset[0])):
        col_values=[row[i] for row in dataset]
        value_max=max(col_values)
        value_min=min(col_values)
        max_min.append([value_max,value_min])
    return max_min

max_min=find_max_min(dataset)
print(max_min)
        
    
# =============================================================================
# #自己写的
# def find_max_min(dataset):
#     max_data=[]
#     min_data=[]
#     values=[]
#     for row in dataset:
#         for i in range(len(row)):
#             values.append(row[i])
#     max_data.append(max(values))
#     min_data.append(min(values))
#          
#     return max_data,min_data
# 
# print(find_max_min(dataset))
# 
# =============================================================================
