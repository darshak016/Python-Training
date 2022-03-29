"""Download any n number of images from the site 
(You can use any image site for example:- https://www.gunnerkrigg.com/comics/00000001.jpg)

Write multithreading version (with Threading and Threadpoolexecutor both)
"""

import threading
import requests
import time
import concurrent.futures

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
    #Threading
    thread_list = []
    for i in range(1,6):
        t = threading.Thread(target=download_image,args=(i,))
        t.start()
        thread_list.append(t)
    for thread in thread_list:
        thread.join()
    print("Time taken using threading is {}".format(time.time()-starttime))
    
    # ThreadpoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:
        e.map(download_image,range(1,6))
    print("Time taken using ThreadPool is {}".format(time.time()-starttime))    