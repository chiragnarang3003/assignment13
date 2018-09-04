#Question1:->Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.
import requests
response1=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(response.status_code)
import json
datata=response.json()
print(type(datata))
print(datata["quoteText"])
