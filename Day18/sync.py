"""Download any n number of images from the site 
(You can use any image site for example:- https://www.gunnerkrigg.com/comics/00000001.jpg)

a) Write Synchronous version with requests lib
"""

import requests
import time

def download_image(n):
    """This function will get image from given URL
    and store in local machine
    Args:
        n (_int_): number of requests
    """
    url = "https://www.gunnerkrigg.com/comics/0000000" + str(n) + ".jpg"
    s = requests.session()
    res = s.get(url)
    
    if res.status_code == 200:
        with open("images/"+ str(n) + ".jpg","wb") as file:
            file.write(res.content)

if __name__ == "__main__":
    starttime = time.time()
    for i in range(1,6):
        download_image(i)
    print("Taken time is {}".format(time.time()-starttime))    