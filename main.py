from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Mirelda Diker<h1>"

@app.route('/whoami', methods = ['GET'])
def whoami():
    x = request.args
    return jsonify({'firstname': x.get('firstname','Mirelda'),
            'lastname':x.get('lastname','Diker')})


@app.route("/alert", methods = ['GET','POST'])
def alert():
    return 'JSON Object Example'

app.run(debug=True)