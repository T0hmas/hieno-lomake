from flask import Flask, render_template, request
from wsgiref.simple_server import make_server


app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    return render_template('vastaus.html', nimi=request.args['nimi'])

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever() 

