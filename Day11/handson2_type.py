"""Define 3 objects: bytes, str, unicode. Check whether they are the type of basestring or not for Py2 and Py3
"""
def main():
    bytes_obj = b'Bytes Object'
    str_obj =   "str Object"
    unicode_obj = u'Unicode Object'

    try:
        basestring
    except:
        basestring = str 

    if isinstance(bytes_obj, basestring):
        print("Bytes Object{} is instance of basestring class.".format(type(bytes_obj)))
    else:
        print("Bytes object{} is not an instance of basestring class.".format(type(bytes_obj)))   
            
    if isinstance(str_obj, basestring):
        print("String Object {} is instance of basestring class.".format(type(str_obj)))
    else:
        print("String Object {} is not an instance of basestring class.".format(type(str_obj)))

    if isinstance(unicode_obj, basestring):
        print("Unicode Object {} is instance of basestring class.".format(type(unicode_obj)))
    else:
        print("Unicode Object {} is not an instance of basestring class.".format(type(unicode_obj)))        

if __name__ == '__main__':
    main()