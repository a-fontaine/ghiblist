import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://ghibliapi.herokuapp.com/films/').content
    films = json.loads(response)
    return render_template('index.html', films=films)

if __name__ == '__main__':
    app.run(debug=False)
