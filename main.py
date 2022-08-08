import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Black-4/dp/B01LWVX2RG/ref=sr_1_15?qid=1659908271&s=videogames-intl-ship&sr=1-15"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": 'en-CZ,en;q=0.9,cs-CZ;q=0.8,cs;q=0.7,en-GB;q=0.6,en-US;q=0.5'
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

my_email = "liborhavranek91@gmail.com"
password = "fopggzzzzpbcebtp"

print(price_as_float)

if price_as_float < 40:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ctiborekskutr@seznam.cz",
                         msg=f"Price of controler is lower than 40 dollars, amazon want {price} for controller")
        connection.close()
else:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ctiborekskutr@seznam.cz",
                         msg=f"Price of controler is grather than 40 dollars, amazon want {price} for controller. You have to waiting !!!")
        connection.close()