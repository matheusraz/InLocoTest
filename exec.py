import json
import sys
import urllib.request


def test_parser():
    value = [{'game_1': {'total_kills': 0, 'players': ['Isgalamido'], 'kills': {}}}, {'game_2': {'total_kills': 9, 'players': ['Isgalamido', 'Dono da Bola', 'Mocinha'], 'kills': {'Isgalamido': -4, 'Mocinha': -1}}}, {'game_3': {'total_kills': 1, 'players': ['Dono da Bola', 'Mocinha', 'Isgalamido', 'Zeh'], 'kills': {'Isgalamido': 1, 'Mocinha': -1, 'Zeh': -2, 'Dono': -1}}}, {'game_4': {'total_kills': 99, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Assasinu Credi'], 'kills': {'Isgalamido': 13, 'Dono': -2, 'Bola': -20, 'Zeh': 12, 'Assasinu': 3, 'killed': -16}}}, {'game_5': {'total_kills': 10, 'players':['Dono da Bola', 'Isgalamido', 'Zeh', 'Assasinu Credi'], 'kills': {'Isgalamido': 1, 'Zeh': 0, 'Dono': -1, 'Assasinu': 1, 'killed': -5}}}, {'game_6': {'total_kills': 20, 'players': ['Fasano Again', 'Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'UnnamedPlayer', 'Maluquinho', 'Assasinu Credi', 'Mal'], 'kills': {'Oootsimo': 6, 'Zeh': 2, 'Isgalamido': -2, 'UnnamedPlayer': -1, 'Dono': -1, 'Bola': -2, 'Maluquinho': 0, 'Assasinu': -1, 'killed': -1, 'Mal': -2}}}, {'game_7': {'total_kills': 123, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi', 'Chessus!', 'Chessus'], 'kills': {'Zeh': -3, 'Dono': -5, 'Assasinu': 8, 'killed': -22, 'Bola': -14, 'Oootsimo': 10, 'Mal': -12, 'Isgalamido': 9, 'Chessus': -2}}}, {'game_8': {'total_kills': 84, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi'], 'kills': {'Oootsimo': 5, 'Isgalamido': 14, 'Zeh': 5, 'Assasinu': -3, 'killed': -12, 'Dono': -8, 'Bola': -5, 'Mal': -11}}}, {'game_9': {'total_kills': 60, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi', 'Chessus!', 'Chessus'], 'kills': {'Assasinu': 2, 'Oootsimo': -2, 'Zeh': -1, 'Mal': -5, 'Dono': 0, 'Bola': -3, 'Isgalamido': -1, 'killed': -11, 'Chessus': 6}}}, {'game_10': {'total_kills': 54, 'players': ['Oootsimo', 'Dono da Bola', 'Zeh', 'Chessus', 'Mal', 'Assasinu Credi', 'Isgalamido'], 'kills': {'Mal': -7, 'Oootsimo': -6, 'Assasinu':-2, 'killed': -5, 'Dono': 1, 'Bola': -5, 'Chessus': 0, 'Zeh': 5, 'Isgalamido': -2}}}, {'game_11': {'total_kills': 13, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'UnnamedPlayer', 'Mal'], 'kills': {'Dono': 0, 'Isgalamido': 1, 'Oootsimo': 4, 'Assasinu': -4, 'Chessus': -3, 'Bola': -1, 'Zeh': -2, 'Mal': -1}}}, {'game_12': {'total_kills': 153, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Dono': -8, 'Assasinu': 6, 'killed': -23, 'Mal': -15, 'Zeh': 7, 'Chessus': 8, 'Isgalamido': 5, 'Oootsimo': 4, 'Bola': -11}}}, {'game_13': {'total_kills': 2, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Isgalamido': -1, 'Oootsimo': 1, 'Assasinu': -1, 'Dono': -2, 'Zeh': 2}}}, {'game_14': {'total_kills': 116, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Isgalamido': 12, 'Zeh': -4, 'Chessus': -2, 'Dono': -13, 'Mal': -8, 'Oootsimo': 4, 'Assasinu': -3, 'killed': -12, 'Bola': -9}}}, {'game_15': {'total_kills': 2, 'players': ['Zeh', 'Assasinu Credi', 'Dono da Bola', 'Fasano Again', 'Isgalamido', 'Oootsimo'], 'kills': {'Zeh': -3}}}, {'game_16': {'total_kills': 0, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh'], 'kills': {}}}, {'game_17': {'total_kills': 7, 'players': ['Dono da Bola','Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh', 'UnnamedPlayer', 'Mal'], 'kills': {'Dono': -2, 'Zeh': -1, 'Assasinu': -4, 'Oootsimo': -1, 'Isgalamido': 0, 'Mal': -1}}}, {'game_18': {'total_kills': 2, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Zeh': 1, 'Assasinu': 2, 'Isgalamido': 1, 'Mal': -2, 'killed': -2, 'Dono': -1}}}, {'game_19': {'total_kills': 89, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Mal': -8, 'Zeh': 8, 'Dono': 5, 'Isgalamido': 6, 'Assasinu': 1, 'Oootsimo': 4, 'Bola': -15, 'killed': -12}}}, {'game_20': {'total_kills': 1, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Dono': 2, 'Bola': -2, 'Oootsimo': 1, 'Assasinu': -1}}}, {'game_21': {'total_kills': 126, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Dono': 0, 'Bola': -16,'Zeh': 7, 'Oootsimo': 14, 'Mal': -6, 'Isgalamido': 6, 'Assasinu': -1, 'killed': -22}}}]
    valueReceived = mainFunc()
    print('primeiro!!!!!!!\n\n')
    print(valueReceived)
    print('\n\nsegundo!!!!!!!!\n\n')
    print(value)
    assert valueReceived == value, "Should be well parsed"


def newData(n):
    return {
        'game_{}'.format(n): {
            'total_kills': 0,
            'players': [],
            'kills': {
            }
        }
    }


def mainFunc(url = None):

    isFromInternet = False

    if(url == None):
        print("VIM LOCAL (TEST)")
        arq = open('games.log','r')
    else:
        print("VIM DA INTERNET")
        isFromInternet = True
        arq = urllib.request.urlopen(url)

    url = sys.argv[1]

    print(url)

    # for line in urllib.request.urlopen(url):


    # arqLines = arq.readlines()

    nGame = 1
    allGames = []
    oneGameCurrently = False
    data = newData(1)

    # for line in urllib.request.urlopen(url):
    #     print(line)
    for line in arq.readlines():

        if(isFromInternet):
            line = line.decode("utf-8")

        if('InitGame' in line and not oneGameCurrently):
            oneGameCurrently = True

        elif('InitGame' in line and oneGameCurrently):
            allGames.append(data)
            nGame += 1
            data = newData(nGame)

        if('ClientUserinfoChanged' in line):
            if(line.split('\\')[1] not in data['game_{}'.format(nGame)]['players']):
                data['game_{}'.format(nGame)]['players'].append(
                    line.split('\\')[1])

        elif(line.split()[1] == 'Kill:'):
            try:
                separate = line.split('killed')
                matou = separate[0].split(':')
                print(matou)
                morto = separate[1].split('by')
                print(morto)
                if(matou[len(matou)-1] != '<world>'):
                    data['game_{}'.format(
                        nGame)]['kills'][matou[len(matou)-1]] += 1
                data['game_{}'.format(nGame)]['kills'][morto[0]] -= 1
                data['game_{}'.format(nGame)]['total_kills'] += 1
            except:
                if(line.split()[5] != '<world>'):
                    data['game_{}'.format(nGame)]['kills'][matou[len(matou)-1]] = 1
                data['game_{}'.format(nGame)]['kills'][morto[0]] = -1

    allGames.append(data)
    if(isFromInternet):
        print(allGames)
    
    print(allGames)
    return allGames


if __name__ == "__main__":
    # if(sys.argv[2] == 'test'):
    #     test_parser()
    #     print("Everything passed")
    # else:
    #     mainFunc(sys.argv[1])
    arq = open('games.log','r')
    arqLines = arq.readlines()
    separate = arqLines[4741].split('killed')
    matou = separate[0].split(':')
    print(matou)
    morto = separate[1].split('by')
    print(morto)

# print(arqLines)

# navega(0,arqLines,data,nGame,oneGameCurrently)

# print(arqLines[39].split())

# print(arqLines[35].split('\\')[1])

# print(arqLines[31].split()[1] == 'Kill:')

# print(data['game_1']['kills']['Isgalamido'])
