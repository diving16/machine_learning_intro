
from csv import reader

#自己写一个读取数据的函数
#数据如果有缺失，先判断再放入

def read_csv(name_file_read):
    dataset=[]
    with open(name_file_read,'r') as file:
        csv_reader=reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
            
    return dataset
# =============================================================================
#     file=open(name_file_read,'r')
#     every_line_data=reader(file)
#     dataset_read=list(every_line_data)
#     return dataset_read
#    
# =============================================================================

#直接传入会发现是''字符串类型，所以需要把字符串转化为float
#想法是每一行一行读取，再一列一列转换，所以参数需要column
def convert_string2float(dataset,column):
    dataset=dataset[1:]
    for row in dataset:
        #Tip：把可能出现的空格去掉
        row[column]=float(row[column].strip())
    
    
    
#调用自己的函数读取数据
name_file_read='diabetes.csv'
dataset=read_csv(name_file_read)
#print(dataset)

for i in range(len(dataset[0])):
    convert_string2float(dataset,i)
    
print(dataset)



