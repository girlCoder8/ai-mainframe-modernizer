
def fetch_mainframe_data(customer_id):
    # Simulated API adapter for mainframe legacy data
    return {
        "customer_id": customer_id,
        "account_balance": 4200.75,
        "recent_transactions": [
            {"amount": 120, "type": "debit"},
            {"amount": 5000, "type": "credit"}
        ]
    }
