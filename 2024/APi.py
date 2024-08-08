import requests

url1 = "test2"
url2 = "test"
response1 = requests.get(url1)
response2 = requests.get(url2)

if response1.status_code == 200:
    print("Response 1:")
    print(response1.json())  
else:
    print("Error getting response 1:", response1.status_code)

if response2.status_code == 200:
    print("\nResponse 2:")
    print(response2.json())  
else:
    print("Error getting response 2:", response2.status_code)