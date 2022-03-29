"""Define 3 objects: bytes, str, unicode. Print these 3 objects, write them into a file, write them in the console.
"""

import sys

def main():
    bytes_obj = b'Bytes Object'
    str_obj =   "str Object"
    unicode_obj = u'Unicode Object'
    
    print(bytes_obj,type(bytes_obj))
    print(str_obj,type(str_obj))
    print(unicode_obj,type(unicode_obj))

    try:
        with open("hands-on_6.txt","w") as file:
            file.write(bytes_obj.decode()+"\n")
            file.write(str_obj+"\n")
            file.write(unicode_obj+"\n")
            
    except Exception as e:
        print(e)
    else:
        sys.stdout.write(bytes_obj.decode() +"\n")
        sys.stdout.write(str_obj+"\n")
        sys.stdout.write(unicode_obj+"\n")    

if __name__ == "__main__":
    main()