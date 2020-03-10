import requests

url = "https://api.airvisual.com/v2/countries?key=5dbfdc43-7b14-4534-acc2-d5dbb0054b78"

payload = {}
files = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
