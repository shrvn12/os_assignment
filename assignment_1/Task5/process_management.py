import os
import time
import multiprocessing as mp

def cpu_worker(nice_value, duration):
    try:
        new_nice = os.nice(nice_value)
    except Exception as e:
        print(f"PID={os.getpid()} | Error setting nice({nice_value}): {e}")
        return

    pid = os.getpid()
    start = time.time()
    count = 0
    while time.time() - start < duration:
        count += 1  

    print(f"PID={pid} | Requested nice={nice_value} | "
          f"Actual nice={new_nice} | Iterations={count}")

if __name__ == "__main__":
    duration = 5  
    nice_values = [0, 5, 10, 15]  
    procs = []

    for n in nice_values:
        p = mp.Process(target=cpu_worker, args=(n, duration))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
