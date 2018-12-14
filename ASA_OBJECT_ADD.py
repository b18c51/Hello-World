#exported this from postman after sending code to create an object-group
import requests

#the url api from the restful api interface
url = "https://192.168.10.100/api/objects/networkobjects"

payload = "{\n  \"host\": {\n    \"kind\": \"IPv4Address\",\n    \"value\": \"10.1.1.1\"\n  },\n  \"kind\": \"object#NetworkObj\",\n  \"name\": \"ASA_Demo_NObj_1190\",\n  \"objectId\": \"ASA_Demo_NObj_1190\"\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
