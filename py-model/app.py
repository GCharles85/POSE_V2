from flask import Flask, request, jsonify
from pymodel import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    input_data = request.json['input']
    result_json = predict(input_data)
    return jsonify(result_json)

if __name__ == '__main__':
    app.run(debug=True)
