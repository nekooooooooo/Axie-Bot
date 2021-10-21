import requests
import json
import config
import time
from PIL import Image

def getCards():
    URL = config.URL_CARDS
    r = requests.get(url=URL).json()
    data = r
    return data

def imageScraper(URL):
    im = Image.open(requests.get(URL, stream=True).raw)
    im.save(f"{cardSkillName}.png")   

data = getCards()
for i in data:
    cardId = data[i]['id']
    cardSkillName = data[i]['skillName']
    cardImageURL = f"{config.URL_CARD_IMAGES}{cardId}.png"
    print(f"Downloading: {cardSkillName}")
    time.sleep(0.1)
    imageScraper(cardImageURL)
