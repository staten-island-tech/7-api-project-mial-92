""" import requests

def getfruit(fruit):
    fruit = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit.lower()}")
    if fruit.status_code != 200:
        print("Error. Cannot fetch data.")
        return None
    
    data = fruit.json()
    return{
        "fruit name": data["name"],
        "fruit genus": data["genus"],
        "fruit family": data["family"],
        "fruit nutrients": data["nutritions"]
    }
fruitinfo = getfruit("banana")
print(fruitinfo) """

import requests

def getfruit(fruit):
    fruit = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit.lower()}")
    if fruit.status_code != 200:
        print("Error. Cannot fetch data.")
        return None
    
    data = fruit.json()
    return data
fruitinfo = getfruit("banana")
print(fruitinfo)