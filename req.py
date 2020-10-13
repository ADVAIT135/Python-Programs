import requests
from bs4 import BeautifulSoup
import pandas


oyo_url = "https://www.oyorooms.com/hotels-in-mumbai/?page="

req = requests.get(oyo_url)
content = req.content

soup = BeautifulSoup(content,"html.parser")

all_hotels = soup.find_all("div",{"class":"hotelCardListing"})


dataFrame = pandas.DataFrame(all_hotels)
dataFrame.to_csv("Oyo.csv")
