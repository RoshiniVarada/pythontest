import bs4
import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl
from flask import Flask
smtp_server = "smtp.gmail.com"
sender_email = "sairohith.guntupally1@gmail.com"
receiver_email = "sairohith.guntupally1@gmail.com"
password = "trashfound404"
i=1
from flask import Flask 
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>Testing App</h1>"

