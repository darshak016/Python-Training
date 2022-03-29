"""Make a python script that takes a string as an input, convert characters of a string to bold characters(Unicode bold characters)
If the input is Crest Data Systems, then the output should be 𝐂𝐫𝐞𝐬𝐭 𝐃𝐚𝐭𝐚 𝐒𝐲𝐬𝐭𝐞𝐦𝐬
"""

if __name__ == "__main__":
    string = "Crest Data systems"
    bold_string = []

    for character in string:
        if ord(character) >= ord('a') and ord(character) <= ord('z'):
            bold_string.append(chr(ord(character)-ord('a') + 119834))    
                
        elif ord(character) >= ord('A') and ord(character) <= ord('Z'):
            bold_string.append(chr(ord(character)-ord('A') + 119808)) 
            
        else:
            bold_string.append(character)   

    print("".join(bold_string))