from flask import Flask, jsonify, render_template, redirect, url_for
import requests
import random

app = Flask(__name__)

CHUCK_NORRIS_API_URL = "https://api.chucknorris.io/jokes/random"

@app.route('/', methods=['GET'])
def index():
    """
    Endpoint para obter uma piada aleatória do Chuck Norris.
    """
    joke = get_random_joke()
    return render_template('index.html', joke=joke)

@app.route('/next_joke')
def next_joke():
    """
    Endpoint para obter ua nova piada e redicionar para a pagina
    """

    joke = get_random_joke()
    return jsonify(joke)

def get_random_joke():
    """
    Obtem uma piada aleatoria do Chuck Norris API
    """

    try:
        response = requests.get(CHUCK_NORRIS_API_URL)
        response.raise_for_status()
        joke_data = response.json()
        return joke_data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
if __name__ == '__main__':
    app.run(debug=True)
