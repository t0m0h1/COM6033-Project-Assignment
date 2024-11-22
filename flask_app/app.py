#  *** Cross origin requests must be enabled else the system won't work. ***


from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  

# Load the model and vectoriser to use the model in app
model = joblib.load('/Users/t-hh_macacct/Downloads/COM6033-Project-Assignment/flask_app/models/model.pkl')
vectoriser = joblib.load('/Users/t-hh_macacct/Downloads/COM6033-Project-Assignment/flask_app/models/vectoriser.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = data.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        text_vec = vectoriser.transform([text])
        prediction = model.predict(text_vec)
        return jsonify({'sentiment': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
