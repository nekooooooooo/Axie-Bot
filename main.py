from discord.ext.commands.errors import PartialEmojiConversionFailure
import requests
import discord
import asyncio
import itertools
import random
import locale
import config
import json
import textwrap
import re
# from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
from datetime import datetime, timezone
from dateutil import parser
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from discord.ext.commands import CommandNotFound

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

dev = "nekooooooooo#5800"

prefix = "a!"

locale.setlocale(locale.LC_ALL, '')

skillDict = {}
partDict = {}
skillList = []
partList = []
# quaticDict, plantDict, beastDict, bugDict, reptileDict, birdDict = {}, {}, {}, {}, {}, {}
aquaticList, plantList, beastList, bugList, reptileList, birdList = [], [], [], [], [], []


def getCards():
    print("Requesting URL_CARDS...")
    URL = config.URL_CARDS
    r = requests.get(url=URL).json()
    data = r
    print("Getting Cards...")
    for i in data: 
        skillDict[data[i]['skillName'].lower()] = data[i]['id']
        skillList.append(data[i]['skillName'].lower())
        partDict[data[i]['partName'].lower()] = data[i]['id']
        partList.append(data[i]['partName'].lower())
    print("Done...")

def addToClassList():
    f = open('parts_dict.json')
    print("Opening parts_dict.json...")
    data = json.load(f)
    # print(data)
    for i in data:
        if i in ['Back', 'Horn', 'Tail', 'Mouth']:
            for j in data[i]:
                if data[i][j]['class'] == 'Aquatic':
                    aquaticList.append(f"{j} | {data[i][j]['skillName']}")
                if data[i][j]['class'] == 'Beast':
                    beastList.append(f"{j} | {data[i][j]['skillName']}")
                if data[i][j]['class'] == 'Bird':
                    birdList.append(f"{j} | {data[i][j]['skillName']}")
                if data[i][j]['class'] == 'Bug':
                    bugList.append(f"{j} | {data[i][j]['skillName']}")
                if data[i][j]['class'] == 'Plant':
                    plantList.append(f"{j} | {data[i][j]['skillName']}")
                if data[i][j]['class'] == 'Reptile':
                    reptileList.append(f"{j} | {data[i][j]['skillName']}")
    f.close()
    print("Done...")

# addToClassList()

def addMystic():
    print("Adding Mystic Parts!")
    partDict['hasagi'] = 'beast-back-02'
    partDict['hamaya'] = 'beast-back-08'
    partDict['candy canes'] = 'bug-back-04'
    partDict['starry shell'] = 'bug-back-02'
    partDict['origami'] = 'bird-back-04'
    partDict['starry balloon'] = 'bird-back-02'
    partDict['pink turnip'] = 'plant-back-02'
    partDict['yakitori'] = 'plant-back-04'
    partDict['crystal hermit'] = 'aquatic-back-02'
    partDict['1nd14n-5t4r'] = 'reptile-back-08'
    partDict['frozen bucket'] = 'reptile-back-08'
    partDict['rugged sail'] = 'reptile-back-02'
    partDict['skull cracker'] = 'beast-mouth-02'
    partDict['feasting mosquito'] = 'bug-mouth-02'
    partDict['kawaii'] = 'bug-mouth-08'
    partDict['mr. doubletalk'] = 'bird-mouth-02'
    partDict['humorless'] = 'plant-mouth-02'
    partDict['rudolph'] = 'plant-mouth-04'
    partDict['geisha'] = 'aquatic-mouth-10'
    partDict['lam handsome'] = 'aquatic-mouth-02'
    partDict['dango'] = 'reptile-mouth-10'
    partDict['tiny carrot'] = 'reptile-mouth-10'
    partDict['venom bite'] = 'reptile-mouth-02'
    partDict['kendama'] = 'beast-horn-04'
    partDict['umaibo'] = 'beast-horn-08'
    partDict['winter branch'] = 'beast-horn-02'
    partDict['laggingggggg'] = 'bug-horn-02'
    partDict['p4r451t3'] = 'bug-horn-10'
    partDict['golden shell'] = 'bird-horn-02'
    partDict['spruce spear'] = 'bird-horn-12'
    partDict['golden bamboo shoot'] = 'plant-horn-02'
    partDict["santa's gift"] = 'plant-horn-10'
    partDict['yorishiro'] = 'plant-horn-04'
    partDict['5h04l-5t4r'] = 'aquatic-horn-12'
    partDict['candy babylonia'] = 'aquatic-horn-02'
    partDict['pinku unko'] = 'reptile-horn-02'
    partDict['sakura cottontail'] = 'beast-tail-02'
    partDict['fire ant'] = 'bug-tail-02'
    partDict['maki'] = 'bug-tail-06'
    partDict['omatsuri'] = 'bird-tail-10'
    partDict['snowy swallow'] = 'bird-tail-02'
    partDict['namek carrot'] = 'plant-tail-02'
    partDict['koinobori'] = 'aquatic-tail-02'
    partDict['kuro koi'] = 'aquatic-tail-02'
    partDict['december surprise'] = 'reptile-tail-08'
    partDict['escaped gecko'] = 'reptile-tail-02'
    partDict['fir trunk'] = 'reptile-tail-06'
    partList.append('hasagi')
    partList.append('hamaya')
    partList.append('candy canes')
    partList.append('starry shell')
    partList.append('origami')
    partList.append('starry balloon')
    partList.append('pink turnip')
    partList.append('yakitori')
    partList.append('crystal hermit')
    partList.append('1nd14n-5t4r')
    partList.append('frozen bucket')
    partList.append('rugged sail')
    partList.append('skull cracker')
    partList.append('feasting mosquito')
    partList.append('kawaii')
    partList.append('mr. doubletalk')
    partList.append('humorless')
    partList.append('rudolph')
    partList.append('geisha')
    partList.append('lam handsome')
    partList.append('dango')
    partList.append('tiny carrot')
    partList.append('venom bite')
    partList.append('kendama')
    partList.append('umaibo')
    partList.append('winter branch')
    partList.append('laggingggggg')
    partList.append('p4r451t3')
    partList.append('golden shell')
    partList.append('spruce spear')
    partList.append('golden bamboo shoot')
    partList.append("santa's gift")
    partList.append('yorishiro')
    partList.append('5h04l-5t4r')
    partList.append('candy babylonia')
    partList.append('pinku unko')
    partList.append('sakura cottontail')
    partList.append('fire ant')
    partList.append('maki')
    partList.append('omatsuri')
    partList.append('snowy swallow')
    partList.append('namek carrot')
    partList.append('koinobori')
    partList.append('kuro koi')
    partList.append('december surprise')
    partList.append('escaped gecko')
    partList.append('fir trunk')
    print("Mystic Parts Added!")

