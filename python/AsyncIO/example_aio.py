#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import asyncio

def main():
    urls = ['www.google.com', 'tw.yahoo.com']
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(get_file(url)) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

async def get_file(url):
    '''
    Suppose this function needs 3 seconds
    '''
    print("Trying to wget url {0}".format(url))
    #await awget.wget(url)
    await asyncio.sleep(3)
    print("Success to wget url {0}".format(url))

if __name__ == '__main__':
    start_time = time.time()
    main()
    # we run 2 funtion, and the total time is near 3 sec
    print(time.time() - start_time)
