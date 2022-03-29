"""Write unit tests for the Phishtank exercise form REST API session. Use mocking to mock any API calls that need to be made.
"""

import requests

def check_phishing_url(url):
    """This function check weather url is phishy or not

    Args:
        url ([string]):

    Returns:
        [response]: return response from url
    """
    try:
        data = {"url": url, "format": "json"}
        response = requests.post("https://checkurl.phishtank.com/checkurl/", data = data)
        
    except Exception as e:
        print(e)
        
    else:
        return response.text      