def isSkillSupported(skill):
    if skill in skillList:
        return True
    else: 
        return False

def isPartSupported(part):
    if part in partList:
        return True
    else: 
        return False

getCards()
addMystic()

def skillDictionary(skill):
    print("Converting Skill...")
    return skillDict.get(skill, skill)

def partDictionary(part):
    print("Converting Part...")
    return partDict.get(part, part)

def iconDictionary(icon):
    print("Getting Icon...")
    return {
        'critical-block' : '<:criticalblock:880699537981849630>',
        'draw-card' : '<:drawcard:880699538141245450>',
        'speed-up' : '<:speedup:880699538346770432>',
        'attack-up' : '<:attackup:880699538061549588>',
        'self-heal' : '<:selfheal:880699538208358470>',
        'prioritize' : '<:prioritize:880699538191552582>',
        'raise-damage' : '<:raisedamage:880699539588280342>',
        'raise-shield' : '<:raiseshield:880699538103468052>',
        'end-last-stand' : '<:endlaststand:880699538099281930>',
        'gain-energy' : '<:gainenemy:880699538074124338>',
        'jinx' : '<:jinx:880699538220908555>',
        'chill' : '<:chill:880699538057359390>',
        'critical' : '<:critical:880699537872797697>',
        'strike-first' : '<:strikefirst:880699539747639307>',
        'multi-hit' : '<:multihit:880699538120278026>',
        'energy-destroy' : '<:energydestroy:880699538099298324>',
        'lethal' : '<:lethal:880699538162208768>',
        'morale-up' : '<:moraleup:880699538065719338>',
        'fear' : '<:fear:880699537860223017>',
        'morale-down' : '<:moraledown:880699537860223017>',
        'remove-debuff' : '<:removedebuff:880699538233520188>',
        'double-hit' : '<:doublehit:880699538048946256>',
        'aroma' : '<:aroma:880699537746984971>',
        'disable-ability' : '<:disableability:880699538040569856>',
        'sleep' : '<:sleep:880699538095104032>',
        'attack-down' : '<:attackdown:880699537994444820>',
        'fixed-damage' : '<:fixeddamage:880699538053148672>',
        'stun' : '<:stun:880699538191568906>',
        'poison' : '<:poison:880699537797287957>',
        'heal-block' : '<:healblock:880699538069934110>',
        'fragile' : '<:fragile:880699538044772352>',
        'speed-down' : '<:speeddown:880699538078335007>',
        'discard' : '<:discard:880699537830846476>',
        'stench' : '<:stench:880699540079001630>',
        'ally-heal' : '<:allyheal:880699538057330688>',
        'untargetable' : '<:untargetable:880699538195767366>',
        'damage-reflect' : '<:damagereflect:880699537742778380>'
    }.get(icon,icon)

