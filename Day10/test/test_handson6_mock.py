"""Write unit tests for the Phishtank exercise form REST API session. Use mocking to mock any API calls that need to be made.
"""

from demo.handson6 import check_phishing_url
import requests_mock

def test_success():
    with requests_mock.Mocker() as m:
        url = "https://amazon.com"
        message = "response from mocking"
        m.post("https://checkurl.phishtank.com/checkurl/", text=message)
        assert check_phishing_url(url) == message