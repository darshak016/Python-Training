"""Create a dummy configuration file (some of extension of such a file can be: .conf, .cfg, .config, .ini) 
in key value pair (refer this document for details). Using ConfigParser library of Python, read the file and write the contents of the old file in a new configuration file. The code should work on both Py2 and Py3. 
Use try-catch blocks wherever necessary.
"""

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


def main():
    config = ConfigParser()
    try:
        # parse existing file
        config.read("sample.ini")
        with open("sample2.ini", "w") as config2:
            config.write(config2)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()