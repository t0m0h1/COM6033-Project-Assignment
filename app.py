from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  

# Load the model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectoriser.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    return jsonify({'sentiment': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
