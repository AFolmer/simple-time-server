import time

from flask import Flask


app = Flask(__name__)


@app.route('/<time>/')
def get_time():
    current_time = int(time.time())
    return f'The current Epoch time is: {current_time}'


if __name__ == "__main__":
    app.run(debug=True)
