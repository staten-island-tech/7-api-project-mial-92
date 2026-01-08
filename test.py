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
import pprint
def character(nintendo):
    nintendo = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name={nintendo.lower()}")
    if nintendo.status_code != 200:
        print("Error. Cannot fetch data.")
        return "error"
    data = nintendo.json()
    return pprint.pformat(data)
nintendoinfo = character("")
print(nintendoinfo)

import tkinter
from tkinter import *
def function():
    thing = character(resposnes.get())
    lable.config(text= thing)
window = Tk()
window.title("Button Example")
my_button = Button(window, text="Type in a Nintendo Character's name", command=function, font=("Arial", 16), bg="lightblue", fg="black", relief="raised", 
padx=10, pady=5)
my_button.pack()

resposnes = Entry(window, width= 30)
resposnes.pack()

lable = Label(window, text="", wraplength= 800)
lable.pack()
window.mainloop()