import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Enter URL of the product\n")
Expected_price = float(
    input("Enter price at which you want to buy the product\n"))

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76'}


def check():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    base_price = (price[2:8])

    final_price = float(base_price.replace(',', '.'))

    if(final_price < Expected_price):
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('aritamasthana@gmail.com', 'usdpmverharenljk')

    subject = "PRICE DROP ALERT!!"

    body = "Check product at "+URL

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'aritamasthana@gmail.com',
        'aritamasthana@gmail.com',
        msg

    )
    print('EMAIL SENT')

    server.quit()


while(True):
    check()
    time.sleep(60*60)
