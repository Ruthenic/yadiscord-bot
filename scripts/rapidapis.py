import http.client
import json
import re
import os
import random
http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
try:
    rapid = os.environ["URBDICID"].replace("\n", "") #try to use heroku config var to get botID
except: 
    print("Running on local machine. Using text file...") #if config var not found, utilize botid.txt for bot id
    try:
        rapid = open (r'rapidapiid.txt', "r")
        rapid = rapid.read().replace("\n", "") #read botID back into the var
    except:
        try:
            rapid = open (r'../rapidapiid.txt', "r")
            rapid = rapid.read().replace("\n", "") #read botID back into the var
        except:
            print("Please place valid RapidAPI ID in rapidapiid.txt")
class urbdic():
    def urban(term, defnum):
        print(defnum)
        if defnum == "":
            defnum = 0
        conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': rapid,
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
        }
        url = "/define?term=" + term
        conn.request("GET", url=url, headers=headers)

        res = conn.getresponse()
        data = res.read()

        jsoning = data.decode("utf-8")
        fulljson = json.loads(jsoning)
        for key, value in fulljson.items():
            zerodic = value[defnum]
        return(zerodic)
    def urbrand():
        conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")
        headers = {
        'x-rapidapi-key': rapid,
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
        }
        os.system('curl https://www.randomlists.com/data/words.json -o out.json')
        randwords = json.load(open("out.json"))
        randnum = random.randrange(0, 2466)
        index = 0
        for i in randwords["data"]:
            index+=1
            if index == randnum:
                term = i
                break
        url = "/define?term=" + term
        conn.request("GET", url=url, headers=headers)
        res = conn.getresponse()
        data = res.read()
        jsoning = data.decode("utf-8")
        fulljson = json.loads(jsoning)
        for key, value in fulljson.items():
            zerodic = value[0]
        zerodic.update({'Word':term})
        return(zerodic)
class covid19():
    def covidcountry(code):
        conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")
        
        headers = {
            'x-rapidapi-key': rapid,
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }
        
        conn.request("GET", "/country/code?code=" + code, headers=headers)
        res = conn.getresponse()
        data = res.read()
        jsoning = data.decode("utf-8")
        fulljson = json.loads(jsoning)
        for key, value in fulljson.items():
            zerodic = value[0]
        return(zerodic)
    
