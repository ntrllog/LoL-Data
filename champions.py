import requests, json

res = requests.get('http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json')

id_dict = json.loads(res.text)

ids = list(map(lambda x: int(id_dict['data'][x]['key']), id_dict['data']))
names = list(map(lambda x: id_dict['data'][x]['name'], id_dict['data']))

idMap = dict(zip(ids, names))

jsFile = open('champions.js', 'w')
jsFile.write('const idToChampNameMap = ' + str(idMap) + ';\n')
jsFile.write('\nconst idToChampKeyMap = ' + str(dict(zip(ids, id_dict['data'].keys()))) + ';\n')
jsFile.close()
