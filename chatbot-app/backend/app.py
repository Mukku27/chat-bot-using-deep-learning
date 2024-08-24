from flask import Flask, request, jsonify
import json
import tensorflow as tf
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# Load necessary files and model
with open('intents.json') as file:
    data = json.load(file)

model = keras.models.load_model('chat_bot_model')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

with open('label_encoder.pickle', 'rb') as ecn:
    label_encoder = pickle.load(ecn)

# Parameters
max_len = 60

# Chatbot endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.json.get("message")
    if user_input.lower() == "quit":
        return jsonify({"response": "You have exited the chat."})

    in2 = tokenizer.texts_to_sequences([user_input])
    in3 = pad_sequences(in2, truncating="post", maxlen=max_len)
    result = model.predict(in3)
    tag = np.argmax(result)
    tags = label_encoder.inverse_transform([tag])

    for i in data['intents']:
        if i["tag"] == tags:
            return jsonify({"response": np.random.choice(i["responses"])})

if __name__ == '__main__':
    app.run(debug=True)
