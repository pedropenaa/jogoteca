from flask import Flask


app = Flask(__name__)



@app.route("/inicio")
def ola():
    return "<h1>Seja Bem Vindo ao Site</h1>"


app.run()
