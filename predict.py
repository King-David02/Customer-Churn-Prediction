import pandas as pd
import pickle
from flask import Flask
from flask import request
from flask import jsonify
from Telco_customer_churn import ValueCountTransformer


with open('pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)


app = Flask('churn')
@app.route('/predict', methods= ['POST'])

def predict():

    customer = request.get_json()
    customer_df = pd.DataFrame([customer])

    
    y_pred = pipeline.predict_proba(customer_df)[:, 1]
    churn = y_pred[0] >= 0.5

    result = {'probability': float(y_pred[0]),
        'churn': bool(churn)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)