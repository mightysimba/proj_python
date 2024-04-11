import json
from urllib import parse, request
url = "http://api.giphy.com/v1/gifs/search"
params = parse.urlencode({
  "q": input("Enter your keyword:"),
  "api_key": "EtLMRzfmAfd8YrhD938TrpnjXHP3QE4B",
  "limit": "1"
})
full_url = "".join((url, "?", params))
with request.urlopen(full_url) as response:
    data = json.loads(response.read())
for gif in data['data']:
    print(gif['url'])
