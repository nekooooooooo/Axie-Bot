import config
import requests
import pprint

partsDict = { 'Eyes': {}, 'Back': {}, 'Horn': {}, 'Ears': {}, 'Mouth': {}, 'Tail': {} }
backDict = {}
hornDict = {}
mouthDict = {}
tailDict = {}

def emoteDictionary(type):
    return {
        'aquatic-back': '<:back_aqua:880709296726360064>',
        'aquatic-horn': '<:horn_aqua:880709299633008660>',
        'aquatic-mouth': '<:mouth_aqua:880709297686855680>',
        'aquatic-tail': '<:tail_aqua:880709297640710154>',
        'beast-back': '<:back_beast:880709296646676500>',
        'beast-horn': '<:horn_beast:880709299221979137>',
        'beast-mouth': '<:mouth_beast:880709297644900382>',  
        'beast-tail': '<:tail_beast:880709297582006282>',
        'bird-back': '<:back_bird:880709296504066089>',
        'bird-horn': '<:horn_bird:880709297619730453>',
        'bird-mouth': '<:mouth_bird:880709297665900544>',  
        'bird-tail': '<:tail_bird:880709299712716900>',
        'bug-back': '<:back_bug:880709297598767165>',
        'bug-horn': '<:horn_bug:880709297863024670>',
        'bug-mouth': '<:mouth_bug:880709297376464937>',  
        'bug-tail': '<:tail_bug:880709297372270663>',
        'plant-back': '<:back_plant:880709297137418271>',
        'plant-horn': '<:horn_plant:880709299658174484>',
        'plant-mouth': '<:mouth_plant:880709297632346152>',  
        'plant-tail': '<:tail_plant:880709297766559764>',
        'reptile-back': '<:back_reptile:880709297577795604>',
        'reptile-horn': '<:horn_reptile:880709297380667403>',
        'reptile-mouth': '<:mouth_reptile:880709297665892382>',  
        'reptile-tail': '<:tail_reptile:880709297770745888>'
    }.get(type, "error")

def getCards():
    URL = config.URL_CARDS
    r = requests.get(url=URL).json()
    data = r
    return data

data = getCards()
for i in data:
    cardId = data[i]['id']
    cardPartName = data[i]['partName']
    cardSkillName = data[i]['skillName']
    cardIconId = data[i]['iconId']
    splitCardId = cardId.split('-')
    tempType = f"{splitCardId[0]}-{splitCardId[1]}"
    classType = splitCardId[0]
    part = splitCardId[1]
    # print(part, cardPartName)
    emote = emoteDictionary(tempType)
    # test = "%s : { 'id': %s, 'class': %s, 'emote': %s }"% (cardPartName, cardId, classType.title(), emote)
    if part == 'back':
        backDict[cardPartName] = { 'id': cardId, 'class': classType.title(), 'skillName': cardSkillName.title(), 'emote': emote }
    elif part == 'horn':
        hornDict[cardPartName] = { 'id': cardId, 'class': classType.title(), 'skillName': cardSkillName.title(), 'emote': emote }
    elif part == 'mouth':
        mouthDict[cardPartName] = { 'id': cardId, 'class': classType.title(), 'skillName': cardSkillName.title(), 'emote': emote }
    elif part == 'tail':
        tailDict[cardPartName] = { 'id': cardId, 'class': classType.title(), 'skillName': cardSkillName.title(), 'emote': emote }

partsDict['Back'] = backDict
partsDict['Horn'] = hornDict
partsDict['Mouth'] = mouthDict
partsDict['Tail'] = tailDict

f = open("parts_dict.txt", "x")
f.write(str(partsDict))
f.close()

