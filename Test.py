from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar
import time
import json
import requests

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]

def process_search(results):


     link_list = [item["link"] for item in results["items"]]
     for x in link_list:
        print x

     return link_list





cx = "004907426129582277813:ayzzauq827e"
key = "AIzaSyBhmi4lwBEOzMD9bPNC3ZEnTgy6UAO5ik8"
url = "https://www.googleapis.com/customsearch/v1"
searchitem="https://pbs.twimg.com/profile_images/1980294624/DJT_Headshot_V2_400x400.jpg"

parameters = {"q": searchitem,
              "cx": cx,
              "key": key,
              "searchType": "image",
              }

page = requests.request("GET", url, params=parameters)
results = json.loads(page.text)
results.keys()

maxindex = results["searchInformation"]["totalResults"]

currentindex = 0;
if results["searchInformation"]["totalResults"] is 0:
  print "Nothing was found"
if results["searchInformation"]["totalResults"] is not 0:
  process_search(results)

  next_index = results["queries"]["nextPage"][0]["startIndex"]
  search_terms = results["queries"]["nextPage"][0]["searchTerms"]

  url = "https://www.googleapis.com/customsearch/v1"
  parameters = {"q": search_terms,
              "cx": cx,
              "key": key,
              "start": next_index
              }

  page = requests.request("GET", url, params=parameters)
  results = json.loads(page.text)
  print results
  process_search(results)
# Second Research


