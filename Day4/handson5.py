"""Write a program to handle file open/close and read/write functionality using Exception handling.
"""

def main():
    try:
        file = open("test.txt", 'r+')
    except Exception as e:
        print(e.args)
        
    else:
        try:
            file.write("This is demo text in test file")
            
        except Exception as e:
            print(e.args)
            
        else:
            file.close()
                            

if __name__ == '__main__':
    main()
