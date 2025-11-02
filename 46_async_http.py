"""
46_async_http.py

This file demonstrates asynchronous HTTP requests in Python.
Covers aiohttp for async HTTP client operations.
Note: Requires 'pip install aiohttp'
"""

import asyncio

print("ASYNCHRONOUS HTTP IN PYTHON")
print("=" * 50)

try:
    import aiohttp
    
    # ASYNC GET REQUEST
    print("1. Basic Async GET Request:")
    
    async def fetch_url(session, url):
        """Fetch URL asynchronously."""
        async with session.get(url) as response:
            return await response.json()
    
    async def basic_example():
        """Basic async HTTP example."""
        async with aiohttp.ClientSession() as session:
            result = await fetch_url(session, "https://httpbin.org/get")
            print(f"   Status: {result.get('url', 'N/A')}\n")
    
    # asyncio.run(basic_example())  # Uncomment to run
    
    # CONCURRENT REQUESTS
    print("2. Concurrent Requests:")
    
    async def fetch_multiple():
        """Fetch multiple URLs concurrently."""
        urls = [
            "https://httpbin.org/delay/1",
            "https://httpbin.org/delay/1",
            "https://httpbin.org/delay/1"
        ]
        
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
            return results
    
    # Time comparison
    async def compare_times():
        """Compare sequential vs concurrent."""
        import time
        
        # Sequential
        start = time.time()
        async with aiohttp.ClientSession() as session:
            for url in ["https://httpbin.org/delay/1"] * 3:
                await session.get(url)
        sequential_time = time.time() - start
        
        # Concurrent
        start = time.time()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[
                session.get("https://httpbin.org/delay/1") for _ in range(3)
            ])
        concurrent_time = time.time() - start
        
        print(f"   Sequential: {sequential_time:.2f}s")
        print(f"   Concurrent: {concurrent_time:.2f}s")
        print(f"   Speedup: {sequential_time/concurrent_time:.2f}x\n")
    
    # asyncio.run(compare_times())  # Uncomment to run
    
    # ASYNC POST REQUEST
    print("3. Async POST Request:")
    
    async def post_example():
        """Example of async POST."""
        data = {"name": "Alice", "age": 30}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://httpbin.org/post",
                json=data
            ) as response:
                result = await response.json()
                return result
    
    # asyncio.run(post_example())  # Uncomment to run
    
    # ERROR HANDLING
    print("4. Error Handling:")
    
    async def safe_fetch(session, url):
        """Safe fetch with error handling."""
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            return {"error": f"Client error: {e}"}
        except asyncio.TimeoutError:
            return {"error": "Timeout"}
    
    # SESSION CONFIGURATION
    print("5. Session Configuration:")
    
    async def configured_session():
        """Example with configured session."""
        timeout = aiohttp.ClientTimeout(total=10)
        headers = {"User-Agent": "MyApp/1.0"}
        
        async with aiohttp.ClientSession(
            timeout=timeout,
            headers=headers
        ) as session:
            # Use session
            pass
    
    # AUTHENTICATION
    print("6. Authentication:")
    
    from aiohttp import BasicAuth
    
    async def auth_example():
        """Example with authentication."""
        auth = BasicAuth("user", "pass")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://httpbin.org/basic-auth/user/pass",
                auth=auth
            ) as response:
                return await response.json()
    
    # CONCURRENT LIMITS
    print("7. Limiting Concurrency:")
    
    async def limited_fetch(urls, max_concurrent=3):
        """Fetch URLs with concurrency limit."""
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def fetch_with_limit(session, url):
            async with semaphore:
                async with session.get(url) as response:
                    return await response.json()
        
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_with_limit(session, url) for url in urls]
            return await asyncio.gather(*tasks)
    
    # STREAMING RESPONSES
    print("8. Streaming Responses:")
    
    async def stream_example():
        """Example of streaming response."""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://httpbin.org/stream/10") as response:
                async for line in response.content:
                    # Process line
                    pass
    
    # COOKIES AND SESSION
    print("9. Cookies and Session:")
    
    async def cookie_example():
        """Example with cookies."""
        async with aiohttp.ClientSession() as session:
            # Set cookie
            async with session.get("https://httpbin.org/cookies/set?name=value") as response:
                cookies = session.cookie_jar
                # Cookies are automatically managed
    
    print()
    
except ImportError:
    print("1. Install aiohttp:")
    print("   pip install aiohttp\n")
    
    print("2. Basic Usage:")
    print("   import aiohttp")
    print("   import asyncio")
    print()
    print("   async def main():")
    print("       async with aiohttp.ClientSession() as session:")
    print("           async with session.get('https://api.example.com') as response:")
    print("               data = await response.json()")
    print()
    print("   asyncio.run(main())\n")
    
    print("3. Concurrent Requests:")
    print("   async def fetch_all():")
    print("       async with aiohttp.ClientSession() as session:")
    print("           tasks = [session.get(url) for url in urls]")
    print("           responses = await asyncio.gather(*tasks)")
    print()
    print("   asyncio.run(fetch_all())\n")
    
    print("4. Key Features:")
    print("   - Async/await syntax")
    print("   - Concurrent requests")
    print("   - Streaming support")
    print("   - Automatic connection pooling")
    print("   - Cookie management")
    print("   - Timeout control")
    print()

print("Async HTTP demonstration complete!")
print("\nComparison with requests:")
print("  - requests: Synchronous, simpler, blocking")
print("  - aiohttp: Asynchronous, faster for I/O-bound, non-blocking")
print("\nUse aiohttp when:")
print("  - Making many concurrent requests")
print("  - I/O-bound operations")
print("  - Building async web applications")
print("  - Need high throughput")

