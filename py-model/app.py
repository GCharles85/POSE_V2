from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLALCHEMY
import os
import pymodel

app = Flask(__name__)

CORS(app)  # Optionally configure CORS for all routes

#Configure SQLAlchemy to use a SQLite or another db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diagnostics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize SQLAlchemy with the Flask app
db = SQLALCHEMY(app)

#Define the Diagnostic class
class Diagnostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    icon = db.Column(db.String(100), nullable=True)

# After request handler to manually add CORS headers if needed
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

# Helper function to add a new diagnostic to the database
def add_diagnostic_to_db(title, description, cost, icon=None):
    try:
        new_diagnostic = Diagnostic(
            title=title,
            description=description,
            cost=cost,
            icon=icon
        )
        db.session.add(new_diagnostic)
        db.session.commit()
        return new_diagnostic
    except Exception as e:
        return {"error": str(e)}

# AI Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request body
        inputData = request.get_json()

        # Use AI model's predict function to generate predictions
        ai_prediction = pymodel.predict(inputData)

        # Extract details from the AI prediction
        title = ai_prediction.get('title', 'AI Generated Diagnostic')
        description = ai_prediction.get('description', 'AI predicted description')
        cost = ai_prediction.get('cost', 0.0)
        icon = ai_prediction.get('icon', None)

        # Add the new diagnostic to the database
        new_diagnostic = add_diagnostic_to_db(title, description, cost, icon)

        # Return the desired fields in a KVP structure
        return jsonify({
            'id': new_diagnostic.id,
            'title': new_diagnostic.title,
            'description': new_diagnostic.description,
            'cost': new_diagnostic.cost,
            'icon': new_diagnostic.icon
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/diagnostics', methods=['GET'])
def get_diagnostics():
    diagnostics = Diagnostic.query.all()
    diagnostics_list = [
        {
            'id': diagnostic.id,
            'title': diagnostic.title,
            'description': diagnostic.description,
            'cost': diagnostic.cost,
            'icon': diagnostic.icon
        } for diagnostic in diagnostics
    ]
    return jsonify(diagnostics_list)

if __name__ == '__main__':
    # Create the database tables if they do not exist
    db.create_all()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)