"""
29_threading.py

This file demonstrates threading in Python.
Threads allow concurrent execution of code, useful for I/O-bound operations.
Note: Python's Global Interpreter Lock (GIL) limits true parallelism for CPU-bound tasks.
"""

import threading
import time

# BASIC THREADING
# Create and start a thread

def worker_function(name):
    """Simple function that runs in a thread."""
    print(f"Thread {name} starting")
    time.sleep(1)  # Simulate work
    print(f"Thread {name} finished")

# Create threads
thread1 = threading.Thread(target=worker_function, args=("Thread-1",))
thread2 = threading.Thread(target=worker_function, args=("Thread-2",))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads completed\n")

# THREADING WITH CLASSES
# Inherit from threading.Thread

class WorkerThread(threading.Thread):
    """Custom thread class."""
    
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        """Method executed when thread starts."""
        print(f"{self.name} started")
        time.sleep(self.delay)
        print(f"{self.name} finished")

# Create and start thread objects
t1 = WorkerThread("Worker-1", 0.5)
t2 = WorkerThread("Worker-2", 0.8)

t1.start()
t2.start()

t1.join()
t2.join()

print("\nWorker threads completed\n")

# THE GLOBAL INTERPRETER LOCK (GIL)
# Only one thread executes Python bytecode at a time
# This limits CPU-bound parallelism, but threads are still useful for I/O-bound tasks

# Example: I/O-bound task (good for threading)
def download_file(file_name):
    """Simulate downloading a file."""
    print(f"Downloading {file_name}...")
    time.sleep(0.5)  # Simulate network delay
    print(f"{file_name} downloaded")

# Multiple downloads can happen concurrently
files = ["file1.txt", "file2.txt", "file3.txt"]
threads = []

for file in files:
    thread = threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nAll downloads completed\n")

# THREAD SYNCHRONIZATION - LOCKS
# Prevents race conditions when multiple threads access shared data

# Without lock (potential race condition)
counter = 0

def increment_counter():
    """Increment shared counter."""
    global counter
    for _ in range(100000):
        counter += 1

# Run without synchronization (unreliable)
threads = [threading.Thread(target=increment_counter) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter without lock: {counter} (should be 300000)")

# With lock (thread-safe)
counter = 0
lock = threading.Lock()

def increment_counter_safe():
    """Safely increment shared counter using lock."""
    global counter
    for _ in range(100000):
        with lock:  # Acquire lock
            counter += 1
        # Lock automatically released

threads = [threading.Thread(target=increment_counter_safe) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter with lock: {counter} (should be 300000)\n")

# THREAD SYNCHRONIZATION - EVENTS
# Allow threads to wait for signals from other threads

event = threading.Event()

def waiter():
    """Thread that waits for an event."""
    print("Waiter thread waiting...")
    event.wait()  # Wait until event is set
    print("Waiter thread received signal!")

def setter():
    """Thread that sets the event."""
    time.sleep(2)  # Simulate some work
    print("Setting event...")
    event.set()  # Signal waiting threads

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()

time.sleep(3)  # Wait for threads to complete
print("\nEvent example completed\n")

# THREAD SYNCHRONIZATION - SEMAPHORES
# Limit the number of threads accessing a resource

semaphore = threading.Semaphore(2)  # Allow 2 threads at a time

def limited_resource_access(thread_id):
    """Access a limited resource."""
    with semaphore:
        print(f"Thread {thread_id} accessing resource")
        time.sleep(1)
        print(f"Thread {thread_id} releasing resource")

# 5 threads, but only 2 can access resource at once
threads = [threading.Thread(target=limited_resource_access, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("\nSemaphore example completed\n")

# THREAD LOCAL DATA
# Each thread has its own copy of data

thread_local = threading.local()

def show_thread_local():
    """Display thread-local data."""
    print(f"Thread {threading.current_thread().name}: {thread_local.data}")

def set_thread_local(value):
    """Set thread-local data."""
    thread_local.data = value
    show_thread_local()

# Each thread has independent data
threading.Thread(target=set_thread_local, args=("Thread-A data",), name="Thread-A").start()
threading.Thread(target=set_thread_local, args=("Thread-B data",), name="Thread-B").start()

time.sleep(0.5)
print("\nThread-local example completed\n")

# DAEMON THREADS
# Threads that terminate when main program exits

def daemon_worker():
    """Daemon thread that runs in background."""
    while True:
        print("Daemon thread running...")
        time.sleep(1)

daemon_thread = threading.Thread(target=daemon_worker, daemon=True)
daemon_thread.start()

time.sleep(2)
print("Main program exiting (daemon thread will terminate)\n")

# THREAD POOLS - ThreadPoolExecutor
# Better way to manage multiple threads

from concurrent.futures import ThreadPoolExecutor

def process_item(item):
    """Process a single item."""
    time.sleep(0.1)
    return f"Processed {item}"

# Use ThreadPoolExecutor for better thread management
with ThreadPoolExecutor(max_workers=3) as executor:
    items = [1, 2, 3, 4, 5]
    results = list(executor.map(process_item, items))

print("ThreadPoolExecutor results:")
for result in results:
    print(f"  {result}")

print("\nThreading demonstration complete!")

