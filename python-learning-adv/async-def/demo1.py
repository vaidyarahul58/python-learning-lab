import time

def make_tea():
    print("Tea Making Started...")
    time.sleep(3)
    print("Tea making finished...")

def make_coffee():
    print("Coffee Making Started..")
    time.sleep(4)
    print("Coffee Making Finished..")

def make_juice():
    print("Juice making started..")
    time.sleep(5)
    print("Juice making finished..")

start = time.perf_counter()
make_tea()
make_coffee()
make_juice()
end = time.perf_counter()
print(f"Total time: {end - start:.2f} seconds")