

# Models Directory

This directory is intended for storing trained machine learning model files used by the AI Mainframe Modernizer application.

## Expected Files
- `fraud_model.pkl`: Serialized model for fraud detection (e.g., a scikit-learn or XGBoost model).
- `personalization_model.pkl`: Serialized model for mobile personalization (e.g., a recommender or classification model).

Sample placeholder files are provided. Replace them with your actual trained models. Ensure the models are compatible with the code in the application.

## Example: Saving a Model
To save a model using `pickle`:
```python
import pickle
with open('fraud_model.pkl', 'wb') as f:
    pickle.dump(your_model, f)
```

## Note
Do not commit sensitive or proprietary models to public repositories.
