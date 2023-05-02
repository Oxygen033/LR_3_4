from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def solve():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    Discriminant = b**2 - 4*a*c
    if Discriminant < 0:
        Root1 = complex(-b/(2*a), math.sqrt(abs(Discriminant))/(2*a))
        Root2 = complex(-b/(2*a), -math.sqrt(abs(Discriminant))/(2*a))
    else:
        Root1 = (-b + math.sqrt(Discriminant)) / (2*a)
        Root2 = (-b - math.sqrt(Discriminant)) / (2*a)
    return render_template('index.html', root1=Root1, root2=Root2, discriminant=Discriminant)