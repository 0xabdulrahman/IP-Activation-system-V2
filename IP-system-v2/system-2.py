from tkinter import *
from tkinter import messagebox
import requests
import socket
from time import strftime
from datetime import date

string = strftime('%H:%M:%S %p')
date = str(date.today())

token = '' # your bot token
ID = '' # your telegram ID

name = socket.gethostname()
IP = socket.gethostbyname(name)

web = f'' # your pastebin website
tele_api = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=- new user : {IP}\n- time : {string}\n- date : {date}'

root = Tk()
root.geometry("250x120")
root.title("Log in form")
root.resizable(0,0)

update = requests.get('https://pastebin.com/raw/5j13aM9W').text
if update == '0':
    pass
if update == '1':
    messagebox.showinfo("Login", "New update available!\nCheck @abdulrahman.sarmad on IG\nfor the latest updates")
    root.destroy()
    exit()

def Login():
    req = requests.get(web).text
    if f'{IP}' in req:
        messagebox.showinfo("Login", "Logged in")
        root.destroy()
        # tool here

    else:
        messagebox.showerror("Login", "Your ip is not activated!")

def Send():
    tele = requests.get(tele_api).status_code
    if tele == 200:
        messagebox.showinfo(f"Login", "Your ip was sent to the developer")
    else:
        messagebox.showerror("Login", "Error while sending your IP address")

def Exit():
    root.destroy()
    exit()

Button(root, text = "Log in",width=20, command=Login).place(x = 50, y = 50)
Button(root, text = "Send ip",width=20, command=Send).place(x = 50, y = 25)
Button(root, text = "Exit",width=20, command=Exit).place(x = 50, y = 75)

root.mainloop()
