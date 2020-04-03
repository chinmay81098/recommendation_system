from flask import Flask, request
from flask_cors import CORS
from calculate import recommendation

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/send",methods=["POST","GET"])
def request_handler():
    if request.method == "POST":
        return recommendation(request.json)




if __name__ == '__main__':
    app.run()