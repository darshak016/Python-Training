"""Given a xml file(sample.xml) print out all the files and folders hierarchically. It should have a proper format 
i.e the files should be clearly visible under the folder so that a user get idea about the folder structure.
        Take the XML filename as an argument. Use OOPS concepts.
        Python script should contain class, and all the required definitions should be defined within that class. 
        Using sample.xml
Sample.xml : smb://10.0.1.22/CrestData/UserData/Milan Parmar/Milan Parmar Python Training files/sample.xml
Sample Output:
	Folder_1
		File_1
		Folder_2
			File_3
		Folder_4
"""

import xml.etree.ElementTree as ET

def get_hierarchy(root,spaces):
    for i in range(len(root)):
        if root[i].tag == "folder":
            print("\t"* spaces, root[i].attrib.get("name"))
            get_hierarchy(root[i], spaces + 1)
        if root[i].tag == "file":
            print("\t"* spaces, root[i].attrib.get("name"))
            
def main():
    try:
        tree = ET.parse("sample.xml")
        root = tree.getroot()
        get_hierarchy(root, 0)
        
    except Exception as e:
        print(e) 

if __name__ == '__main__':
    main()