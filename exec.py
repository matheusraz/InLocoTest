import json

def newData(n):
    return {
        'game_{}'.format(n): {
            'total_kills': 0,
            'players': [],
            'kills': {
            }
        }
    }

def navega(line,arqLines,data,nGame,oneGameCurrently):
    print(line)
    if(line == len(arqLines) -1):
        allGames.append(data)
        print(allGames)
        
    if('InitGame' in arqLines[line] and not oneGameCurrently):
        print('COMECEI UM JOGO')
        oneGameCurrently = True
        navega(line+1,arqLines,data,nGame,oneGameCurrently)
    
    elif('InitGame' in arqLines[line] and oneGameCurrently):
        print('TERMINEI UM E VOU COMEÇAR OUTRO!')
        print(allGames)
        # print(data)
        allGames.append(data)
        nGame += 1
        data = newData(nGame)
        navega(line+1,arqLines,data,nGame,oneGameCurrently)
    
    if('ClientUserinfoChanged' in arqLines[line]):
        if(arqLines[line].split('\\')[1] not in data['game_{}'.format(nGame)]['players']):
            data['game_{}'.format(nGame)]['players'].append(arqLines[line].split('\\')[1])
        navega(line+1,arqLines,data,nGame,oneGameCurrently)
    
    elif(arqLines[line].split()[1] == 'Kill:'):
        try:
            if(arqLines[line].split()[5] != '<world>'):
                data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[5]] += 1
            data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[7]] -= 1
            data['game_{}'.format(nGame)]['total_kills'] += 1
            navega(line+1,arqLines,data,nGame,oneGameCurrently)
        except:
            if(arqLines[line].split()[5] != '<world>'):
                data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[5]] = 1
            data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[7]] = -1
            navega(line+1,arqLines,data,nGame,oneGameCurrently)
    else:
        navega(line+1,arqLines,data,nGame,oneGameCurrently)


arq = open('games.log','r')

arqLines = arq.readlines()

nGame = 1
allGames = []
oneGameCurrently = False
data = newData(1)

for line in range(len(arqLines)):

    if('InitGame' in arqLines[line] and not oneGameCurrently):
        print('COMECEI UM JOGO')
        oneGameCurrently = True
    
    elif('InitGame' in arqLines[line] and oneGameCurrently):
        allGames.append(data)
        nGame += 1
        data = newData(nGame)
    
    if('ClientUserinfoChanged' in arqLines[line]):
        if(arqLines[line].split('\\')[1] not in data['game_{}'.format(nGame)]['players']):
            data['game_{}'.format(nGame)]['players'].append(arqLines[line].split('\\')[1])
    
    elif(arqLines[line].split()[1] == 'Kill:'):
        try:
            if(arqLines[line].split()[5] != '<world>'):
                data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[5]] += 1
            data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[7]] -= 1
            data['game_{}'.format(nGame)]['total_kills'] += 1
        except:
            if(arqLines[line].split()[5] != '<world>'):
                data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[5]] = 1
            data['game_{}'.format(nGame)]['kills'][arqLines[line].split()[7]] = -1

allGames.append(data)

print(allGames)

# print(arqLines)
        
# navega(0,arqLines,data,nGame,oneGameCurrently)

# print(arqLines[39].split())

# print(arqLines[35].split('\\')[1])

# print(arqLines[31].split()[1] == 'Kill:')

# print(data['game_1']['kills']['Isgalamido'])