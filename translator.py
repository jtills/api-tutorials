import requests
import time

print("Here are our languages: \nShakespeare\nYoda\nPirate\nMorse\nBrooklyn\nChef\nVulcan\nKlingon\nPig Latin")
language = input('\nWhat language to be translated to: ')
text = input('\nWrite text to be translated: ')


text = text.split(' ')

url = "https://api.funtranslations.com/translate/{}.json?text=".format(language)

for word in text:
    url = url +  word + '%20'

data = requests.get(url).json()

print(data['contents']['translated'])
time.sleep(60)
