from flask import Flask, request
from flask_cors import CORS

import pandas as pd 

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/send",methods=["POST","GET"])
def request_handler():
	if request.method == "POST":
		df=pd.read_csv("./data/suggestion.csv")
		df1=df.sample(n=16)
		payload=df1.to_json(orient="records")
		return payload



if __name__ == '__main__':
    app.run()