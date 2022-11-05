import pandas as pd
import warnings
warnings.filterwarnings(action='ignore')
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# 주어진 url 주소를 이용해 house prices 데이터를 가져옵니다.
df = pd.read_csv('house_prices_train.csv')
#소수점 1자리까지 표시
pd.set_option('display.float_format', '{:,.1f}'.format)
df = df[['GrLivArea', 'OverallQual', 'TotRmsAbvGrd','BedroomAbvGr','KitchenAbvGr','SalePrice']]

def PolynomialRegression(degree=3, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), 
                         LinearRegression(**kwargs))

features = ['GrLivArea', 'OverallQual','TotRmsAbvGrd']
target = 'SalePrice'

X = df[features]
y = df[target]

model = PolynomialRegression(degree=4)
model.fit(X, y)



import pickle

with open('model.pkl','wb') as pickle_file:
    pickle.dump(model,pickle_file)
