# python
import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

params = parse.urlencode({
  "q": input("Enter you keyword:"),
  "api_key": "EtLMRzfmAfd8YrhD938TrpnjXHP3QE4B",
  "limit": "2"
})

with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())

print(json.dumps(data, sort_keys=True, indent=4))
