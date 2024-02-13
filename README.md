# chat-bot-using-deep-learning
Project Description:
The Chat Bot Using Deep Learning project is an intelligent conversational agent built using deep learning techniques. This chatbot is designed to understand and respond to user inputs based on predefined intents. The underlying deep learning model is trained on a dataset containing various user patterns and corresponding responses, allowing the bot to provide meaningful and context-aware replies.

Project Structure:
The project consists of three main components:

intents.json: This JSON file contains predefined intents with associated patterns and responses. It serves as the training data for the deep learning model.

model_training.py: This script includes the code for training the deep learning model. It uses TensorFlow and Keras to create a neural network that can classify user input into different intents. The trained model is then saved for later use.

main.py: The main script for running the chatbot. It loads the trained model, tokenizer, and label encoder from the saved files and uses them to process and respond to user inputs in real-time.

Setup and Usage:
To use the chatbot, follow these steps:

Install Dependencies:

Ensure you have Python installed on your system.
Install required packages using pip install -r requirements.txt.
Training the Model:

Run model_training.py to train the deep learning model. This step generates the chat_bot_model file, tokenizer.pickle, and label_encoder.pickle for later use.
Run the Chatbot:

Execute main.py to start the chatbot.
Input your queries and receive responses from the chatbot.
Exiting the Chatbot:

Type "quit" to exit the chatbot.
Additional Notes
The intent.json file can be customized with new intents, patterns, and responses to enhance the chatbot's capabilities.
Feel free to experiment with the model architecture, hyperparameters, and training data to improve the chatbot's performance.
