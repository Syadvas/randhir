import json
from flask import Flask, request

app = Flask(__name__)

def multiplyer(a,c):
    return a*c

@app.route("/result",methods = ['POST'])
def result():
    req = request.get_json(silent=True,force=True)
    """
    {"num1":20,"num2":30}

    """
    a  = req.get("num1")
    b = req.get("num2")
    return str(multiplyer(a,b))

if __name__ == '__main__':
    app.run()