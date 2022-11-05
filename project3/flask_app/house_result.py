import pickle

model = None

with open('model.pkl','rb') as pickle_file:
    model=pickle.load(pickle_file)

X_test = [[4000,5,4]]
y_pred = model.predict(X_test)[0]    

print(f'GrLivArea(지상 생활면적(square feet)가 {X_test[0][0]}이고 평으로 {X_test[0][0]*0.0281}평, OverallQual(전반적인 퀄리티){X_test[0][1]}이고 화장실 제외 방의 갯수 {X_test[0][2]}개 인 경우 주택판매 예측값은 ${abs(round(y_pred,2))}입니다.')