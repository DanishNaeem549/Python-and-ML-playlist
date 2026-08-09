import threading
import time


def square():
    time.sleep(2)
    for i in range(1,6):
       print(f"square of number: {i*i}")

def cube():
    time.sleep(2)
    for i in range(1,6):
       print(f"cube of number: {i*i*i}")


# creating multiprocess
if __name__ == "__main__":
    
    p1 = threading.Thread(target= square)
    p2 = threading.Thread( target = cube)

    t =time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish= time.time()-t
    print(finish)