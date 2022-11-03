from flask import Flask

# 학습한 모델 파일을 부르기

# Flask Server 를 구현
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
