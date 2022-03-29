"""Write a python program to convert XML string to dictionary
"""

import re


def main():
    user_string = input("Enter in XML format: ")
    pattern = r"<(.*)>([^<]+)</\1>"
    ans = re.findall(pattern, user_string)
    print(dict(ans))


if __name__ == "__main__":
    main()
