import asyncio

"""Asynchronous Programming: 
Asynchrony, in computer programming, it refers to the occurrence of events independent of the main 
program flow and ways to deal with such events.  -- Wikipedia

In other words, Asynchronous Programming means we don't need to wait for some program to complete before others to be 
executed """


async def main():  # <-- coroutine object
    print("Hello, ")
    await foo('Paul')  # use 'await' to execute 'async' function
    print("Nice to meet you")  # wait 'async' function to be executed first before this line.


# what if we want to execute "Nice to meet you" while 'async' function is waiting?
# Well, we use 'task'
async def main2():
    print("Hello, there ")
    task = asyncio.create_task(foo('Lynn'))
    await task
    print("Nice to meet you")


# Note: 'await' has to be inside 'async' function
async def foo(text):
    print(text)
    await asyncio.sleep(3)  # pause for 3 sec.


asyncio.run(main())
print("==========================")
asyncio.run(main2())
