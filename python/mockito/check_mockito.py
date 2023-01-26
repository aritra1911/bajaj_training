import requests
from mockito import when, mock, verifyStubbedInvocationsAreUsed
from mock1 import fetch

def test_fetch():
    url = 'https://www.genunix.com/'
    response = mock({ "text": "Ok" }, spec=requests.Response)
    session = mock(requests.Session)
    when(session).get(url).thenReturn(response)
    when(requests).Session().thenReturn(session)
    r = fetch(url)
    assert r.text == 'Ok'
    verifyStubbedInvocationsAreUsed()

def main() -> None:
    test_fetch()

if __name__ == '__main__':
    main()
