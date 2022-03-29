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

Sample CSV File:
url, is_valid
https://google.com, yes
https://dummy.com, no
"""
from flask import Flask, request, jsonify, make_response
import csv
import json
from simplexml import dumps

app = Flask(__name__)

@app.route('/checkurl/', methods=['POST'])
def check_url():
    url = request.form['url']
    format_type = request.form['format']
    response = {"url": url, "is_valid": "unknown"}
    try:
        file = open('url_data.csv')
        read_csv = csv.reader(file)
        for row in read_csv:
            if row[0] == url:
                response['is_valid'] = row[1]
                break
        if format_type == 'json':
            res =  jsonify(response) 
        else:
            res = make_response(dumps({'root': response}))
        return res    
    except Exception as e:
        print(e)           


if __name__ == "__main__":
    app.run()