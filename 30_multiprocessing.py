"""
30_multiprocessing.py

This file demonstrates multiprocessing in Python.
Multiprocessing allows true parallelism by using separate processes,
each with its own Python interpreter, bypassing the GIL.
Best for CPU-bound tasks that benefit from multiple CPU cores.
"""

import multiprocessing
import time
import os

# BASIC MULTIPROCESSING
# Create and start a process

def worker_process(name):
    """Simple function that runs in a separate process."""
    print(f"Process {name} (PID: {os.getpid()}) starting")
    time.sleep(1)  # Simulate work
    print(f"Process {name} finished")

# Create processes
process1 = multiprocessing.Process(target=worker_process, args=("Process-1",))
process2 = multiprocessing.Process(target=worker_process, args=("Process-2",))

# Start processes
process1.start()
process2.start()

# Wait for processes to complete
process1.join()
process2.join()

print("All processes completed\n")

# MULTIPROCESSING WITH CLASSES
# Inherit from multiprocessing.Process

class WorkerProcess(multiprocessing.Process):
    """Custom process class."""
    
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        """Method executed when process starts."""
        print(f"{self.name} (PID: {os.getpid()}) started")
        time.sleep(self.delay)
        print(f"{self.name} finished")

# Create and start process objects
p1 = WorkerProcess("Worker-1", 0.5)
p2 = WorkerProcess("Worker-2", 0.8)

p1.start()
p2.start()

p1.join()
p2.join()

print("\nWorker processes completed\n")

# CPU-BOUND TASK EXAMPLE
# Multiprocessing excels at CPU-intensive tasks

def cpu_intensive_task(n):
    """CPU-intensive computation."""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

# Sequential execution
start_time = time.time()
results_seq = [cpu_intensive_task(1000000) for _ in range(4)]
sequential_time = time.time() - start_time

# Parallel execution with multiprocessing
start_time = time.time()
with multiprocessing.Pool(processes=4) as pool:
    results_par = pool.map(cpu_intensive_task, [1000000] * 4)
parallel_time = time.time() - start_time

print(f"Sequential time: {sequential_time:.2f} seconds")
print(f"Parallel time: {parallel_time:.2f} seconds")
print(f"Speedup: {sequential_time / parallel_time:.2f}x\n")

# PROCESS COMMUNICATION - QUEUES
# Share data between processes using queues

def producer(queue, items):
    """Produce items and put them in queue."""
    for item in items:
        print(f"Producing {item}")
        queue.put(item)
        time.sleep(0.1)
    queue.put(None)  # Sentinel value to signal completion

def consumer(queue):
    """Consume items from queue."""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming {item}")
        time.sleep(0.1)

# Create queue and processes
queue = multiprocessing.Queue()
items = [1, 2, 3, 4, 5]

p_producer = multiprocessing.Process(target=producer, args=(queue, items))
p_consumer = multiprocessing.Process(target=consumer, args=(queue,))

p_producer.start()
p_consumer.start()

p_producer.join()
p_consumer.join()

print("\nQueue example completed\n")

# PROCESS COMMUNICATION - PIPES
# Bidirectional communication between two processes

def sender(conn):
    """Send data through pipe."""
    for i in range(5):
        conn.send(f"Message {i}")
        time.sleep(0.1)
    conn.send(None)  # Signal completion
    conn.close()

def receiver(conn):
    """Receive data from pipe."""
    while True:
        msg = conn.recv()
        if msg is None:
            break
        print(f"Received: {msg}")
    conn.close()

# Create pipe
parent_conn, child_conn = multiprocessing.Pipe()

p_sender = multiprocessing.Process(target=sender, args=(child_conn,))
p_receiver = multiprocessing.Process(target=receiver, args=(parent_conn,))

p_sender.start()
p_receiver.start()

p_sender.join()
p_receiver.join()

print("\nPipe example completed\n")

# SHARED MEMORY - Value and Array
# Share data in memory between processes

def increment_shared_value(shared_value, lock):
    """Increment shared value."""
    for _ in range(1000):
        with lock:
            shared_value.value += 1

# Create shared value and lock
shared_value = multiprocessing.Value('i', 0)  # 'i' = integer
lock = multiprocessing.Lock()

# Create multiple processes
processes = [multiprocessing.Process(target=increment_shared_value, args=(shared_value, lock)) for _ in range(4)]

for p in processes:
    p.start()
for p in processes:
    p.join()

print(f"Shared value after increments: {shared_value.value} (should be 4000)")

# Shared array
shared_array = multiprocessing.Array('i', [0, 0, 0, 0])  # Array of 4 integers

def increment_array(shared_array, index, lock):
    """Increment specific array element."""
    for _ in range(1000):
        with lock:
            shared_array[index] += 1

processes = [multiprocessing.Process(target=increment_array, args=(shared_array, i, lock)) for i in range(4)]

for p in processes:
    p.start()
for p in processes:
    p.join()

print(f"Shared array: {list(shared_array)} (each should be 1000)\n")

# PROCESS POOLS - Pool.map()
# Execute function in parallel across multiple processes

def square_number(x):
    """Square a number."""
    return x ** 2

# Use Pool.map() for parallel execution
with multiprocessing.Pool(processes=4) as pool:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    squared = pool.map(square_number, numbers)

print(f"Numbers: {numbers}")
print(f"Squared: {squared}\n")

# PROCESS POOLS - Pool.apply_async()
# Asynchronous execution with callbacks

def process_data(data):
    """Process data and return result."""
    time.sleep(0.1)
    return data * 2

def callback(result):
    """Callback function for async results."""
    print(f"Callback received: {result}")

with multiprocessing.Pool(processes=2) as pool:
    results = []
    for i in range(5):
        result = pool.apply_async(process_data, args=(i,), callback=callback)
        results.append(result)
    
    # Wait for all results
    output = [r.get() for r in results]

print(f"All results: {output}\n")

# MANAGERS - Shared Namespace
# More flexible shared state management

def update_namespace(shared_ns):
    """Update shared namespace."""
    shared_ns.value += 1
    shared_ns.counter += 1

manager = multiprocessing.Manager()
shared_ns = manager.Namespace()
shared_ns.value = 0
shared_ns.counter = 0

processes = [multiprocessing.Process(target=update_namespace, args=(shared_ns,)) for _ in range(5)]

for p in processes:
    p.start()
for p in processes:
    p.join()

print(f"Namespace value: {shared_ns.value}")
print(f"Namespace counter: {shared_ns.counter}\n")

# PROCESS SYNCHRONIZATION - Locks
# Same concept as threading, but for processes

def worker_with_lock(lock, shared_list):
    """Worker that uses lock for synchronization."""
    with lock:
        shared_list.append(os.getpid())
        time.sleep(0.1)

lock = multiprocessing.Lock()
shared_list = manager.list()

processes = [multiprocessing.Process(target=worker_with_lock, args=(lock, shared_list)) for _ in range(5)]

for p in processes:
    p.start()
for p in processes:
    p.join()

print(f"Process IDs added to list: {shared_list}\n")

# GETTING PROCESS INFORMATION

def show_process_info():
    """Display current process information."""
    print(f"Current process PID: {os.getpid()}")
    print(f"Parent process PID: {os.getppid()}")
    print(f"Number of CPU cores: {multiprocessing.cpu_count()}")

show_process_info()

print("\nMultiprocessing demonstration complete!")

