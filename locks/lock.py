
import threading
import time

lock = threading.Lock()

def try_acquire_twice_lock():
    print(f"{threading.current_thread().name}: Trying to acquire lock (1st time)...")
    lock.acquire() # first lock acquired 

    print(f"{threading.current_thread().name}: Lock acquired (1st time). Now trying again...")

    # this line will cause a deadlock, as the same thraed holds the lock
    lock.acquire() # deadlock


    print("this line won't be reached")
    lock.release()
    lock.release()



# Reentrant lock

rlock = threading.RLock()

def try_acquire_twice_rlock():
    print(f"{threading.current_thread().name}: Trying to acquire RLock (1st time)")
    rlock.acquire() # first acquisition (count = 1)
    print(f"{threading.current_thread().name}: RLock acquired (1st time). Now trying again. ")

    rlock.acquire() # second acquisition by same thrad (count = 2)
    print(f"{threading.current_thread().name}: RLock acquired (2nd time). performing work. ")

    time.sleep(0.1) #Simulate work

    print(f"{threading.current_thread().name}: Releasing RLock (1st release, count = 1)...")
    rlock.release()

    print(f"{threading.current_thread().name}: Releasing RLock (2nd release, count = 0)...")
    rlock.release() 

    print(f"{threading.current_thread().name}: All RLock acquisition released.")



if __name__ == "__main__":
    print("---- example with thrading.Lock (will deadlock) ---")
    t1 = threading.Thread(target=try_acquire_twice_lock, name='LockThread')
    t1.start()
    t1.join(timeout=1)
    if t1.is_alive():
        print(f"{t1.name} is deadlocked")


    t2 = threading.Thread(target=try_acquire_twice_rlock, name='RLockThread')
    t2.start()
    t2.join(timeout=1)
    if not t2.is_alive():
        print(f"{t2.name} finished successfully.")
