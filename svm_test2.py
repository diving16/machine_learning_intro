import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from sklearn import svm

X = np.array([[1,2],
              [3,4],
              [2,2.4],
              [10.3,15.2],
              [13.7,16.4],
              [15.2,17.9]])

#人工贴个标签
y = [0,0,0,1,1,1]

black_box = svm.SVC(kernel='linear',C=1)
black_box.fit(X,y)

#print(black_box.predict([[0.1,0.6]]))

#画出垂直向量,y=ax+b与垂直向量w的关系
w=black_box.coef_[0]
#print(w)

a=-w[0]/w[1]

#intercept是截距
xx=np.linspace(0,18)
yy=a*xx-black_box.intercept_[0]/w[1]

H=plt.plot(xx,yy,'r-',label='not consider weight')

plt.scatter(X[:,0],X[:,1],c=y)
plt.legend()
plt.show()