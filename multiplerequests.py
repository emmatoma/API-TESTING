import concurrent.futures
import requests

def make_api_request(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        return {"error": str(err)}

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

# Number of simultaneous requests
num_requests = 50

# Create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit multiple requests concurrently
    futures = [executor.submit(make_api_request, url) for _ in range(num_requests)]

    # Wait for all requests to complete
    concurrent.futures.wait(futures)

    # Collect results
    results = [future.result() for future in futures]

# Print results
for i, result in enumerate(results, start=1):
    print(f"Request {i}:", result)
