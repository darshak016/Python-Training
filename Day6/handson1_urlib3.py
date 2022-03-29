"""Write a python program using "requests" (3rdparty) and "urllib3" (in-built) module to integrate "PhishTank" service. 
PhishTank is a free online service, which stores information about Phishing URLs.
The Input to the program should be a URL. The output should tell us whether the input url is Phishing URL or not.
Implement a demo function which will utilize the functionality.
"""

import urllib3
import json

def main():
    try:
        """ Get the URL from user 
        """
        user_url = input("Enter URL to check weather it is phishy or not:  ")
        http = urllib3.PoolManager()
        res = http.request("POST","https://checkurl.phishtank.com/checkurl/", fields = {"url": user_url,"format": "json"})
    except Exception as e:
        print(e)
    else:
        res = res.data.decode("utf-8")
        res_json = json.loads(res)
        
        if res_json["results"]["in_database"]:
            if res_json["results"]["valid"]:
                print("{} is a Phishing URL".format(user_url))     
        else:
            print("{} is not a Phishing URL".format(user_url))          

if __name__ == '__main__':
    main()