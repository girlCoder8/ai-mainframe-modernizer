import pickle
import numpy as np

model = pickle.load(open('models/personalization_model.pkl', 'rb'))


def recommend_features(user_profile):
    features = np.array([user_profile['account_balance'], len(user_profile['recent_transactions'])])
    recommendation = model.predict([features])
    return recommendation[0]
