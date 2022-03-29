"""Write (not print) a sample xml on the console / terminal. You can either read the xml from a file or 
declare the xml in string and then write it on the console (the output should be xml itself). 
(Use either lxml or xml library). The content should be written in Py2 and Py3.
"""
from xml.dom.minidom import parse
import sys

def main():
    try:
        xml_file = parse("sample.xml")
    except Exception as e:
        print(e)
    else:
        file_xml = xml_file.toprettyxml()
        print(file_xml)   

if __name__ == "__main__":
    main()