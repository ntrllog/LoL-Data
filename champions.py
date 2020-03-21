import requests, json

res = requests.get('http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json')

id_dict = json.loads(res.text)

ids = list(map(lambda x: id_dict['data'][x]['key'], id_dict['data']))

idMap = dict(zip(ids, id_dict['data'].keys()))

jsFile = open('champions.js', 'w')
jsFile.write('const champions = ' + str(idMap) + ';\n\n export default champions;')
jsFile.close()
