"""implement the retry mechanism in the task 1 (PhishTank) with backoff time for the fault tolerance of request.
Use built-in “requests.packages.urllib3.util.retry.Retry”
"""
import urllib3
from urllib3.util.retry import Retry
import json

def main():
    try:
        """ Get the URL from user 
        """
        user_url = input("Enter URL to check weather it is phishy or not:  ")
        
        retries = Retry(total=5,backoff_factor=0.8,redirect=5)
        http = urllib3.PoolManager(retries=retries)
        
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