# LoL-Data

Objects/Dictionaries that make it easier to work with the [Riot Games API](https://developer.riotgames.com/)

Patch: `11.8.1`

Latest champion: `Gwen`

## Champion names for displaying

`{266: 'Aatrox', 103: 'Ahri', 84: 'Akali', 12: 'Alistar', 32: 'Amumu', 34: 'Anivia', 1: 'Annie', 523: 'Aphelios', 22: 'Ashe', 136: 'Aurelion Sol', 268: 'Azir', 432: 'Bard', 53: 'Blitzcrank', 63: 'Brand', 201: 'Braum', 51: 'Caitlyn', 164: 'Camille', 69: 'Cassiopeia', 31: "Cho'Gath", 42: 'Corki', 122: 'Darius', 131: 'Diana', 119: 'Draven', 36: 'Dr. Mundo', 245: 'Ekko', 60: 'Elise', 28: 'Evelynn', 81: 'Ezreal', 9: 'Fiddlesticks', 114: 'Fiora', 105: 'Fizz', 3: 'Galio', 41: 'Gangplank', 86: 'Garen', 150: 'Gnar', 79: 'Gragas', 104: 'Graves', 887: 'Gwen', 120: 'Hecarim', 74: 'Heimerdinger', 420: 'Illaoi', 39: 'Irelia', 427: 'Ivern', 40: 'Janna', 59: 'Jarvan IV', 24: 'Jax', 126: 'Jayce', 202: 'Jhin', 222: 'Jinx', 145: "Kai'Sa", 429: 'Kalista', 43: 'Karma', 30: 'Karthus', 38: 'Kassadin', 55: 'Katarina', 10: 'Kayle', 141: 'Kayn', 85: 'Kennen', 121: "Kha'Zix", 203: 'Kindred', 240: 'Kled', 96: "Kog'Maw", 7: 'LeBlanc', 64: 'Lee Sin', 89: 'Leona', 876: 'Lillia', 127: 'Lissandra', 236: 'Lucian', 117: 'Lulu', 99: 'Lux', 54: 'Malphite', 90: 'Malzahar', 57: 'Maokai', 11: 'Master Yi', 21: 'Miss Fortune', 62: 'Wukong', 82: 'Mordekaiser', 25: 'Morgana', 267: 'Nami', 75: 'Nasus', 111: 'Nautilus', 518: 'Neeko', 76: 'Nidalee', 56: 'Nocturne', 20: 'Nunu & Willump', 2: 'Olaf', 61: 'Orianna', 516: 'Ornn', 80: 'Pantheon', 78: 'Poppy', 555: 'Pyke', 246: 'Qiyana', 133: 'Quinn', 497: 'Rakan', 33: 'Rammus', 421: "Rek'Sai", 526: 'Rell', 58: 'Renekton', 107: 'Rengar', 92: 'Riven', 68: 'Rumble', 13: 'Ryze', 360: 'Samira', 113: 'Sejuani', 235: 'Senna', 147: 'Seraphine', 875: 'Sett', 35: 'Shaco', 98: 'Shen', 102: 'Shyvana', 27: 'Singed', 14: 'Sion', 15: 'Sivir', 72: 'Skarner', 37: 'Sona', 16: 'Soraka', 50: 'Swain', 517: 'Sylas', 134: 'Syndra', 223: 'Tahm Kench', 163: 'Taliyah', 91: 'Talon', 44: 'Taric', 17: 'Teemo', 412: 'Thresh', 18: 'Tristana', 48: 'Trundle', 23: 'Tryndamere', 4: 'Twisted Fate', 29: 'Twitch', 77: 'Udyr', 6: 'Urgot', 110: 'Varus', 67: 'Vayne', 45: 'Veigar', 161: "Vel'Koz", 254: 'Vi', 234: 'Viego', 112: 'Viktor', 8: 'Vladimir', 106: 'Volibear', 19: 'Warwick', 498: 'Xayah', 101: 'Xerath', 5: 'Xin Zhao', 157: 'Yasuo', 777: 'Yone', 83: 'Yorick', 350: 'Yuumi', 154: 'Zac', 238: 'Zed', 115: 'Ziggs', 26: 'Zilean', 142: 'Zoe', 143: 'Zyra'}`

## Champion names for making requests to Data Dragon

`{266: 'Aatrox', 103: 'Ahri', 84: 'Akali', 12: 'Alistar', 32: 'Amumu', 34: 'Anivia', 1: 'Annie', 523: 'Aphelios', 22: 'Ashe', 136: 'AurelionSol', 268: 'Azir', 432: 'Bard', 53: 'Blitzcrank', 63: 'Brand', 201: 'Braum', 51: 'Caitlyn', 164: 'Camille', 69: 'Cassiopeia', 31: 'Chogath', 42: 'Corki', 122: 'Darius', 131: 'Diana', 119: 'Draven', 36: 'DrMundo', 245: 'Ekko', 60: 'Elise', 28: 'Evelynn', 81: 'Ezreal', 9: 'Fiddlesticks', 114: 'Fiora', 105: 'Fizz', 3: 'Galio', 41: 'Gangplank', 86: 'Garen', 150: 'Gnar', 79: 'Gragas', 104: 'Graves', 887: 'Gwen', 120: 'Hecarim', 74: 'Heimerdinger', 420: 'Illaoi', 39: 'Irelia', 427: 'Ivern', 40: 'Janna', 59: 'JarvanIV', 24: 'Jax', 126: 'Jayce', 202: 'Jhin', 222: 'Jinx', 145: 'Kaisa', 429: 'Kalista', 43: 'Karma', 30: 'Karthus', 38: 'Kassadin', 55: 'Katarina', 10: 'Kayle', 141: 'Kayn', 85: 'Kennen', 121: 'Khazix', 203: 'Kindred', 240: 'Kled', 96: 'KogMaw', 7: 'Leblanc', 64: 'LeeSin', 89: 'Leona', 876: 'Lillia', 127: 'Lissandra', 236: 'Lucian', 117: 'Lulu', 99: 'Lux', 54: 'Malphite', 90: 'Malzahar', 57: 'Maokai', 11: 'MasterYi', 21: 'MissFortune', 62: 'MonkeyKing', 82: 'Mordekaiser', 25: 'Morgana', 267: 'Nami', 75: 'Nasus', 111: 'Nautilus', 518: 'Neeko', 76: 'Nidalee', 56: 'Nocturne', 20: 'Nunu', 2: 'Olaf', 61: 'Orianna', 516: 'Ornn', 80: 'Pantheon', 78: 'Poppy', 555: 'Pyke', 246: 'Qiyana', 133: 'Quinn', 497: 'Rakan', 33: 'Rammus', 421: 'RekSai', 526: 'Rell', 58: 'Renekton', 107: 'Rengar', 92: 'Riven', 68: 'Rumble', 13: 'Ryze', 360: 'Samira', 113: 'Sejuani', 235: 'Senna', 147: 'Seraphine', 875: 'Sett', 35: 'Shaco', 98: 'Shen', 102: 'Shyvana', 27: 'Singed', 14: 'Sion', 15: 'Sivir', 72: 'Skarner', 37: 'Sona', 16: 'Soraka', 50: 'Swain', 517: 'Sylas', 134: 'Syndra', 223: 'TahmKench', 163: 'Taliyah', 91: 'Talon', 44: 'Taric', 17: 'Teemo', 412: 'Thresh', 18: 'Tristana', 48: 'Trundle', 23: 'Tryndamere', 4: 'TwistedFate', 29: 'Twitch', 77: 'Udyr', 6: 'Urgot', 110: 'Varus', 67: 'Vayne', 45: 'Veigar', 161: 'Velkoz', 254: 'Vi', 234: 'Viego', 112: 'Viktor', 8: 'Vladimir', 106: 'Volibear', 19: 'Warwick', 498: 'Xayah', 101: 'Xerath', 5: 'XinZhao', 157: 'Yasuo', 777: 'Yone', 83: 'Yorick', 350: 'Yuumi', 154: 'Zac', 238: 'Zed', 115: 'Ziggs', 26: 'Zilean', 142: 'Zoe', 143: 'Zyra'}`

## Image urls for summoner spells

`{21: 'SummonerBarrier.png', 1: 'SummonerBoost.png', 14: 'SummonerDot.png', 3: 'SummonerExhaust.png', 4: 'SummonerFlash.png', 6: 'SummonerHaste.png', 7: 'SummonerHeal.png', 13: 'SummonerMana.png', 30: 'SummonerPoroRecall.png', 31: 'SummonerPoroThrow.png', 11: 'SummonerSmite.png', 39: 'SummonerSnowURFSnowball_Mark.png', 32: 'SummonerSnowball.png', 12: 'SummonerTeleport.png'}`

## Image urls for runes [(local images only)](https://developer.riotgames.com/docs/lol#data-dragon)

`{8100: 'Domination', 8300: 'Inspiration', 8000: 'Precision', 8400: 'Resolve', 8200: 'Sorcery'}`

`{8112: 'Electrocute', 8124: 'Predator', 8128: 'DarkHarvest', 9923: 'HailOfBlades', 8351: 'GlacialAugment', 8360: 'UnsealedSpellbook', 8358: 'MasterKey', 8005: 'PressTheAttack', 8008: 'LethalTempo', 8021: 'FleetFootwork', 8010: 'Conqueror', 8437: 'GraspOfTheUndying', 8439: 'Aftershock', 8465: 'Guardian', 8214: 'SummonAery', 8229: 'ArcaneComet', 8230: 'PhaseRush'}`
