# Put your app in here.
"""Simple Calculator with Flask"""

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_calc():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f"<p>{add(a,b)}</p>"
    

@app.route('/sub')
def sub_calc():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f"<p>{sub(a,b)}</p>"

@app.route('/mult')
def mult_calc():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f"<p>{mult(a,b)}</p>"

@app.route('/div')
def div_calc():
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f"<p>{div(a,b)}</p>"

function_map = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<calc>')
def all_calc(calc):
    a = request.args.get('a',type=int)
    b = request.args.get('b',type=int)
    return f"<p>{function_map[calc](a,b)}</p>"