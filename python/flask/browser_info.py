from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index() -> str:
    # Get the User-Agent of the client
    browser_info = request.headers.get('User-Agent')
    return f'<h2>User-Agent: {browser_info}</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)
