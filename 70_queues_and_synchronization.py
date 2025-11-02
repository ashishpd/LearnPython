"""
70_queues_and_synchronization.py

This file demonstrates queues and synchronization primitives.
Covers queue.Queue, threading primitives (Lock, Event, Semaphore).
"""

import queue
import threading

print("QUEUES AND SYNCHRONIZATION")
print("=" * 50)

# QUEUE
print("1. queue.Queue:")

q = queue.Queue()
q.put(1)
q.put(2)
print(f"   Get: {q.get()}\n")

# LOCK
print("2. Lock:")

lock = threading.Lock()
with lock:
    print("   Critical section\n")

# EVENT
print("3. Event:")

event = threading.Event()
# event.set()  # Signal
# event.wait()  # Wait for signal
print("   Event for thread coordination\n")

print("Queues and synchronization demonstration complete!")

