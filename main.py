import time
import gunicorn
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def get_time():
    current_time = int(time.time())
    return f'The current Epoch time is: {current_time}'


if __name__ == "__main__":
    app.run(debug=True)
