"""Using urllib.parse, make a URL browser friendly, 
i.e., a blank space should be converted to %20, : should be replaced with %3A. Read the input from command line as an argument. 
Apply validations and then parse the URL. User can pass multiple URLs too. Make your code compatible to accept n number of URLs.
"""
from future.moves.urllib import parse
import sys
import re 

def main():
    regex = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    for url in sys.argv[1:]:
        validation = re.match(regex, url)       
        if validation:
            browser_friendly_url = parse.quote(url)    
            print("browser friendly url is {}".format(browser_friendly_url))
        else:
            print("Please enter valid url")
            
if __name__ == "__main__":
    main()