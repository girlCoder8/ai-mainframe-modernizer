import pickle
import numpy as np

model = pickle.load(open('models/fraud_model.pkl', 'rb'))


def detect_fraud(transaction):
    features = np.array([transaction['amount'], 1 if transaction['type'] == 'debit' else 0])
    risk_score = model.predict_proba([features])[0][1]
    return risk_score > 0.8