def getEmote(emote):
    return {
        'eye_aquatic': "<:eye_aqua:880709299280691200>",
        'back_aquatic': "<:back_aqua:880709296726360064>",
        'horn_aquatic': "<:horn_aqua:880709299633008660>",
        'ear_aquatic': "<:ear_aqua:880709297435205654>",
        'mouth_aquatic': "<:mouth_aqua:880709297686855680>",
        'tail_aquatic': "<:tail_aqua:880709297640710154>",
        'eye_beast': "<:eye_beast:880709297581985822>",
        'back_beast': "<:back_beast:880709296646676500>",
        'horn_beast': "<:horn_beast:880709299221979137>",
        'ear_beast': "<:ear_beast:880709297577816095>",
        'mouth_beast': "<:mouth_beast:880709297644900382>",
        'tail_beast': "<:tail_beast:880709297582006282>",
        'eye_bird': "<:eye_bird:880709299444260904>",
        'back_bird': "<:back_bird:880709296504066089>",
        'horn_bird': "<:horn_bird:880709297619730453>",
        'ear_bird': "<:ear_bird:880709297447796786>",
        'mouth_bird': "<:mouth_bird:880709297665900544>",
        'tail_bird': "<:tail_bird:880709299712716900>",
        'eye_bug': "<:eye_bug:880709297590398996>",
        'back_bug': "<:back_bug:880709297598767165>",
        'horn_bug': "<:horn_bug:880709297863024670>",
        'ear_bug': "<:ear_bug:880709297594581022>",
        'mouth_bug': "<:mouth_bug:880709297376464937>",
        'tail_bug': "<:tail_bug:880709297372270663>",
        'eye_plant': "<:eye_plant:880709297535852554>",
        'back_plant': "<:back_plant:880709297137418271>",
        'horn_plant': "<:horn_plant:880709299658174484>",
        'ear_plant': "<:ear_plant:880709297296785429>",
        'mouth_plant': "<:mouth_plant:880709297632346152>",
        'tail_plant': "<:tail_plant:880709297766559764>",
        'eye_reptile': "<:eye_reptile:880709297531670548>",
        'back_reptile': "<:back_reptile:880709297137418271>",
        'horn_reptile': "<:horn_reptile:880709297380667403>",
        'ear_reptile': "<:ear_reptile:880709297665892382>",
        'mouth_reptile': "<:mouth_reptile:880709297665892382>",
        'tail_reptile': "<:tail_reptile:880709297770745888>"
    }.get(emote, emote)

def getPartEmote(classType, part):

    classType = classType.lower()
    part = part.title()

    if part == 'Eyes':
        part = "eye"
    elif part == 'Ears':
        part = "ear"

    part = part.lower()
    
    emote = f"{part}_{classType}"

    return getEmote(emote)

def getPart(part):
    f = open('parts_dict.json')
    print("Opening parts_dict.json...")
    data = json.load(f)
    # print(data)
    for i in data:
        if part in data[i]:
            print(f"Part found in {i}")
            partData = data[i][part]
            # print(partData)
            return partData
        else:
            print(f"Cant find part in {i}. Trying Again...")
            partData = "Error"
    f.close()
    print("Done...")
    return partData

def getCard(card):
    print(f"Getting Card: {card}")
    card = card.lower()
    URL = config.URL_CARDS
    r = requests.get(url=URL).json()
    data = r
    return data[card]

def getAxie(axieId):
    print(f"Fetching Axie#{axieId}")
    URL = "https://axieinfinity.com/graphql-server-v2/graphql"
    variables = {
        "axieId": f"{axieId}"
    }
    r = requests.post(URL, json = {'query': config.query, 'variables': variables})
    data = r.json()
    print(f"Fetched")
    return data['data']['axie']

def getGenes(axieId):
    print(f"Fetching Axie#{axieId} Genes")
    URL = f"{config.URL_AXIE_GENES}{axieId}"
    r = requests.get(url=URL)
    data = r.json()
    print(f"Fetched")
    return data

def getEarnings(ronin):
    URL = config.URL_SCHO_EARNINGS + ronin
    r = requests.get(url=URL)
    data = r.json()
    return data

def getStats(ronin):
    URL = config.URL_BASIC_STATS + ronin
    r = requests.get(url=URL)
    data = r.json()
    return data

def getAxieImageURL(axie):
    URL = f"https://storage.googleapis.com/assets.axieinfinity.com/axies/{axie}/axie/axie-full-transparent.png"
    return URL

def getAxies(ronin):
    URL = config.URL_AXIES + ronin
    r = requests.get(url=URL)
    data = r.json()
    return data

