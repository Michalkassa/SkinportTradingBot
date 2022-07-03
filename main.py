import base64
from operator import index
from types import NoneType
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
def RequestSale(ItemNameSale):
    return requests.get("https://api.skinport.com/v1/sales/history", params={
    "app_id": 730,
    "currency": "EUR",
    "market_hash_name": f"{ItemNameSale}"
    }).json()

sellprice = 0
minimumprice = 0

# def ApiData():
#     minimumprice = 0 
#     sellprice = 0
#     for item in item_data:
#         minimumprice = item['min_price']
#         for sale in sales_data:
#             if sale["market_hash_name"] == item["market_hash_name"]:
#                 sellprice = int(sale['last_30_days']['max']) * 0.88
#         return [item['market_hash_name'],sellprice - minimumprice]


#         print("\n")
#         print (f"Max Price: {i['max_price']}")
#         print (f"Mean Price: {i['mean_price']}")
#         print (f"Min Price: {i['min_price']}")

    # for i in sales_data:
    #     sellprice = i['last_30_days']['max'] * 0.88
#         print(pp.pprint(int(i['last_30_days']['max'])))
#         print(pp.pprint(i['last_7_days']))
#         print('................................\n')
#         print(i['item_page'])
#         print('\n..............................\n')
#         print(sellprice - minimumprice)
        

indx = 0
while indx <= 2:
    minimumprice = 0
    sellprice = 0
    for item in item_data:
        minimumprice = 0
        #type checking for non in the skinport api as prices can be none
        if type(RequestSale(item["market_hash_name"])[0]["last_7_days"]["min"]) != NoneType:
            minimumprice = item["min_price"]
        if type(RequestSale(item["market_hash_name"])[0]["last_7_days"]["min"]) != NoneType:
            sellprice = RequestSale(item["market_hash_name"])[0]["last_7_days"]["min"]

        #display data by printing
        print(item['market_hash_name']) 
        profit = float(sellprice * 0.88 ) - minimumprice
        print(profit)
        print(sellprice)

