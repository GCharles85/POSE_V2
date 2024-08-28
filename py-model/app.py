from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)  # Optionally configure CORS for all routes

# After request handler to manually add CORS headers if needed
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Path to the 'wwwroot/data' directory relative to the parent directory of 'py-model'
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    wwwroot_path = os.path.join(parent_dir, 'wwwroot/data')
    
    # Specify the JSON file you want to return
    json_filename = 'updated-diagnostics.json'
    
    try:
        # Return the contents of the JSON file
        return send_from_directory(wwwroot_path, json_filename)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
