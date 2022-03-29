"""Write a python program to find Urls from a given string
"""

import re


def main():
    user_input = input("Enter String: ")
    #(https:\/\/|www\.|http:\/\/)[a-zA-Z0-9_]+\.[a-z]{2,3}$
    regex = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    url = re.findall(regex, user_input)
    print(url)
if __name__ == '__main__':
    main()
