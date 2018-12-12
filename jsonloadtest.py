#python script for parsing json
import json
json_string = '{"hi": "there"}'
parsed_json = json.loads(json_string)
print(parsed_json['hi'])
