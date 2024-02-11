from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv('.env')

@app.route('/')
def get_env_variable():
    env_variable = os.getenv('MY_ENV_VARIABLE')
    return env_variable

if __name__ == '__main__':
    app.run()
