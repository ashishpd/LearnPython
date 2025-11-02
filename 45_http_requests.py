"""
45_http_requests.py

This file demonstrates HTTP requests in Python.
Covers the requests library, REST APIs, authentication, and error handling.
Note: Requires 'pip install requests'
"""

# HTTP REQUESTS WITH REQUESTS LIBRARY
# Simple and elegant HTTP library

print("HTTP REQUESTS IN PYTHON")
print("=" * 50)

try:
    import requests
    
    print("1. Basic GET Request:")
    
    # Simple GET request
    response = requests.get("https://httpbin.org/get")
    print(f"   Status code: {response.status_code}")
    print(f"   Response headers: {dict(list(response.headers.items())[:3])}")
    print(f"   Response JSON: {response.json()}\n")
    
    # GET with parameters
    print("2. GET with Parameters:")
    params = {"key1": "value1", "key2": "value2"}
    response = requests.get("https://httpbin.org/get", params=params)
    print(f"   URL: {response.url}")
    print(f"   Params in response: {response.json()['args']}\n")
    
    # POST Request
    print("3. POST Request:")
    data = {"name": "Alice", "age": 30}
    response = requests.post("https://httpbin.org/post", json=data)
    print(f"   Status: {response.status_code}")
    print(f"   Posted data: {response.json()['json']}\n")
    
    # Request Headers
    print("4. Custom Headers:")
    headers = {"User-Agent": "MyApp/1.0", "Accept": "application/json"}
    response = requests.get("https://httpbin.org/headers", headers=headers)
    print(f"   Sent headers: {response.json()['headers']}\n")
    
    # Error Handling
    print("5. Error Handling:")
    
    def safe_request(url):
        """Make request with error handling."""
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raises HTTPError for bad status
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "Request timeout"}
        except requests.exceptions.HTTPError as e:
            return {"error": f"HTTP error: {e}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Request error: {e}"}
    
    result = safe_request("https://httpbin.org/status/200")
    print(f"   Safe request result: {result}\n")
    
    # Authentication
    print("6. Authentication:")
    
    # Basic Auth
    from requests.auth import HTTPBasicAuth
    response = requests.get(
        "https://httpbin.org/basic-auth/user/pass",
        auth=HTTPBasicAuth("user", "pass")
    )
    print(f"   Basic auth status: {response.status_code}")
    
    # Token Auth
    token = "your-token-here"
    headers = {"Authorization": f"Bearer {token}"}
    # response = requests.get("https://api.example.com/data", headers=headers)
    print("   Token auth: Use Authorization header\n")
    
    # Session for persistent connections
    print("7. Sessions (Persistent Connections):")
    session = requests.Session()
    session.headers.update({"User-Agent": "MyApp/1.0"})
    
    response1 = session.get("https://httpbin.org/get")
    response2 = session.get("https://httpbin.org/get")
    print(f"   Session maintains headers across requests\n")
    
    # File Upload
    print("8. File Upload:")
    # files = {'file': open('example.txt', 'rb')}
    # response = requests.post('https://httpbin.org/post', files=files)
    print("   Use files parameter for multipart/form-data\n")
    
    # Download File
    print("9. Download File:")
    def download_file(url, filename):
        """Download file from URL."""
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        return False
    
    # Example (commented out)
    # download_file("https://example.com/file.pdf", "file.pdf")
    print("   Use stream=True and iter_content() for large files\n")
    
    # Response Objects
    print("10. Response Object Methods:")
    response = requests.get("https://httpbin.org/json")
    print(f"   response.text - Raw text: {len(response.text)} chars")
    print(f"   response.json() - Parsed JSON: {type(response.json())}")
    print(f"   response.content - Raw bytes: {len(response.content)} bytes")
    print(f"   response.status_code - Status: {response.status_code}")
    print(f"   response.headers - Headers: dict with {len(response.headers)} items\n")
    
    # Timeout
    print("11. Timeout:")
    try:
        response = requests.get("https://httpbin.org/delay/1", timeout=0.5)
    except requests.exceptions.Timeout:
        print("   Request timed out (as expected)\n")
    
    # SSL Verification
    print("12. SSL Verification:")
    # Disable SSL verification (not recommended for production)
    # response = requests.get("https://example.com", verify=False)
    print("   Use verify=True (default) for production")
    print("   verify=False only for development/testing\n")
    
except ImportError:
    print("1. Install requests library:")
    print("   pip install requests\n")
    
    print("2. Basic Usage:")
    print("   import requests")
    print("   response = requests.get('https://api.example.com/data')")
    print("   data = response.json()\n")
    
    print("3. Common Methods:")
    print("   - requests.get(url, params={}, headers={})")
    print("   - requests.post(url, json={}, data={})")
    print("   - requests.put(url, json={})")
    print("   - requests.delete(url)")
    print("   - requests.patch(url, json={})\n")
    
    print("4. Response Object:")
    print("   - response.status_code - HTTP status code")
    print("   - response.json() - Parse JSON response")
    print("   - response.text - Response as text")
    print("   - response.headers - Response headers")
    print("   - response.raise_for_status() - Raise on error\n")
    
    print("5. Error Handling:")
    print("   - requests.exceptions.RequestException")
    print("   - requests.exceptions.HTTPError")
    print("   - requests.exceptions.Timeout")
    print("   - requests.exceptions.ConnectionError\n")

print("HTTP requests demonstration complete!")
print("\nBest practices:")
print("  - Always handle exceptions")
print("  - Use timeouts")
print("  - Verify SSL certificates")
print("  - Use sessions for multiple requests")
print("  - Respect rate limits")
print("  - Cache responses when appropriate")

