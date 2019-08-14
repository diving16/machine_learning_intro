from csv import reader

#自己写一个读取数据的函数
def read_csv(name_file_read):
    file=open(name_file_read,'r')
    every_line_data=reader(file)
    dataset_read=list(every_line_data)
    return dataset_read
    
name_file_read='diabetes.csv'
dataset=read_csv(name_file_read)
print(dataset)