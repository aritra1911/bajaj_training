from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return '<h2>Hello there I am using Flask""""</h2>'

@app.route('/user_latin/<name>')
def user_latin(name: str) -> str:
    username: str = name[:-1] + 'iful' if name[-1] == 'y' else name + 'y'
    return f'<h1>Hi {name}!  Your user latin name is {username}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)
