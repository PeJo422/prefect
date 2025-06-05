import requests

url = 'https://naas.isalman.dev/no'

response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        print("Random rejection reason:", data['reason'])
    except ValueError:
        print("Error: Failed to parse JSON.")
else:
    print(f"Error: Received unexpected status code {response.status_code}")
