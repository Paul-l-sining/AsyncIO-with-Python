import asyncio


async def fetch_data():
    print('Start fetching: ')
    await asyncio.sleep(2)
    print('Done Fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1  # while waiting for task1 to be executed, we start to executed task2
    print(value)
    await task2  # we continue finishing task2

    # Note: if we want to execute sequentially, we do:
    # await fetch_data()
    # await print_numbers()


asyncio.run(main())
