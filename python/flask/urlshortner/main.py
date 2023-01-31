from flask import Flask, request, render_template, redirect, url_for, abort
from werkzeug.wrappers.response import Response
from hashlib import sha3_512
from base64 import b64encode
from typing import List, Optional, Dict, Tuple

app: Flask = Flask(__name__)
dbfile: str = 'urls.dat'
urldb: Dict[str, str] = dict()  # URL DB Cache

def shorten(url: str) -> str:
    '''
    Given a long URL, this can shorten the URL to a very precise and
    short form.
    '''
    # Step 1: Get the SHA3-512 hash of the URL
    hash: bytes = sha3_512(url.encode('utf-8')).digest()

    # Step 2: Get the base64 encoding of the hash
    b64: str = b64encode(hash).decode('ascii')

    # Step 3: Reject all numeric characters at the begining of the
    #         encoding
    starts_with_alpha = b64.lstrip('1234567890+/')

    # Step 4: Return the first 6 characters only
    return starts_with_alpha[:7]

    # TODO: Should we bother to handle collisions?

def bootstrap_urldb(file: str) -> None:
    '''
    Bootstraps the database dictionary from existing file
    '''
    lines: List[str] = list()
    try:
        with open(file, 'r') as db:
            lines = db.readlines()
    except FileNotFoundError:
        return None

    for line in lines:
        if not line: continue   # skip empty lines
        short, long = line.split()
        urldb[short] = long

def lookup_url(file: str, code: str) -> Optional[str]:
    '''
    Lookup the the actual url for the given code in a url database file
    '''
    if code in urldb.keys():
        return urldb[code]

    return None

def record_url(file: str, url: str) -> str:
    '''
    Given a long URL, this computes the short form, records it in the
    database file and finally returns it.  If URL is already present in
    database, it just returns that.
    '''
    code: str = shorten(url)

    if code not in urldb.keys():
        with open(file, 'a') as db:
            db.write(f'{code} {url}\n')       
        urldb[code] = url

    return url_for('redir', code=code)

@app.errorhandler(404)
def url_not_found(_) -> Tuple[str, int]:
    return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        url: str = request.form['url']
        short_url = record_url(dbfile, url)
        return render_template('result.html', base_url=request.base_url.rstrip('/'), url=short_url)
    return render_template('index.html')

@app.route('/<code>')
def redir(code: str) -> Response:
    url: Optional[str] = lookup_url(dbfile, code)
    if url:
        return redirect(url, 302)
    abort(404)

if __name__ == '__main__':
    bootstrap_urldb(dbfile)
    app.run(debug=True)