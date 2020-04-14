from flask import Flask, request
from flask_cors import CORS
from calculate import recommendation
import pandas as pd



DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})


userRating = ''


@app.route("/",methods=["GET"])
def request_handler1():
    df=pd.read_csv("./data/suggestion.csv")
    df1=df.sample(n=24)
    payload=df1.to_json(orient="records")
    return payload

@app.route("/response",methods=["GET"])
def send_response():
    return recommendation(userRating)

@app.route("/send",methods=["POST","GET"])
def request_handler():
    global userRating
    if request.method == "POST":
        userRating = request.json
    return "recieved"



if __name__ == '__main__':
    app.run()
