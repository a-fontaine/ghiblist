import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://ghibliapi.herokuapp.com/films/').content
    return response

if __name__ == '__main__':
    app.run(debug=False)
