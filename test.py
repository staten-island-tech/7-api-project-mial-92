""" import requests

def getchar(character):
    response = requests.get(f"https://api.disneyapi.dev/character{character.lower()}")
    if response.status_code != 200:
        print("Error. Cannot fetch data.")
        return None
    
    data = response.json()
    return{
        "filmname": data["films"],
        "charname": data["name"],
        "charallies": data["allies"],
        "charenemies": data["enemies"]
    }
charinfo = getchar("Hercules")
print(charinfo)
 """
import requests

def getchar(character):
    response = requests.get(f"https://api.disneyapi.dev/character")
    if response.status_code != 200:
        print("Error. Cannot fetch data.")
        return None
    
    data = response.json()
    for i in range(len(data)):
        if data[i]["name"] == character:
            return data[i]["name"]
    
charinfo = getchar("Hercules")
print(charinfo)