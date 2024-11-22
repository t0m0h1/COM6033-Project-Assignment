from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model and vectorizer
model = joblib.load('model.pkl')
vectoriser = joblib.load('vectoriser.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')  # Extract text from request
    text_vec = vectoriser.transform([text])  # Transform input text
    prediction = model.predict(text_vec)  # Predict sentiment
    return jsonify({'sentiment': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
