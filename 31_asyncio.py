"""
31_asyncio.py

This file demonstrates asyncio (asynchronous I/O) in Python.
Asyncio provides single-threaded concurrency for I/O-bound operations.
It uses coroutines and an event loop to handle many operations concurrently.
Perfect for network requests, file I/O, and other I/O-bound tasks.
"""

import asyncio
import time

# BASIC ASYNC/AWAIT
# Define async functions and use await

async def simple_coroutine():
    """A simple coroutine function."""
    print("Coroutine started")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("Coroutine finished")
    return "Result"

# Run a coroutine
async def main():
    result = await simple_coroutine()
    print(f"Got result: {result}\n")

# asyncio.run(main())  # Uncomment to run

# CONCURRENT EXECUTION
# Run multiple coroutines concurrently

async def fetch_data(url_id):
    """Simulate fetching data from a URL."""
    print(f"Fetching data from URL {url_id}...")
    await asyncio.sleep(1)  # Simulate network delay
    print(f"Data from URL {url_id} received")
    return f"Data from {url_id}"

async def concurrent_example():
    """Run multiple fetch operations concurrently."""
    # Sequential (slow)
    start = time.time()
    result1 = await fetch_data(1)
    result2 = await fetch_data(2)
    result3 = await fetch_data(3)
    sequential_time = time.time() - start
    print(f"Sequential time: {sequential_time:.2f} seconds\n")
    
    # Concurrent (fast)
    start = time.time()
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    concurrent_time = time.time() - start
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    print(f"Results: {results}\n")

# asyncio.run(concurrent_example())  # Uncomment to run

# ASYNCIO.GATHER() - Collect Results
# Run multiple coroutines and collect all results

async def process_item(item):
    """Process a single item."""
    await asyncio.sleep(0.1)
    return f"Processed {item}"

async def gather_example():
    """Example of using asyncio.gather()."""
    items = [1, 2, 3, 4, 5]
    results = await asyncio.gather(*[process_item(item) for item in items])
    print("Gather results:")
    for result in results:
        print(f"  {result}")
    print()

# asyncio.run(gather_example())  # Uncomment to run

# ASYNCIO.CREATE_TASK() - Background Tasks
# Create tasks that run concurrently

async def background_task(name, duration):
    """A background task."""
    print(f"Task {name} starting")
    await asyncio.sleep(duration)
    print(f"Task {name} completed")
    return f"Task {name} result"

async def task_example():
    """Example of creating tasks."""
    task1 = asyncio.create_task(background_task("A", 1))
    task2 = asyncio.create_task(background_task("B", 0.5))
    
    # Do other work while tasks run
    await asyncio.sleep(0.2)
    print("Main code continues...")
    
    # Wait for tasks to complete
    result1 = await task1
    result2 = await task2
    print(f"Results: {result1}, {result2}\n")

# asyncio.run(task_example())  # Uncomment to run

# ASYNCIO.SLEEP() vs TIME.SLEEP()
# asyncio.sleep() is non-blocking, time.sleep() blocks

async def non_blocking_example():
    """Demonstrate non-blocking sleep."""
    print("Starting non-blocking operations...")
    start = time.time()
    
    await asyncio.gather(
        asyncio.sleep(1),
        asyncio.sleep(1),
        asyncio.sleep(1)
    )
    
    elapsed = time.time() - start
    print(f"Completed in {elapsed:.2f} seconds (not 3 seconds!)\n")

# asyncio.run(non_blocking_example())  # Uncomment to run

# ASYNCIO.TO_THREAD() - CPU-Bound Tasks
# Run CPU-bound functions in thread pool

def cpu_intensive_task(n):
    """CPU-intensive computation."""
    result = sum(i ** 2 for i in range(n))
    return result

async def thread_pool_example():
    """Run CPU-bound tasks in thread pool."""
    # Run blocking CPU-bound function in thread pool
    result = await asyncio.to_thread(cpu_intensive_task, 1000000)
    print(f"CPU task result: {result}\n")

# asyncio.run(thread_pool_example())  # Uncomment to run

# ASYNCIO.SEMAPHORE - Limit Concurrency
# Control how many coroutines run simultaneously

async def limited_operation(semaphore, operation_id):
    """Operation limited by semaphore."""
    async with semaphore:  # Acquire semaphore
        print(f"Operation {operation_id} starting")
        await asyncio.sleep(1)
        print(f"Operation {operation_id} completed")

