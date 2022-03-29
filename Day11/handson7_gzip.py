"""Create a gzip of a single simple text file, write some text in it. Open the gzip file programmatically 
and read the contents. The file should be read in Py2 and Py3. Raise FileNotFoundError if the gzip file doesn't exist. 
After reading the file, write the same content in a new gzip file.
"""

import gzip

def main():
    try:
        data = b"This is some content in file."
        with open("handson7.txt.gz","wb") as file:
            file.write(data)
    except FileNotFoundError as e:
        print(e)
    else:
        with open("handson7.txt.gz","rb") as file:
            file_data = file.read()
            print(file_data)
if __name__ == "__main__":
    main()