from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

load_dotenv()

URL="https://appbrewery.github.io/instant_pot/"
web_page = requests.get(URL).text

soup= BeautifulSoup(web_page,"html.parser")
#print(soup.prettify())
product_price =soup.find(class_="aok-offscreen").getText()

price_without_symbol = product_price.split("$")[1]
#print(price_without_symbol)

product_title = soup.find(id="productTitle").get_text().strip()
#print(product_title)


