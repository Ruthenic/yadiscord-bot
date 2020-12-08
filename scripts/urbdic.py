import http.client
import json
import re
import os
http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
def urban(term):
    try:
        urbid = os.environ["URBDICID"].replace("\n", "") #try to use heroku config var to get botID
    except: 
        print("Running on local machine. Using text file...") #if config var not found, utilize botid.txt for bot id
        try:
            urbid = open (r'urbdicid.txt', "r")
            urbid = urbid.read().replace("\n", "") #read botID back into the var
        except:
            try:
                urbid = open (r'../urbdicid.txt', "r")
                urbid = urbid.read().replace("\n", "") #read botID back into the var
            except:
                print("Please place valid UrbanDic ID in urbdicid.txt beside main.py")
    conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': urbid,
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    url = "/define?term=" + term
    conn.request("GET", url=url, headers=headers)

    res = conn.getresponse()
    data = res.read()

    jsoning = data.decode("utf-8")
    fulljson = json.loads(jsoning)
    for key, value in fulljson.items():
        zerodic = value[0]
        #print(zerodic["definition"])
    return(zerodic)
