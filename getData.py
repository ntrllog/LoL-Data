import requests, json

PATCH_VERSION = '10.16.1'

res = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{PATCH_VERSION}/data/en_US/champion.json')

champions = json.loads(res.text)

champion_ids = list(map(lambda x: int(champions['data'][x]['key']), champions['data']))
names = list(map(lambda x: champions['data'][x]['name'], champions['data']))

res = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{PATCH_VERSION}/data/en_US/summoner.json')

spells = json.loads(res.text)

spell_ids = list(map(lambda x: int(spells['data'][x]['key']), spells['data']))
spell_image_urls = list(map(lambda x: spells['data'][x]['image']['full'], spells['data']))

jsFile = open('gameData.js', 'w')
jsFile.write('const idToChampNameMap = ' + str(dict(zip(champion_ids, names))) + ';\n')
jsFile.write('\nconst idToChampKeyMap = ' + str(dict(zip(champion_ids, champions['data'].keys()))) + ';\n')
jsFile.write('\nconst idToSpellImageUrlMap = ' + str(dict(zip(spell_ids, spell_image_urls))) + ';\n')
jsFile.close()
