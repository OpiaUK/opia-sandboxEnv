import requests
from itertools import cycle

# List of proxies
proxies = [
    'http://proxy1.com:8080',
    'http://proxy2.com:8080',
    'http://proxy3.com:8080',
    # Add more proxies to the list as needed
]

proxy_pool = cycle(proxies)

url = 'https://dfn9ht-5173.csb.app/'

for i in range(10):  # Replace 10 with the number of requests you want to send
    # Get the next proxy from the pool
    proxy = next(proxy_pool)

    print(f"Request #{i}:")
    print(f"Using proxy: {proxy}")

    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        print(response.text)
    except requests.exceptions.RequestException as e:
        # This will print any connection errors (like 'Max retries exceeded')
        print(e)
