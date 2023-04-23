customer = {
        "gender": "female",
        "seniorcitizen": 0,
        "partner": "yes",
        "dependents": "no",
        "phoneservice": "no",
        "multiplelines": "no_phone_service",
        "internetservice": "dsl",
        "onlinesecurity": "no",
        "onlinebackup": "yes",
        "deviceprotection": "no",
        "techsupport": "no",
        "streamingtv": "no",
        "streamingmovies": "no",
        "contract": "month-to-month",
        "paperlessbilling": "yes",
        "paymentmethod": "electronic_check",
        "tenure": 1,
        "monthlycharges": 29.85,
        "totalcharges": 29.85
    }
import requests
print(requests.post('http://0.0.0.0:9658/predict', json = customer))
print(requests.post('http://0.0.0.0:9658/predict', json = customer).json())