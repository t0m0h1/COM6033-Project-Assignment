#  *** Cross origin requests must be enabled else the system won't work. ***


from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  

# Load the model and vectoriser to use the model in app
model = joblib.load('model.pkl')
vectoriser = joblib.load('vectoriser.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    text_vec = vectoriser.transform([text])
    prediction = model.predict(text_vec)
    return jsonify({'sentiment': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)