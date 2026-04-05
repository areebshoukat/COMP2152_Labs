import threading
import time

def simulate_task(name, duration, lock):
    lock.acquire()
    print(f"[START] {name}")
    lock.release()

    time.sleep(duration)

    lock.acquire()
    print(f"[DONE]  {name} ({duration}s)")
    lock.release()

def run_threaded(tasks, lock):
    threads = []

    for name, duration in tasks:
        t = threading.Thread(target=simulate_task, args=(name, duration, lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()