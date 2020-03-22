import requests, json

res = requests.get('http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json')

id_dict = json.loads(res.text)

###
# In champion.json, the "data" key maps to a dictionary where each key* is the champion name and the value is a dictionary containing information about the champion. 
###

# x is the key* (champion name)
ids = list(map(lambda x: int(id_dict['data'][x]['key']), id_dict['data']))

idMap = dict(zip(ids, id_dict['data'].keys()))

jsFile = open('champions.js', 'w')
jsFile.write('const champions = ' + str(idMap) + ';\n')
jsFile.close()
