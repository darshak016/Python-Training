"""Write a python program using "requests" (3rdparty) and "urllib3" (in-built) module to integrate "PhishTank" service. 
PhishTank is a free online service, which stores information about Phishing URLs.
The Input to the program should be a URL. The output should tell us whether the input url is Phishing URL or not.
Implement a demo function which will utilize the functionality.
"""

import requests


def main():
    try:
        retries = Retry(connect=5, read=2, redirect=5)
        """ Get the URL from user 
        """
        user_url = input("Enter URL to check weather it is phishy or not:  ")
        res = requests.post("https://checkurl.phishtank.com/checkurl/", data = {"url": user_url,"format": "json"})
        
    except Exception as e:
        print(e)
        
    else:
        if res.json()["results"]["in_database"]:
            if res.json()["results"]["valid"]:
                print("{} is a Phishing URL".format(user_url))     
        else:
            print("{} is not a Phishing URL".format(user_url))          

if __name__ == '__main__':
    main()



