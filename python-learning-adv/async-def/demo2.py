import asyncio
import time

import time

async def make_tea():
    print("Tea Making Started...")
    await asyncio.sleep(3)
    print("Tea making finished...")

async def make_coffee():
    print("Coffee Making Started..")
    await asyncio.sleep(4)
    print("Coffee Making Finished..")

async def make_juice():
    print("Juice making started..")
    await asyncio.sleep(5)
    print("Juice making finished..")

async def main():
    start = time.perf_counter()
    await asyncio.gather(make_tea(),make_coffee(),make_juice())
    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds")

asyncio.run(main())