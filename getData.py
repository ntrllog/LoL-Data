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

with open('runesReforged.json') as f:
    runes = json.load(f)

rune_path_ids = list(map(lambda x: x['id'], runes))
rune_path_names = list(map(lambda x: x['key'], runes))

keystone_ids = []
keystone_names = []

for rune_path in runes:
    for keystone in rune_path['slots'][0]['runes']:
        keystone_ids.append(keystone['id'])
        keystone_names.append(keystone['key'])

with open('gameData.js', 'w') as jsFile:
    jsFile.write('const idToChampNameMap = ' + str(dict(zip(champion_ids, names))) + ';\n')
    jsFile.write('\nconst idToChampKeyMap = ' + str(dict(zip(champion_ids, champions['data'].keys()))) + ';\n')
    jsFile.write('\nconst idToSpellImageUrlMap = ' + str(dict(zip(spell_ids, spell_image_urls))) + ';\n')
    jsFile.write('\nconst idToRunePathNameMap = ' + str(dict(zip(rune_path_ids, rune_path_names))) + ';\n')
    jsFile.write('\nconst idToKeystoneNameMap = ' + str(dict(zip(keystone_ids, keystone_names))) + ';\n')
