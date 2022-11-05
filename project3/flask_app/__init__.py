from flask import Flask
from flask import Blueprint, render_template, request
import pickle
import pandas as pd

# Flask factory
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return render_template('main.html')
    
    @app.route('/search')
    def search():
        return render_template('search.html')

    @app.route('/result', methods = ['POST'])
    def result():
        column_list=['GrLivArea', 'OverallQual', 'TotRmsAbvGrd']

        a = request.form.get('GrLivArea')
        b = request.form.get('OverallQual')
        c = request.form.get('TotRmsAbvGrd')
     
   
      
        
        data = [int(a),int(b),int(c)]
        X_test = pd.DataFrame([data], columns = column_list)

        with open('model.pkl', 'rb') as pickle_file:
            model = pickle.load(pickle_file)
            y_pred = model.predict(X_test)[0]
            re = round(abs(y_pred),2)
          

        return render_template('result.html', result_ = re)
    
    return app




if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


