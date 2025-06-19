from data_connector import get_customer_profile
from mobile_personalization_ai import recommend_features
from fraud_detection_engine import detect_fraud


def handle_user_request(customer_id):
    profile = get_customer_profile(customer_id)
    recommendation = recommend_features(profile)
    fraud_flags = [tx for tx in profile['recent_transactions'] if detect_fraud(tx)]
    return {
        "profile": profile,
        "recommendation": recommendation,
        "fraud_alerts": fraud_flags
    }
