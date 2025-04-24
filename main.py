from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    fact_url = "https://uselessfacts.jsph.pl/api/v2/facts/random"

    joke = {"setup": "No joke found.", "punchline": ""}
    fact = {"text": "No fact found."}

    try:
        # Get joke
        joke_response = requests.get(joke_url)
        joke_response.raise_for_status()
        joke = joke_response.json()

        # Get fact
        fact_response = requests.get(fact_url)
        fact_response.raise_for_status()
        fact = fact_response.json()
    except requests.exceptions.RequestException as e:
        print("Perate mano que se jodió algo!")
        print(e)

    return render_template('index.html', joke=joke, fact=fact)
    
if __name__ == '__main__':
    app.run(debug=True)
