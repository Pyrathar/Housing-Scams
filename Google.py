import json
import requests

#Experimental filters by .com so that domains like .dk .pt might reveal
def filtercoms(results):
    link_list = [item["link"] for item in results["items"]]
    for x in link_list:
       if x.endswith(".com"):
           del link_list[x]

#Prints current list
def process_search(results):
    link_list = [item["link"] for item in results["items"]]
    for x in link_list:
        print x

    return link_list

def Search(searchitem):
    cx = "004907426129582277813:ayzzauq827e"
    key = "AIzaSyBhmi4lwBEOzMD9bPNC3ZEnTgy6UAO5ik8"
    url = "https://www.googleapis.com/customsearch/v1"


    parameters = {"q": searchitem,
                  "cx": cx,
                  "key": key,
                  }


    page = requests.request("GET", url, params=parameters)
    results = json.loads(page.text)
    results.keys()
    print results
    maxindex = results["searchInformation"]["totalResults"]
    print maxindex
    currentindex = 0;

    link_list = [item["link"] for item in results["items"]]
    for x in link_list:
        print x



    #Second Research

    while (maxindex>=currentindex):

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
     process_search(results)
     currentindex=currentindex+1



process_search("ninjas")




