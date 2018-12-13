import json
#json_string is json format in one line.
json_string = '{"aaaUser":  {"attributes":  {"name":"admin", "pwd":"cisco123"}}}'
parsed_json = json.loads(json_string)
#print statment is just printing out the key value of name
print(parsed_json["aaaUser"]['attributes']['name'])
print(parsed_json["aaaUser"]['attributes']['pwd'])
