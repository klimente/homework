# from threading import Thread
# import time
#
# def hello(name,interval):
#     while True:
#         print(f"Hello {name}")
#         time.sleep(interval)
#
# t1 = Thread(target=hello,args=("Kiril",2))
# t2 = Thread(target=hello,args=("Andrey",3))

# import time
# def hello(name,seconds):
#     while True:
#         print(f"Hello {name}")
#         initial = time.time()
#         while time.time() - initial < seconds:
#             print(".",end='')
#             yield
#
# loop = zip(hello("kieil",2),hello('artem',3))
# while True:
#     next(loop)
# import time
#
# def sleep(seconds):
#     initital = time.time()
#     while time.time() - initital < seconds:
#         yield
#
# def hello(name,seconds):
#     while True:
#         print(f"{name}")
#         yield from sleep(seconds)
#
# loop = zip(hello("Andrey",2),hello("Anton",3))
#
# while True:
#     next(loop)

# import asyncio
#
# def hello(name,seconds): #async def <-> def
#     while True:
#         print(f"Hello {name}")
#         yield from asyncio.sleep(seconds) #await <-> yield from
#
# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(hello("Kirill",2)),
#     asyncio.ensure_future(hello("Andrey",3)),
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
