import requests

response = requests.get("http://127.0.0.1:8000/weather/sample")
print(response.reason)
print(response.status_code)
print(response.ok)