from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Mirelda Diker<h1>"

@app.route('/whoami', methods = ['GET'])
def whoami():
    x = request.args
    return jsonify({'firstname': x.get('firstname',''),
            'lastname':x.get('lastname','')})


@app.route("/alert")
    
app.run(debug=True)