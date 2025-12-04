import requests

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
charinfo = getchar("Herucles")
print(charinfo)