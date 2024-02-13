#creating a chatbot
import json
import tensorflow
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
 
import colorama
colorama.init()
from colorama import Fore,Style,Back


import random
import pickle
with open('intents.json') as file :
     data=json.load(file)


def chat() :
    #load trained model
    model=keras.models.load_model('chat_bot_model')
    
    #load tokenizer pickle
    with open('tokenizer.pickle','rb') as handle:
        tokenizer=pickle.load(handle) 
    
    #load label_encoder pickle
    with open('label_encoder.pickle','rb') as ecn:
        label_encoder=pickle.load(ecn)
    
    #parameter
    max_len=60
    
    
    while True:
        print(Fore.BLUE +"USER ::" + Style.RESET_ALL,end="")
        in1=input()
        if in1.lower() == "quit" :
            break
        in2=tokenizer.texts_to_sequences([in1])
        in3=pad_sequences(in2,truncating="post",maxlen=max_len)
        result=model.predict(in3)
        tag=np.argmax(result)
        tags=label_encoder.inverse_transform([tag])
         
        for i in data['intents']:
            if i["tag"]==tags:
                print(Fore.RED + "CHAT_BOT ::" + Style.RESET_ALL,np.random.choice(i["responses"]))
print(Fore.MAGENTA +"PLEASE ASK YOUR QUERY: ( Type quit to exit)"+Style.RESET_ALL)
chat()