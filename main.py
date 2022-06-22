import base64
from operator import index
import requests
import pprint 
import sec
 
clientId = sec.Id
clientSecret = sec.KEY
clientData = f"{clientId}:{clientSecret}"
encodedData = str(base64.b64encode(clientData.encode("utf-8")), "utf-8")
authorizationHeaderString = f"Basic {encodedData}" 

pp = pprint.PrettyPrinter(indent=2)


#get items
item_data = requests.get("https://api.skinport.com/v1/items?app_id=730¤cy=EUR&tradable=0", params={
    "app_id": 730,
    "currency": "EUR",
    "tradable": 0,
}).json()

#get sales
sales_data = requests.get("https://api.skinport.com/v1/sales/history", params={
    "app_id": 730,
    "currency": "EUR",
    "market_hash_name": "Glove Case Key,★ Karambit | Slaughter (Minimal Wear)"
}).json()

def ApiData(itemName):
    for i in item_data:
        if(i['market_hash_name'] == str(itemName)):
            print("------------------------")
            print (i['market_hash_name'])
            print("\n")
            print (f"Max Price: {i['max_price']}")
            print (f"Mean Price: {i['mean_price']}")
            print (f"Min Price: {i['min_price']}")
            break

    for i in sales_data:
        if(i['market_hash_name'] == str(itemName)):
            print(pp.pprint(i['last_30_days']))
            print(pp.pprint(i['last_7_days']))
            print('................................\n')
            print(i['item_page'])
            print('\n..............................\n')
            break


