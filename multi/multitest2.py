import multiprocessing
import time
import os

def whoami(name):
    print("I am {}, in process {}".format(name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 100000
    for num in range(start, stop):
        print("\tNumber {} of {}. Honk!".format(num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(10)
    p.terminate()
