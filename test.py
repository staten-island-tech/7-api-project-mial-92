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

def character(nintendo):
    nintendo = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={nintendo.lower()}")
    if nintendo.status_code != 200:
        print("Error. Cannot fetch data.")
        return None
    data = nintendo.json()
    return data
nintendoinfo = character("yoshi")
print(nintendoinfo)

import tkinter
from tkinter import *
root = Tk() 
root.title("Message Reverser")
root.geometry("400x250")
prompt = Tk.Label(root, text="Type your message below")
result_label = Tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=15)
