from flask import Flask

app = Flask(__name__)


@app.route('/roll/<int:number>')
def roll(number):

    if number > 100 or number < 0:
        return f'{number} exceeds 100!' if number > 100 else f'{number} is less than 0!'

    return f'{number} These number is ok'


@app.route('/')
def index():
    return "hello"


app.run()