########################################################################
# Title Multiprocessing in Python
# Author Sachin Acharya
# Saturday, June 12, 2021
########################################################################
# Methods One | Old way
########################################################################
import time, multiprocessing

def sleep_for(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print("Waking up")
"""
# For some of couple of functions
p1 = multiprocessing.Process(target=sleep_for, args=[1])
p2 = multiprocessing.Process(target=sleep_for, args=[1])

if __name__=='__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()

"""
"""
# For Multiple-Multiple Functions
process = []
for i in range(10):
    p = multiprocessing.Process(target=sleep_for, args=[1])
    if __name__ == "__main__":
        p.start()
        process.append(p)
for p in process:
    p.join()
finish = time.perf_counter()
print('Finished After ', finish)
########################################################################
"""
########################################################################
# Methods Two | New Methods
# async Create Functions
# await wait for task/async function to be completed
# task run without waiting
########################################################################
"""
import asyncio as asc, time as t
async def fetch_data():
    print("Start Fetching")
    # t.sleep(2)
    # It pause program for 2 seconds syncronously
    await asc.sleep(2) # It checks for other async funtion to run
    # If they are wait for more than this, it will continue else other
    # Will continue until another pause
    print("Done Fetching")
    print(time.perf_counter())
    return {"data": "True"}
async def print_data():
    for i in range(10):
        print(i)
        await asc.sleep(0.25)
async def main():
    # Creating task so that it can run without any intruption
    task1 = asc.create_task(fetch_data())
    task2 = asc.create_task(print_data())
    # To get value task must be awaited
    # Here future is created (Wikipedia for more)
    value = await task1
    print(value)
    # Since program is done here it will be terminated if task2 is not awaited
    await task2
asc.run(main())
########################################################################
"""
########################################################################
# Methods Three | Threading
########################################################################
import time
start = time.perf_counter()
def do_something():
    print('Sleeping for 1 second')
    time.sleep(1)
    print('I am wake')
do_something()
finish = time.perf_counter()
print("Finished in {} Sec(s)".format(round(finish, 2)))
########################################################################
