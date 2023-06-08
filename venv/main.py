import requests
from bs4 import BeautifulSoup as Bs
import csv
url = "https://store.steampowered.com/hwsurvey/videocard/?sort=pct"
page  = requests.get(url)

soup = Bs(page.content, "html.parser")
rows = soup.find_all("div", class_="substats_row")

with open("graphic_cards.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "jan", "feb", "mar", "apr", "may", "increase"])
    for row in rows:
        name = row.find("div", class_="substats_col_left")
        month_val = row.find_all("div", class_="substats_col_month")
        last_month = row.find("div", class_="substats_col_month_last_pct")
        increase = row.find("div", class_ ="substats_col_month_last_chg")
        card_data = [name.text]
        card_data.extend([month.text for month in month_val])
        card_data.extend([last_month.text, increase.text])
        writer.writerow(card_data)

    
