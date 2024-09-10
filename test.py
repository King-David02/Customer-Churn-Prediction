import  pandas as pd
import requests

url = "http://localhost:9696/predict"

customer = {
     "gender": "female",
     "seniorcitizen": "0",
     "partner": "yes",
     "dependents": "no",
     "tenure": "15",
     "phoneservice": "no",
     "multiplelines": "yes",
     "internetservice": "dsl",
     "onlinesecurity": "yes",
     "onlinebackup": "yes",
     "deviceprotection": "no",
     "techsupport": "no",
     "streamingtv": "yes",
     "streamingmovies": "no",
     "contract": "one_year",
     "paperlessbilling": "yes",
     "paymentmethod": "mailed_check",
     "monthlycharges": "2325",
     "totalcharges": "29.85",
}

response = requests.post(url, json=customer).json()
response


if response['churn'] == True:
    print('Send promotion')