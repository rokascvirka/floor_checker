from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import time, sleep
import smtplib

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


driver = webdriver.Chrome(executable_path="C:\\Users\\r.c\\Downloads\\chromedriver_win32\\chromedriver.exe") #path to chromedriver.exe. Note that you need to use escape character \ for every - \

driver.get("https://opensea.io/collection/billionaireclubnft") #project link



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


def email_sender():
    gmailaddress = 'xr@gmail.com' #senders email login NOTE: Turn off all bullshit of gmail safety 
    gmailpassword = 'l' #senders email password
   
    mailto = 'x@gmail.com' #write your email
    msg = 'Pasikeitimas eik checkink savo NFT'
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    print(" \n Sent!")
    mailServer.quit()


def price_drop():
    print(f" Crash! Dabartinė floor kaina krito žemiau nustatytos {floor} floor ribos: kaina yra {price}")
    email_sender()
    sleep(60)


def price_growth():
    print(f"Kaina auga! NFT floor dabar yra {price}. Tavo nustatyta aukščiausia kainos riba - {roof}")
    email_sender()
    sleep(60)

def regular_price():
    print(f"Dabartinė floor kaina {price} yra nustatytose ribose: žemiausia galima kaina yra {floor}, didžiausia yra {roof}")
    sleep(60)

price_checker()
