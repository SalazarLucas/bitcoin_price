from flask import Flask, render_template
from helpers import Client

app = Flask(__name__)
client = Client()


@app.route('/')
def index():
    return render_template('index.html', data=client.get_crypto_data())


@app.route('/<string:cryptocurrency>')
def cryptocurrency(cryptocurrency):
    return render_template(
        'crypto.html',
        currency=cryptocurrency,
        data=client.get_ticker(cryptocurrency)
    )


if __name__ == '__main__':
    app.run(debug=True)
