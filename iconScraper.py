import config
import requests
from PIL import Image

def emoteDictionary(icon):
    return {

    }.get(icon, icon)

def getCards():
    URL = config.URL_CARDS
    r = requests.get(url=URL).json()
    data = r
    return data

def iconScraper(URL):
    im = Image.open(requests.get(URL, stream=True).raw)
    im.save(f"{iconId}.png")

iconIds = []

data = getCards()
for i in data: 
    iconId = data[i]['iconId']
    if i not in iconIds:
        iconIds.append(iconId)
    #iconIds += f"{iconId}\n"

f = open("iconIds.txt", "x")
f.write("{\n")
for i in iconIds:
    f.write(f"'<>' : '{i}'\n")
f.write("}")
f.close()
    # iconImageURL = f"{config.URL_EFFECT_ICONS}{iconId}.png"
    # print(f"Downloading: {iconId}")
    # iconScraper(iconImageURL)

