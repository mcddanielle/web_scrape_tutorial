#beautiful soup is designed to scrap the web
#https://www.crummy.com/software/BeautifulSoup/

from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?CityName=Forest+Grove&state=OR&site=PQR&textField1=45.52&textField2=-123.109&e=0")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")

forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()

print(period)
print(short_desc)


#NOW
current = soup.find(id='current_conditions-summary')
current_items = current.find_all("p")
#print(current) #.prettify())
#print()
temp = current_items[1].get_text()
#print(temp)

#all days
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
#print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(len(short_descs))
print(len(descs))

weather = pd.DataFrame({
        "period": periods, 
        "short_desc": short_descs, 
        #"temp": temps, 
        "desc":descs
    })

print(weather)


weather2 = pd.DataFrame({
    "temp": temps, 
    })

temp_nums = weather2["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather2["temp_num"] = temp_nums.astype('int')
print(temp_nums)

print(weather2["temp_num"].mean())

is_night = weather2["temp"].str.contains("Low")
weather2["is_night"] = is_night
print(is_night)
