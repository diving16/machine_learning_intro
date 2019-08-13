import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

numbers = datasets.load_digits()

# =============================================================================
# #feature
# print(numbers.data)
# #label
# print(numbers.target)
# 
# =============================================================================

#调参
black_box=svm.SVC(gamma=0.001,C=100)

#print(len(numbers.data))

X,y = numbers.data[:-1000],numbers.target[:-1000]

black_box.fit(X,y)

print(black_box.predict([numbers.data[-34]]))

plt.imshow(numbers.images[-34])
plt.show()