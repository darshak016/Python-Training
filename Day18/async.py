"""Download any n number of images from the site 
(You can use any image site for example:- https://www.gunnerkrigg.com/comics/00000001.jpg)

Write a async version for same

"""
import asyncio
import time
import aiohttp
import aiofiles


async def main():
    starttime = time.time()
    url = "https://www.gunnerkrigg.com/comics/0000000{}.jpg"
    async with aiohttp.ClientSession() as session:

        for i in range(1,6):
            res = await session.get(url.format(i))

            async with aiofiles.open("images/" + str(i) + ".jpg", "wb") as f:
                await f.write(await res.read())
    print(time.time()-starttime)   
            
asyncio.run(main())    