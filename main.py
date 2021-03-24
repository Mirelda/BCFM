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


@app.route("/alert", methods = ['POST'])
def alert():
    if request.method == 'POST' :
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        return jsonify({'firstname': x.get('firstname','Mirelda'),
            'lastname':x.get('lastname','Diker')})
    else:
        return "Geçersiz"


        

app.run(debug=True)