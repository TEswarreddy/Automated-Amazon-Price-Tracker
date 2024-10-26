from bs4 import BeautifulSoup
import requests
import smtplib

import os
from dotenv import load_dotenv,dotenv_values

# Load environment variables from .env file
load_dotenv()

URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header= {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 
   }

web_page = requests.get(url = URL,headers = header).text

soup= BeautifulSoup(web_page,"html.parser")
#print(soup.prettify())
product_price =soup.find(class_="aok-offscreen").getText()
#print(product_price)

price_without_symbol = product_price.split("$")[1]
#print(price_without_symbol)

price_as_float = float(price_without_symbol.split(" ")[0])


product_title = soup.find(id="productTitle").get_text().strip()
#print(product_title)

BUY_PRICE = 100

EMAIL_ADDRESS="your_gmail"
EMAIL_PASSWORD="your_app_password_under_security_app-password"
SMTP_ADDRESS="smtp.gmail.com"

if price_as_float < BUY_PRICE:
    message = f"{product_title} \n is on sale for {product_price}!"

    
    
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
