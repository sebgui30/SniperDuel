import json

with open('followers_1.json', 'r') as followers_file:
    parsed_json = json.load(followers_file)

print(parsed_json)

try:
    followers_list = parsed_json['relationships_followers']
except KeyError:
    print("Error: Could not find followers. Is it the right JSON?")

for item in followers_list:
    username = item['string_list_data'][0]['value']
    print(f"Found follower: {username}")