from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Merhaba! Ben Fatıma Betül MEMDUHOĞLU.'

if __name__ == '__main__':
    app.run()