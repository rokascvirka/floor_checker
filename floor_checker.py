from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import time, sleep
import smtplib

#roof = raw_input(float(input('Mažiausia galima kaina?')))

#def clean_roof(roof):
#    #if roof.isdigit
#    #roof = roof.replace(",", ".")
#    while True:
#        try:
#            roof = raw_input('Mažiausia galima kaina?')
#            real_roof = float(roof)
#            # validity check(s)
#            if roof < 0: raise ValueError('Skaičius turi būti teigiamas')
#        except ValueError, e:
#            print("ValueError: '{}'".format(e))
#            print("Please try entering it again...")
#        except KeyboardInterrupt:
#            sys.exit("\n<terminated by user>")
#        except:
#            exc_value = sys.exc_info()[1]
#            exc_class = exc_value.__class__.__name__
#            print("{} exception: '{}'".format(exc_class, exc_value))
#            sys.exit("<fatal error encountered>")
#        else:
#            break  # no exceptions occurred, terminate loop

roof = float(0.8)
floor = float(0.7)

driver = webdriver.Chrome(executable_path="C:\\Users\\rokas.cvirka\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://opensea.io/collection/billionaireclubnft")



def price_checker():
    while True:
    
        html = driver.page_source

        soup = BS(html,"html.parser")
        listas = soup.findAll('div',{"class":"Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf"})
        listas[2].text

        global kaina
        kaina = float(listas[2].text)

        if kaina >= roof:
            kainos_augimas()
        elif kaina <= floor:
            kainos_kritimas()
        else:
            normali_kaina()


def email_sender():
    gmailaddress = 'y@gmail.com'
    gmailpassword = 'z'
   
    mailto = 'x@gmail.com'
    msg = 'Pasikeitimas eik checkink savo NFT'
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    print(" \n Sent!")
    mailServer.quit()


def kainos_kritimas():
    print(f" Crash! Dabartinė floor kaina krito žemiau nustatytos {floor} floor ribos: kaina yra {kaina}")
    email_sender()
    sleep(60 - time() % 60)


def kainos_augimas():
    print(f"Kaina auga! NFT floor dabar yra {kaina}. Tavo nustatyta aukščiausia kainos riba - {roof}")
    email_sender()
    sleep(60 - time() % 60)


def normali_kaina():
    print(f"Dabartinė floor kaina {kaina} yra nustatytose ribose: žemiausia galima kaina yra {floor}, didžiausia yra {roof}")
    sleep(60 - time() % 60)

price_checker()