def convertRonin(ronin):
    ronin = ronin.split("ronin:")
    ronin = f"0x{ronin[1]}"
    return ronin

def getPrefix(bot, msg):
    return [f"{prefix} ", f"{prefix}"]

activity = discord.Game(name="Use a!help | neko")

bot = commands.Bot(
    command_prefix = getPrefix,
    activity = activity,
    status = discord.Status.online,
    case_insensitive = True,
    help_command = None
)

DiscordComponents(bot)

axieCommandList = ['stats', 'axie', 'cards', 'parts']
infoCommandList = ['help', 'info', 'todo']

attackEmote = "<:iconatk:880816503463743558>"
defenseEmote = "<:icondef:880816503476330556>"
energyEmote = "<:energy:880822829518585866>"

@bot.event
async def on_ready():
    print(f'SaltyG Axie is running...')

def findUrl(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    return [x[0] for x in url]

@bot.event
async def on_message(msg):

    validLink = "https://marketplace.axieinfinity.com/axie/"
    links = findUrl(msg.content)

    pfx = getPrefix(bot, msg)[1]
    if msg.content.lower().startswith(pfx):
        msg.content = msg.content[:len(pfx)].lower() + msg.content[len(pfx):]
    else:
        for link in itertools.islice(links, 0, 3):
            if link.startswith(validLink):
                axieId = link.split(validLink)[1]
                axieId = axieId.replace('/', '')
                print(axieId)
                await axie(msg.channel, axieId)
            else:
                print("Invalid Link!")

    await bot.process_commands(msg)

@bot.command(aliases=['e'])
async def earnings(ctx, ronin):
    
    # found = false
    # for i in database
    #   if i equals ronin
    #       found = true
    # return found

    # if not found
    #   add to database

    earningsData = getEarnings(convertRonin(ronin))
    print(f"{earningsData}")
    await ctx.send(f'{earningsData}')

@bot.command(aliases=['s'])
async def stats(ctx, ronin):

    statsData = getStats(convertRonin(ronin))

    name = statsData['stats']['name']
    elo = statsData['stats']['elo']
    rank = statsData['stats']['rank']
    await ctx.send(f'Name: {name}\nMMR: {elo}\nRank: {rank}')

@bot.command(aliases=['a', 'ax'])
async def axie(ctx, *axies):

    if len(axies) > 3:
        embed = discord.Embed(
            title = f"Too Many Axies!",
            description = f"Please only enter max 3 axies! Thank You!",
            color = discord.Color.red()
        )
        return await ctx.send(embed = embed)

    for axie in axies:
        axieData = getAxie(axie)
        axieGenesData = getGenes(axie)

        axieMarketplaceLink = "https://marketplace.axieinfinity.com/axie/"
        
        axieName = axieData['name']
        axieClass = axieData['class']
        axieOwner = axieData['owner']
        axieOwnerName = axieData['ownerProfile']['name']
        axieBreedCount = axieData['breedCount']
        axieStats = axieData['stats']
        axieParts = axieData['parts']

        axieTraits = axieGenesData
        axieTraitsEyes = axieTraits['eyes']
        axieTraitsMouth = axieTraits['mouth']
        axieTraitsEars = axieTraits['ears']
        axieTraitsHorn = axieTraits['horn']
        axieTraitsBack = axieTraits['back']
        axieTraitsTail = axieTraits['tail']

        # PART_QUALITY = { 'D': 76 / 6, 'R1': 3, 'R2': 1 }
        # MAX_QUALITY = 6 * (PART_QUALITY['D'] + PART_QUALITY['R1'] + PART_QUALITY['R2'])

        # pureness = 0
        # quality = 0
        pureness = 0

        for i in range(len(axieParts)):
            if axieParts[i]['class'] == axieClass:
                pureness += 76 / 6

        for i in axieTraits:
            if i in ['eyes', 'mouth', 'ears', 'horn', 'back', 'tail']:
                if axieTraits[i]['r1']['class'] == axieClass.lower():
                    pureness += 3

        for i in axieGenesData:
            if i in ['eyes', 'mouth', 'ears', 'horn', 'back', 'tail']:
                if axieTraits[i]['r2']['class'] == axieClass.lower():
                    pureness += 1
        
        print(f"Name: {axieName}\nPureness: {pureness}")

        embed = discord.Embed(
            title = f"{axieName}",
            description = f"Axie #{axie}\n[Marketplace]({axieMarketplaceLink}{axie})"
        )

        if axieClass == 'Aquatic':
            axieClass = '<:aquatic:881201528428429323> ' + axieClass
            embed.color = 0x2de8f2
        elif axieClass == 'Beast':
            axieClass = '<:beast:881201528256491541> ' + axieClass
            embed.color = 0xffec51
        elif axieClass == 'Bird':
            axieClass = '<:bird:881201528495562762>' + axieClass
            embed.color = 0xffb4bb
        elif axieClass == 'Bug':
            axieClass = '<:bug:881201528428458035>' + axieClass
            embed.color = 0xf74e4e
        elif axieClass == 'Plant':
            axieClass = '<:plant:881201528462008380>' + axieClass
            embed.color = 0xccef5e
        elif axieClass == 'Reptile':
            axieClass = '<:reptile:881201528571048017>' + axieClass
            embed.color = 0xef93ff
        elif axieClass == 'Mech':
            axieClass = '<:mech:881201528550068244>' + axieClass
            embed.color = 0xc6bdd4
        elif axieClass == 'Dusk':
            axieClass = '<:dusk:881201528231313409>' + axieClass
            embed.color = 0x129092
        elif axieClass == 'Dawn':
            axieClass = '<:dawn:881201528092885063>' + axieClass
            embed.color = 0xbeceff

        embed.add_field(
            name = "Class",
            value = axieClass,
            inline = True
        )

        axieOwner = axieOwner.split("0x")
        axieOwner = axieOwner[1]
        axieOwner = f"ronin:{axieOwner}"

        print(axieOwner)

        embed.add_field(
            name = "Owner",
            value = f"[{axieOwnerName}](https://marketplace.axieinfinity.com/profile/{axieOwner}/axie)",
            inline = True
        )

        embed.add_field(
            name = "Breed Count",
            value = f"🥚 {axieBreedCount}/7",
            inline = True
        )

        # embed.add_field(
        #     name = "Stats",
        #     value = f"Health: 💚 **{axieStats['hp']}** | Speed: ⚡ **{axieStats['speed']}** | Skill: ⭐ **{axieStats['skill']}** | Morale: 🔥 **{axieStats['morale']}**",
        #     inline = False
        # )

        embed.add_field(
            name = "Stats",
            value = f"💚 **{axieStats['hp']}** | ⚡ **{axieStats['speed']}** | ⭐ **{axieStats['skill']}** | 🔥 **{axieStats['morale']}** | 🅿 **{round(pureness, 2)}**%",
            inline = False
        )

        # embed.add_field(
        #     name = "Body Parts",
        #     value = f'''
        #     {getPartEmote(axieParts[0]['class'], axieParts[0]['type'])} {axieParts[0]['type']['name']}
        #     {getPartEmote(axieParts[1]['class'], axieParts[1]['type'])} {axieParts[1]['type']['name']}
        #     {getPartEmote(axieParts[2]['class'], axieParts[2]['type'])} {axieParts[2]['type']['name']}
        #     {getPartEmote(axieParts[0]['class'], axieParts[0]['type'])} {axieParts[0]['type']['name']}
        #     {getPartEmote(axieParts[0]['class'], axieParts[0]['type'])} {axieParts[0]['type']['name']}
        #     {getPartEmote(axieParts[0]['class'], axieParts[0]['type'])} {axieParts[0]['type']['name']}
        #     ''',
        #     inline = False
        # )

        parts = ''
        for index, value in enumerate(axieParts):
            parts += f"{getPartEmote(axieParts[index]['class'], axieParts[index]['type'])} {axieParts[index]['name']}\n"

        # embed.add_field(
        #     name = "Body Parts",
        #     value = parts,
        #     inline = True
        # )

        embed.add_field(
            name = "Body Parts",
            value = f'''
            {getPartEmote(axieParts[0]['class'], axieParts[0]['type'])} {axieParts[0]['name']}
            {getPartEmote(axieParts[1]['class'], axieParts[1]['type'])} {axieParts[1]['name']}
            ''',
            inline = True
        )

        embed.add_field(
            name = "\u200b",
            value = f'''
            {getPartEmote(axieParts[2]['class'], axieParts[2]['type'])} {axieParts[2]['name']}
            {getPartEmote(axieParts[3]['class'], axieParts[3]['type'])} {axieParts[3]['name']}
            ''',
            inline = True
        )

        embed.add_field(
            name = "\u200b",
            value = f'''
            {getPartEmote(axieParts[4]['class'], axieParts[4]['type'])} {axieParts[4]['name']}
            {getPartEmote(axieParts[5]['class'], axieParts[5]['type'])} {axieParts[5]['name']}
            ''',
            inline = True
        )

        embed.add_field(
            name = "D",
            value = f'''
            {getPartEmote(axieTraitsEyes['d']['class'], axieTraitsEyes['d']['type'])} {axieTraitsEyes['d']['name']}
            {getPartEmote(axieTraitsEars['d']['class'], axieTraitsEars['d']['type'])} {axieTraitsEars['d']['name']}
            {getPartEmote(axieTraitsMouth['d']['class'], axieTraitsMouth['d']['type'])} {axieTraitsMouth['d']['name']}
            {getPartEmote(axieTraitsHorn['d']['class'], axieTraitsHorn['d']['type'])} {axieTraitsHorn['d']['name']}
            {getPartEmote(axieTraitsBack['d']['class'], axieTraitsBack['d']['type'])} {axieTraitsBack['d']['name']}
            {getPartEmote(axieTraitsTail['d']['class'], axieTraitsTail['d']['type'])} {axieTraitsTail['d']['name']}
            ''',
            inline = True
        )

        embed.add_field(
            name = "R1",
            value = f'''
            {getPartEmote(axieTraitsEyes['r1']['class'], axieTraitsEyes['r1']['type'])} {axieTraitsEyes['r1']['name']}
            {getPartEmote(axieTraitsEars['r1']['class'], axieTraitsEars['r1']['type'])} {axieTraitsEars['r1']['name']}
            {getPartEmote(axieTraitsMouth['r1']['class'], axieTraitsMouth['r1']['type'])} {axieTraitsMouth['r1']['name']}
            {getPartEmote(axieTraitsHorn['r1']['class'], axieTraitsHorn['r1']['type'])} {axieTraitsHorn['r1']['name']}
            {getPartEmote(axieTraitsBack['r1']['class'], axieTraitsBack['r1']['type'])} {axieTraitsBack['r1']['name']}
            {getPartEmote(axieTraitsTail['r1']['class'], axieTraitsTail['r1']['type'])} {axieTraitsTail['r1']['name']}
            ''',
            inline = True
        )

        embed.add_field(
            name = "R2",
            value = f'''
            {getPartEmote(axieTraitsEyes['r2']['class'], axieTraitsEyes['r2']['type'])} {axieTraitsEyes['r2']['name']}
            {getPartEmote(axieTraitsEars['r2']['class'], axieTraitsEars['r2']['type'])} {axieTraitsEars['r2']['name']}
            {getPartEmote(axieTraitsMouth['r2']['class'], axieTraitsMouth['r2']['type'])} {axieTraitsMouth['r2']['name']}
            {getPartEmote(axieTraitsHorn['r2']['class'], axieTraitsHorn['r2']['type'])} {axieTraitsHorn['r2']['name']}
            {getPartEmote(axieTraitsBack['r2']['class'], axieTraitsBack['r2']['type'])} {axieTraitsBack['r2']['name']}
            {getPartEmote(axieTraitsTail['r2']['class'], axieTraitsTail['r2']['type'])} {axieTraitsTail['r2']['name']}
            ''',
            inline = True
        )

        embed.set_image(
            url = getAxieImageURL(axie)
        )
        await ctx.send(embed = embed)

def createCardEmbed(cardData, part, searched):

    # card filter by class and effect

    cardId = cardData['id']
    cardPartName = cardData['partName']
    cardSkillName = cardData['skillName']
    cardAttack = cardData['defaultAttack']
    cardDefense = cardData['defaultDefense']
    cardEnergy = cardData['defaultEnergy']
    cardType = cardData['expectType']
    cardIconId = cardData['iconId']
    cardTriggerColor = cardData['triggerColor']
    cardTriggerText = cardData['triggerText']
    cardDescription = cardData['description']

    partData = getPart(cardPartName)
    partEmote = partData['emote']
    partClass = partData['class']

    cardImageURL = f"{config.URL_CARD_IMAGES}{cardId}.png"

    # im = Image.open(requests.get(cardImageURL, stream=True).raw)
    # draw = ImageDraw.Draw(im)
    # font = ImageFont.truetype("ChangaOne-Regular.ttf", 20)
    # draw.text((85, 31),cardSkillName,(255,255,255),font=font)
    # draw.text((28, 26),str(cardEnergy),(255,255,255),font=font)
    # im.save(f"{cardSkillName}.png")

    embed = discord.Embed()

    if searched == "Skill":
        embed.title = f"{cardSkillName}"
    else:
        embed.title = f"{searched}: {part.title()} | {cardSkillName}"

    if partClass == 'Aquatic':
        partClass = '<:aquatic:881201528428429323> ' + partClass
        embed.color = 0x2de8f2
    elif partClass == 'Beast':
        partClass = '<:beast:881201528256491541> ' + partClass
        embed.color = 0xffec51
    elif partClass == 'Bird':
        partClass = '<:bird:881201528495562762> ' + partClass
        embed.color = 0xffb4bb
    elif partClass == 'Bug':
        partClass = '<:bug:881201528428458035> ' + partClass
        embed.color = 0xf74e4e
    elif partClass == 'Plant':
        partClass = '<:plant:881201528462008380> ' + partClass
        embed.color = 0xccef5e
    elif partClass == 'Reptile':
        partClass = '<:reptile:881201528571048017> ' + partClass
        embed.color = 0xef93ff

    if cardType == 'melee':
        typeEmote = '🗡'
    else:
        typeEmote = '🏹'

    embed.add_field(
        name = "Class",
        value = f"{partClass}",
        inline = False
    )
    
    embed.add_field(
        name = "Type",
        value = f"{typeEmote} {cardType.title()}",
        inline = True
    )

    iconEmote = iconDictionary(cardIconId)

    embed.add_field(
        name = "Effect",
        value = f"{iconEmote} {cardTriggerText}",
        inline = True
    )

    embed.add_field(
        name = "Description",
        value = f"**```{textwrap.fill(cardDescription, 30)}```**",
        inline = False
    )
    embed.add_field(
        name = "Energy",
        value = f"{energyEmote} {cardEnergy}",
        inline = True
    )
    embed.add_field(
        name = "Attack",
        value = f"{attackEmote} {cardAttack}",
        inline = True
    )
    embed.add_field(
        name = "Defense",
        value = f"{defenseEmote} {cardDefense}",
        inline = True
    )
    embed.add_field(
        name = "Part",
        value = f"{partEmote} {cardPartName}",
        inline = False
    )
    embed.set_image(url = cardImageURL)

    print("Fetch Success...")

    return embed

@bot.command(aliases=['c'])
async def card(ctx, *, card):

    if not isSkillSupported(card.lower()) and not isPartSupported(card.lower()):
        embed = discord.Embed(
            title = f"❌ Skill or Part '{card.title()}'' not found!",
            color = discord.Color.red()
        )
        embed.set_author(
            name = ctx.author.display_name,
            icon_url = ctx.author.avatar_url
        )
        await ctx.send(embed = embed)
        return

    print(f"\nFetching {card}\n")

    query = card
    card = card.lower()

    if card == 'scale dart':   
        searched = "Skill"
        cardData = getCard('aquatic-back-04')
        await ctx.send(embed = createCardEmbed(cardData, card, searched))
        cardData = getCard('reptile-tail-04')
        await ctx.send(embed = createCardEmbed(cardData, card, searched))
        return

    if card in skillDict.keys():
        card = skillDictionary(card)
        searched = "Skill"

    if card in partDict.keys():
        card = partDictionary(card)
        searched = "Part"

    cardData = getCard(card)

    # "id": "aquatic-back-02",
    # "partName": "Hermit",
    # "skillName": "Shelter",
    # "defaultAttack": 0,
    # "defaultDefense": 115,
    # "defaultEnergy": 1,
    # "expectType": "melee",
    # "iconId": "critical-block",
    # "triggerColor": "#ACBCBF",
    # "triggerText": "Critical Block",
    # "description": "Disable critical strikes on this Axie during this round."
    
    await ctx.send(embed = createCardEmbed(cardData, query, searched))
    # await ctx.send(file = discord.File(f"{cardSkillName}.png"))

@card.error
async def card_error(ctx, error):

    print(error)

    embed = discord.Embed(
        color = discord.Color.red()
    )

    embed.set_author(
        name = ctx.author.display_name,
        icon_url = ctx.author.avatar_url
    )

    if isinstance(error, commands.MissingRequiredArgument):
        embed.description = "❌ Invalid < skill | part> argument given. \n\nUsage:\n```c <skill | part>```"
        await ctx.send(embed = embed)
        # await ctx.send('Invalid <crypto> <currency> argument given')
        # await ctx.send('Usage: price <crypto> <currency>')
        return

@bot.command(aliases=['p'])
async def parts(ctx, classType, bodyPart = None):

    embed = discord.Embed(
        color = discord.Color.blue()
    )

    classType = classType.title()
    embed.title = f"Fetching {classType} Parts"

    if bodyPart != None:
        bodyPart = bodyPart.title()
        embed.title = f"Fetching {classType} {bodyPart} Parts"

    if classType in ['Aquatic', 'Beast', 'Bird', 'Bug', 'Plant', 'Reptile']:
        f = open('parts_dict.json')
        print("Opening parts_dict.json...")
        data = json.load(f)
        msg = ""
        if bodyPart != None:
            if bodyPart in ['Back', 'Horn', 'Tail', 'Mouth']:
                parts = ''
                for i in data[bodyPart]:
                    if data[bodyPart][i]['class'] == classType:
                        emote = data[bodyPart][i]['emote']
                        skillName = data[bodyPart][i]['skillName'] if 'skillName' in data[bodyPart][i] else ""
                        if skillName != "":
                            parts += f"{emote} **{i}**\n└─ {skillName}\n"
                        else:
                            parts += f"{emote} **{i}**\n"
                embed.add_field(
                    name = bodyPart,
                    value = parts,
                    inline = True
                )
        else:
            for index, val in enumerate(data):
                parts = ''
                # emote = getPartEmote(classType, val)
                # print(emote)
                embed.add_field(
                    name = f"{val}",
                    value = '',
                    inline = True
                ) 
                for j in data[val]:
                    if data[val][j]['class'] == classType:
                        msg += f"{j}\n"
                        emote = data[val][j]['emote']
                        skillName = data[val][j]['skillName'] if 'skillName' in data[val][j] else ""
                        if skillName != "":
                            parts += f"{emote} **{j}**\n└─ {skillName}\n"
                        else:
                            parts += f"{emote} **{j}**\n"
                embed.set_field_at(
                    index = index,
                    name = val,
                    value = parts,
                    inline = True
                )

    if classType == 'Aquatic':
        thumbnailURL = "https://cdn.discordapp.com/emojis/881201528428429323.png?v=1"
        embed.color = 0x2de8f2
    elif classType == 'Beast':
        thumbnailURL = "https://cdn.discordapp.com/emojis/881201528256491541.png?v=1"
        embed.color = 0xffec51
    elif classType == 'Bird':
        thumbnailURL = "https://cdn.discordapp.com/emojis/881201528495562762.png?v=1"
        embed.color = 0xffb4bb
    elif classType == 'Bug':
        thumbnailURL = "https://cdn.discordapp.com/emojis/881201528428458035.png?v=1"
        embed.color = 0xf74e4e
    elif classType == 'Plant':
        thumbnailURL = "https://cdn.discordapp.com/emojis/881201528462008380.png?v=1"
        embed.color = 0xccef5e
    elif classType == 'Reptile':
        thumbnailURL = "https://cdn.discordapp.com/emojis/881201528571048017.png?v=1"
        embed.color = 0xef93ff

    embed.set_thumbnail(
        url = thumbnailURL
    )

    return await ctx.send(embed = embed)

@bot.command
async def breed(ctx, axie1, axie2):
    return await ctx.send("Breed Test")

@bot.command(
    name = "info",
    alias = ["i"]
)
async def info(ctx):
    embed = discord.Embed(
        color = discord.Color.orange()
    )

    embed.add_field(
        name = "Version",
        value = "0.0.1",
        inline = False
    )

    embed.add_field(
        name = "Library",
        value = "[Discord.py](https://discordpy.readthedocs.io/en/stable/#)",
        inline = False
    )

    embed.add_field(
        name = "API",
        value = f"[Lunacia Proxy](https://api.lunaciaproxy.cloud/)\nAxie.Technology\n[Axie GraphQL](https://axie-graphql.web.app/getting-started/)\nAxie Google API",
        inline = False
    )

    embed.add_field(
        name = "Prefix",
        value = f"{prefix}",
        inline = False
    )

    embed.add_field(
        name = "Servers",
        value = len(bot.guilds),
        inline = False
    )

    embed.add_field(
        name = "Users",
        value = len(bot.users),
        inline = False
    )

    embed.add_field(
        name = "Developer",
        value = f"{dev}",
        inline = False
    )

    embed.add_field(
        name = "Invite",
        value = f"Bot is currently private\n\nIf you want the bot added to your server\n contact {dev}",
        inline = False
    )

    embed.set_author(
        name = bot.user.name,
        icon_url = bot.user.avatar_url
    )

    embed.set_footer(
        text = f"Prefix {prefix} | This bot is still under construction"
    )

    await ctx.send(embed = embed)

@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(
        color = discord.Color.red()
    )

    embed.set_author(
        name = ctx.author.display_name,
        icon_url = ctx.author.avatar_url
    )
    if isinstance(error, CommandNotFound):
        embed.description = f"❌ Invalid command \n\n**Help**\n`{prefix}help`\nShows list of commands."
        await ctx.send(embed = embed)
        # await ctx.send('Invalid <crypto> <currency> argument given')
        # await ctx.send('Usage: price <crypto> <currency>')
        return
    raise error

@bot.command()
async def laststand(ctx):
    await ctx.send(f"Last Stand formula: (Final blow damage - Remaining HP) < (Remaining HP x Morale / 100).")

cedId = "454964469752266762"

@bot.command()
async def cedrick(ctx):
    await ctx.send(f'<@!{cedId}> pangit')

@bot.command()
async def pangit(ctx):
    await ctx.send(f'ni <@!{cedId}>')

@bot.command()
async def servers(ctx):
  guilds = list(bot.guilds)
  await ctx.send('\n'.join(guild.name for guild in guilds))

bot.run(config.BOT_TOKEN)