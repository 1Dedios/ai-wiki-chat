# import the response from parser - also import the users prompt
# import requests lib - import requests

sesh = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
search_for = "RESPONSE FROM PARSER"

# b/c it's a search the following parameters must be present: 
PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "utf8": 1,
    "formatversion": 2,
    "srsearch": search_for
}

res = sesh.get(url=URL, params=PARAMS)
data = res.json()

if len(data['query']['search']) > 0:
    # then we've found some hits based on the search
        # this needs to be sent back to llm - w/ users original prompt as context and the data as the resource to use to respond to the user's query
    pass
else: 
    # when there is no result need to send back to llm - and have it answer based on its pretrained data
        # when this happens tell llm to explicitly say in the response that their search didn't find anything in wikipedia
        # however that the llm will respond based on its own data
    pass 





