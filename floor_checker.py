from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import time, sleep
import smtplib

#import tkinter as tk
#from tkinter import filedialog, Text
#import os

#root = tk.Tk()

#canvas = tk.Canvas(root, height=600, width=400, bg="#263d42")
#canvas.pack()

#frame = tk.Frame(root, bg="#3e646c")
#frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

#root.mainloop()


def highest_floor_price(roof):
    try:
        float(roof)
        return True
    except ValueError:
        return False
    return True

while True:
    roof = input('Write the highest floor price: \n')
    if highest_floor_price(roof):
        roof = float(roof)
        if roof >= 0:
            print(f'The floor is set to: {roof} ')
            break
        else:  # Use else
            print(f"The highest price must be a positive number only. You wrote: '{roof}'. What a noob... Please try again.")
    else:  # No need to call integer_check(..) again
        print(f"Sorry, that's not a number. You wrote: '{roof}'. What a double noob you are... Please try again.")

def lowest_floor_price(floor):
    try:
        float(floor)
        return True
    except ValueError:
        return False
    return True

while True:
    floor = input('Write the lowest floor price: \n')
    if lowest_floor_price(floor):
        floor = float(floor)
        if floor >= 0:
            print(f'The floor is set to: {floor} ')
            break
        else:  # Use else
            print(f"The highest price must be a positive number only. You wrote: '{floor}''. What a noob... Please try again.")
    else:  # No need to call integer_check(..) again
        print(f"Sorry, that's not a number. You wrote: '{floor}'. What a double noob you are... Please try again.")


driver = webdriver.Chrome(executable_path="C:\\Users\\rokas.cvirka\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://opensea.io/collection/cryptozombieznft")



def price_checker():
    while True:
    
        html = driver.page_source

        soup = BS(html,"html.parser")
        listas = soup.findAll('div',{"class":"Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf"})
        listas[2].text

        global price
        price = float(listas[2].text)

        if price >= roof:
            price_growth()
        elif price <= floor:
            price_drop()
        else:
            regular_price()


def price_growth_email_sender():
    gmailaddress = 'nftmailsender@gmail.com'
    gmailpassword = 'nftlietuva'
   
    mailto = 'iggysservice@gmail.com'
    #msg = print(f'floor kaina pakilo: {price}') + str(kaina)
    msg = 'floor price pakilo iki '  + str(price)
    mailserver = smtplib.smtp('smtp.gmail.com' , 587)
    mailserver.starttls()
    mailserver.login(gmailaddress , gmailpassword)
    mailserver.sendmail(gmailaddress, mailto , msg)
    print(" \n sent!")
    mailserver.quit()

def price_drop_email_sender():
    gmailaddress = 'nftmailsender@gmail.com'
    gmailpassword = 'nftlietuva'
   
    mailto = 'rokas42@gmail.com'
    #msg = print(f'dabartinė floor kaina krenta: {price}')
    msg = 'floor price nukrito iki ' + str(price)
    mailserver = smtplib.smtp('smtp.gmail.com' , 587)
    mailserver.starttls()
    mailserver.login(gmailaddress , gmailpassword)
    mailserver.sendmail(gmailaddress, mailto , msg)
    print(" \n sent!")
    mailserver.quit()



def price_drop():
    print(f"crash! dabartinė floor kaina krito žemiau nustatytos {floor} floor ribos: kaina yra {price}")
    price_drop_email_sender()
    sleep(300)
    driver.refresh()


def price_growth():
    print(f"kaina auga! nft floor dabar yra {price}. tavo nustatyta aukščiausia kainos riba yra {roof}")
    price_growth_email_sender()
    sleep(300)
    driver.refresh()

def regular_price():
    print(f"dabartinė floor kaina {price} yra nustatytose ribose: žemiausia galima kaina yra {floor}, didžiausia yra {roof}")
    sleep(60)
    driver.refresh()

price_checker()
  
