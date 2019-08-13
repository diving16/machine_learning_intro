import pandas as pd
import tushare as ts
import math
import numpy as np
from sklearn import preprocessing,svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate, train_test_split

df=ts.get_hist_data('000001')
df=df[['open','high','close','low','volume']]
df['High_low_pct']=(df['high']-df['low'])/df['low']*100
df['Change_pct']=(df['close']-df['open'])/df['open']*100

df=df[['close','High_low_pct','Change_pct','volume']]

pd.set_option('display.max_row',100)
pd.set_option('display.max_columns',100)

#print(df.head())

future_value='close'
df.fillna(value=-99999,inplace=True)
how_far_forecast=int(math.ceil(0.01*len(df)))
#print(how_far_forecast)

df['label']=df[future_value].shift(-how_far_forecast)
df.dropna(inplace=True)
print(df.head(15))

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
y = np.array(df['label'])

X_Recent_Real_Data=X[-how_far_forecast:]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)

#black_box = LinearRegression()
black_box = svm.SVR()
black_box.fit(X_train,y_train)

forecast_set=black_box.predict(X_Recent_Real_Data)
print(forecast_set)


#accuracy=black_box.score(X_test,y_test)


print(accuracy)







