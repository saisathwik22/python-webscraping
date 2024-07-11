import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Description = []
Reviews = []



url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(1)

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
box = soup.find("div", class_ = "DOjaWF gdgoEp")
      

names = box.find_all("div", class_ = "KzDlHZ")

for i in names:
      name = i.text
      Product_name.append(name)

# print(Product_name)

prices = box.find_all("div", class_ = "Nx9bqj _4b5DiR")

for i in prices:
      name = i.text
      Prices.append(name)

# print(Prices)

desc = box.find_all("ul", class_ = "G4BRas")

for i in desc:
      name = i.text
      Description.append(name)

# print(Description)

reviews = box.find_all("div", class_ = "XQDdHH")

for i in reviews:
      name = i.text
      Reviews.append(name)

# print(len(Reviews))

df = pd.DataFrame({"Product name":Product_name, "Prices":Prices, "Description":Description, "Reviews":Reviews})
# print(df)

df.to_csv("C:/Users/Bunny/Desktop/PRODIGY_SD_05/flipkart_mobiles_under_50K.csv")