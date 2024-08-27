import json
import random
from sklearn.linear_model import LogisticRegression

# Sample dummy data
training_data = [
    {"input": [0, 0, 1], "output": {"title": "Brakes", "cost": "$500", "description": "Heavy wear on rear passenger side brake pad.", "icon": "fas fa-car"}},
    {"input": [1, 1, 0], "output": {"title": "Software and engine", "cost": "$600", "description": "OBD-II code P0300. Multiple cylinder misfires.", "icon": "fas fa-tools"}},
    {"input": [1, 0, 0], "output": {"title": "Transmission", "cost": "$100", "description": "Defective pressure switch on 4th gear.", "icon": "fas fa-cogs"}},
]

# Extracting features and labels
X = [data['input'] for data in training_data]
y = [data['output'] for data in training_data]

# Dummy model (Logistic Regression for simplicity)
model = LogisticRegression()
model.fit(X, range(len(y)))

# Function to simulate predictions and return JSON
def predict(input_data):
    prediction_index = model.predict([input_data])[0]
    return json.dumps(y[prediction_index])

# Example usage
dummy_input = [1, 0, 0]  # Replace with actual input
result_json = predict(dummy_input)
print(result_json)
