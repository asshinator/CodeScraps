"""Mafia site, find all roles."""
import json
import requests
from bs4 import BeautifulSoup

def main():
    f1 = open('C:\Personal\CodeScraps\data\Mafia\Roles.txt', 'w')
    url = "https://epicmafia.com/role/suggested?display=grid&page=1&sortby=votes&type=all"
    response = requests.get(url)
    jsonParser = json.loads(response.text)
    data = jsonParser['data']
    for entry in data:
        print("---------------------",file = f1)
        print(">   %s:%s" % (entry['id'],entry['name']),file = f1 )
        url2 = "https://epicmafia.com/role/"+str(entry['id'])+"/descr"
        response2 = requests.get(url2)
        jsonParser2 = json.loads(response2.text)
        for entry2 in jsonParser2:
            if entry2 != '1' and entry2 != 1:
                print("%s" % (entry2), file=f1)
        print("---------------------",file = f1)
        print("finished %s" % (entry['id']))
    
if __name__ == "__main__":
    if 'isNullRun' in globals():
        True
    else:
        main()