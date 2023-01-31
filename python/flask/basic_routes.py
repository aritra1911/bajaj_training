from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return '<h2>Hello there I am using Flask""""</h2>'

@app.route('/info')
def info() -> str:
    return '<h2>Flask is easy to learn...</h2>'

@app.route('/user/<name>')
def user(name: str) -> str:
    return f'<h2>This page is for user: {name.upper()}</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)
