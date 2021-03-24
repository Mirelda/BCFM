from flask import Flask, jsonify, request
import requests as req

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Mirelda Diker<h1>"

@app.route('/whoami', methods = ['GET'])
def whoami():
    x = request.args
    return jsonify({'firstname': x.get('firstname','Mirelda'),
            'lastname':x.get('lastname','Diker')})


@app.route("/alert", methods = ['POST'])
def alert():
    if request.method == 'POST' and request.is_json:
        
        url = "https://webhook.site/5f975ca9-efb3-4e3b-9580-cae8b11db28a"
        r = req.post(url, data = request.json)
        return "Success"
    else:
        return "Please enter a Json data"

        

app.run()