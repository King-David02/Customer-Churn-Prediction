import  pandas as pd
import requests

url = "http://localhost:9696/predict"

customer = {
     "gender": "male",
     "seniorcitizen": "0",
     "partner": "no",
     "dependents": "no",
     "tenure": "12",
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
     "paperlessbilling": "no",
     "paymentmethod": "mailed_check",
     "monthlycharges": "2325",
     "totalcharges": "30.3",
}

response = requests.post(url, json=customer).json()
print(response)


if response['churn'] == True:
    print('Send promotion')