async def semaphore_example():
    """Example using semaphore to limit concurrency."""
    semaphore = asyncio.Semaphore(2)  # Allow 2 at a time
    
    # Create 5 operations, but only 2 run concurrently
    await asyncio.gather(*[
        limited_operation(semaphore, i) for i in range(5)
    ])
    print()

# asyncio.run(semaphore_example())  # Uncomment to run

# ASYNCIO.EVENT - Synchronization
# Coordinate between coroutines

async def waiter(event, name):
    """Waiter coroutine."""
    print(f"Waiter {name} waiting...")
    await event.wait()
    print(f"Waiter {name} received signal!")

async def setter(event):
    """Setter coroutine."""
    await asyncio.sleep(2)
    print("Setting event...")
    event.set()

async def event_example():
    """Example using asyncio.Event."""
    event = asyncio.Event()
    
    await asyncio.gather(
        waiter(event, "A"),
        waiter(event, "B"),
        setter(event)
    )
    print()

# asyncio.run(event_example())  # Uncomment to run

# ASYNCIO.QUEUE - Async Queues
# Queue for coroutine communication

async def producer(queue, items):
    """Producer coroutine."""
    for item in items:
        print(f"Producing {item}")
        await queue.put(item)
        await asyncio.sleep(0.1)
    await queue.put(None)  # Sentinel

async def consumer(queue):
    """Consumer coroutine."""
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consuming {item}")
        await asyncio.sleep(0.1)

async def queue_example():
    """Example using asyncio.Queue."""
    queue = asyncio.Queue()
    items = [1, 2, 3, 4, 5]
    
    await asyncio.gather(
        producer(queue, items),
        consumer(queue)
    )
    print()

# asyncio.run(queue_example())  # Uncomment to run

# ASYNCIO.TIMEOUT - Timeout Protection
# Set timeouts for operations

async def slow_operation():
    """A slow operation."""
    await asyncio.sleep(5)
    return "Done"

async def timeout_example():
    """Example of using timeout."""
    try:
        # Operation must complete in 2 seconds
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("Operation timed out!\n")

# asyncio.run(timeout_example())  # Uncomment to run

# ASYNCIO.SHIELD - Prevent Cancellation
# Protect a coroutine from cancellation

async def important_task():
    """An important task that shouldn't be cancelled."""
    try:
        await asyncio.sleep(2)
        print("Important task completed")
    except asyncio.CancelledError:
        print("Important task was cancelled (unexpected!)")

async def shield_example():
    """Example using asyncio.shield()."""
    task = asyncio.create_task(important_task())
    
    # Shield protects the task
    try:
        result = await asyncio.shield(task)
    except asyncio.CancelledError:
        print("Shield was cancelled, but task continues")
    
    await asyncio.sleep(0.5)
    task.cancel()
    await asyncio.sleep(0.5)
    print()

# asyncio.run(shield_example())  # Uncomment to run

# ASYNC GENERATORS
# Create async iterators

async def async_counter(max_count):
    """Async generator."""
    for i in range(max_count):
        await asyncio.sleep(0.1)
        yield i

async def async_generator_example():
    """Example using async generator."""
    async for value in async_counter(5):
        print(f"Generated: {value}")
    print()

# asyncio.run(async_generator_example())  # Uncomment to run

# ASYNC CONTEXT MANAGERS
# Context managers that work with async

class AsyncResource:
    """Async context manager."""
    
    async def __aenter__(self):
        print("Entering async context")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting async context")
        await asyncio.sleep(0.1)
        return False

async def async_context_example():
    """Example using async context manager."""
    async with AsyncResource() as resource:
        print("Inside async context")
        await asyncio.sleep(0.1)
    print()

# asyncio.run(async_context_example())  # Uncomment to run

# COMBINING ASYNC AND SYNC CODE
# When to use asyncio.run()

def synchronous_function():
    """A synchronous function."""
    print("Synchronous function called")
    return "Sync result"

async def mixed_example():
    """Mix async and sync code."""
    # Can call sync functions from async code
    result = synchronous_function()
    print(f"Got: {result}")
    
    # Can't use await in sync code, need asyncio.run()
    await asyncio.sleep(0.1)
    print("Async operation completed\n")

# Run the final example
print("Asyncio demonstration - running main example...")
print("Note: Uncomment individual examples above to see them in action.\n")

# Uncomment to see examples:
# asyncio.run(mixed_example())
print("Asyncio demonstration complete!")

