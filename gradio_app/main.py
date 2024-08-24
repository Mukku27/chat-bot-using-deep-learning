import json
import tensorflow as tf
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import pickle
import gradio as gr

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

# Chatbot function
def chatbot_response(user_input):
    if user_input.lower() == "quit":
        return "You have exited the chat."

    in2 = tokenizer.texts_to_sequences([user_input])
    in3 = pad_sequences(in2, truncating="post", maxlen=max_len)
    result = model.predict(in3)
    tag = np.argmax(result)
    tags = label_encoder.inverse_transform([tag])

    for i in data['intents']:
        if i["tag"] == tags:
            return np.random.choice(i["responses"])

# Gradio UI
iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="Chatbot Application",
    description="Ask your questions below. Type 'quit' to exit."
)

iface.launch()
