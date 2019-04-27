import json
import sys
import urllib.request


def newData(n):
    return {
        'game_{}'.format(n): {
            'total_kills': 0,
            'players': [],
            'kills': {
            }
        }
    }

url = sys.argv[1]

print(url)

# for line in urllib.request.urlopen(url):

arq = open('games.log','r')

arqLines = arq.readlines()

nGame = 1
allGames = []
oneGameCurrently = False
data = newData(1)

# for line in urllib.request.urlopen(url):
#     print(line)
for line in urllib.request.urlopen(url).readlines():
    
    line = line.decode("utf-8")

    if('InitGame' in line and not oneGameCurrently):
        print('COMECEI UM JOGO')
        oneGameCurrently = True
    
    elif('InitGame' in line and oneGameCurrently):
        allGames.append(data)
        nGame += 1
        data = newData(nGame)
    
    if('ClientUserinfoChanged' in line):
        if(line.split('\\')[1] not in data['game_{}'.format(nGame)]['players']):
            data['game_{}'.format(nGame)]['players'].append(line.split('\\')[1])
    
    elif(line.split()[1] == 'Kill:'):
        try:
            if(line.split()[5] != '<world>'):
                data['game_{}'.format(nGame)]['kills'][line.split()[5]] += 1
            data['game_{}'.format(nGame)]['kills'][line.split()[7]] -= 1
            data['game_{}'.format(nGame)]['total_kills'] += 1
        except:
            if(line.split()[5] != '<world>'):
                data['game_{}'.format(nGame)]['kills'][line.split()[5]] = 1
            data['game_{}'.format(nGame)]['kills'][line.split()[7]] = -1

allGames.append(data)

print(allGames)


# print(arqLines)
        
# navega(0,arqLines,data,nGame,oneGameCurrently)

# print(arqLines[39].split())

# print(arqLines[35].split('\\')[1])

# print(arqLines[31].split()[1] == 'Kill:')

# print(data['game_1']['kills']['Isgalamido'])