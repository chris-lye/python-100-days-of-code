import smtplib
import requests
from bs4 import BeautifulSoup
import lxml
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.com/GoPro-HERO9-Black-Commerce-Stabilization/dp/B09J713ZS7/ref=sr_1_1_sspa?crid=4VH5VT4THL4U&keywords=gopro%2Bcold%2Bweather&qid=1668256390&sprefix=gopro%2Bcold%2Bweathe%2Caps%2C292&sr=8-1-spons&smid=ANIVUW1SREVVT&th=1"
my_email = os.getenv('MY_EMAIL')
password = os.getenv('MAILER_PASSWORD')

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(url=URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, 'lxml')
price = soup.find(name='span', class_='a-price-whole').getText().split(".")[0]
print(price)

full_title = soup.find(id="productTitle").get_text().strip()
title = full_title[:10] + ".."
print(title)


lower_limit = 400
if int(price) < lower_limit:
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=my_email, 
                msg=f"Subject:Amazon Price Alert:{title}!\n\nThe price of {full_title} is now {price}"
            )

