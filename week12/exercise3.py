import re
from flask import Flask, jsonify, abort, request
import exercise1_2 as facade

# Lav en flask server, hvor du åbner minimum 2 endpoints:
# - GET : returner data omkring antallet af crimes i en given periode 
# (giv to datoer med som query-param i URL'en)
# - POST : returner den totale mængde af "burglaries" i januar, men returner kun data, 
# hvis request.body indeholder et json objekt med key-value {"key":"secret"}

app = Flask(__name__)

@app.route('/test')
def index():
    return "Hello, World from flask server!"

@app.route('/crimes', methods=['GET'])
def crimes():
    try:
        startday = request.args.get('start')
        endday = request.args.get('end')
        #return jsonify(startday, endday)
        isNum = re.compile(r'^[0-9]*$')
        if(isNum.match(startday) and isNum.match(endday)):
            res = facade.second(startday, endday)
            return(jsonify(res))
        return jsonify({"msg": "Dates must be numeric"}), 400
    except:
        return jsonify({"msg": "Error"}), 404
#http://127.0.0.1:5000/crimes?start=01&end=02

@app.route('/crimes', methods=['POST'])
def burglaries():
    if (request.json['key'] == 'secret'):
        res = facade.second()
        return jsonify(res)
    return jsonify({'msg': 'Error'}), 404
#{"key": "secret"}
    

if __name__ == '__main__':
    app.run(debug=True)

