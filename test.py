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
def say_hello():
    print("Hello there!")
window = Tk()
window.title("Button Example")
my_button = Tk.Button(
window, 
text="Say Hello",
command=say_hello, 
font=("Arial", 16), 
bg="lightblue",
fg="black", 
relief="raised", 
padx=10, pady=5)