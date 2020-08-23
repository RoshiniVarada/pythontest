import bs4
import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'])  # at the end point /
def stock(): 
 smtp_server = "smtp.gmail.com"
 sender_email = "sairohith.guntupally1@gmail.com"
 receiver_email = "sairohith.guntupally1@gmail.com"
 password = "trashfound404"
 i=1
 while True:
  price=parsePrice()
  print(price)
  if price >= 295 and i==1:
    print("sell  ",i)
    i=0
    port = 587  # For starttls
    message="price above 306 sell stock"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
  if price <= 280 and i==0:
    print("buy  ",i)
    i=1
    port = 587  # For starttls
    message = "price below 294 buy stock"
    print("buy")
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
def parsePrice():
  r= requests.get('https://finance.yahoo.com/quote/BCH-USD/')
  soup = BeautifulSoup(r.text,'lxml')
  price=soup.find_all('div',{'class':'D(ib) Va(m) Maw(65%) Ov(h)'})[0].find('span').text
  price=float(price)
  return price
