"""Create a simple API Web Server (using flask) similar to PhishTank API service. 
PhishTank is a free online service, which stores information about Phishing URLs.
It should have one POST endpoint named "checkurl" which accepts the following Request Body Parameters 
and returns the response with following Response Fields. 
             Implement a demo function which will utilize the functionality

Request Body Parameter:
- url: encoded url
- format: “json” | “xml”

Response Fields:
- url: URL passed in input
- is_valid: yes | no | unknown

Server will have one static hard-coded csv file with two columns "url" and "is_valid". 
For each request, check if csv file contains entry for that url, 
if yes then return is_valid field accordingly else return is_valid as unknown.
"""

import requests


def main():
    try:
        user_url = input("Enter URL to check weather it is phishy or not:  ")
        user_format = input("Enter format (json or XML): ")
        res = requests.post("http://127.0.0.1:5000/checkurl/", data = {"url": user_url,"format": user_format})
        
    except Exception as e:
        print(e)
        
    else:
        print()
        if res.json()["url"]:
            if res.json()["is_valid"] == 'no':
                print("{} is a Phishing URL".format(user_url))  
            elif res.json()["is_valid"] == 'unknown':
                print("{} is unknown URL".format(user_url))   
            else:
                print("{} is not a Phishing URL".format(user_url))

            
            
if __name__ == '__main__':
    main()



