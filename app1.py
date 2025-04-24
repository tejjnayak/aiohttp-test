import requests

# Define the URL for the GET request
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Failed to retrieve data. Status code:", response.status_code)

