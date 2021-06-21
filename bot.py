from flask import Flask,render_template,request #pip install flask
from chatterbot import ChatBot                  #pip install chatterbot==1.0.1
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__)
#variable name = english_bot, object name = ChatBot, 
#username = Chatterbot, database = storage_adapter
#data will be stored in chatterbot.storage.SQLStorageAdapter
english_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter") 

trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data") #data will store here

@app.route("/")
def index():
    return render_template("index.html") #send context to html

@app.route("/get")
def get_bot_response():
    userText=request.args.get("msg") #get data from input, we write js to index.html
    return str(english_bot.get_response(userText))

if __name__=="__main__":
    app.run(debug=True)