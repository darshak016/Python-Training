"""Download any n number of images from the site 
(You can use any image site for example:- https://www.gunnerkrigg.com/comics/00000001.jpg)

Write multiprocessing version same

"""

import requests
import time
from concurrent.futures import ProcessPoolExecutor

def download_image(n):
    """This function will get image from given URL
    and store in local machine
    Args:
        n (_int_): number of requests
    """
    url = "https://www.gunnerkrigg.com/comics/0000000" + str(n) + ".jpg"
    res = requests.get(url)
    if res.status_code == 200:
        with open("images/"+ str(n) + ".jpg","wb") as file:
            file.write(res.content)      

if __name__ == "__main__":
    starttime = time.time()
    # ProcesspoolExecutor
    with ProcessPoolExecutor(max_workers=5) as e:
        e.map(download_image,range(1,6))
    print("Time taken using ProcessPool is {}".format(time.time()-starttime))    
        
        