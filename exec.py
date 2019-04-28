import json
import sys
import urllib.request


def test_parser():
    value = [{'game_1': {'total_kills': 0, 'players': ['Isgalamido'], 'kills': {}}}, {'game_2': {'total_kills': 11, 'players': ['Isgalamido', 'Dono da Bola', 'Mocinha'], 'kills': {'Isgalamido': -5}}}, {'game_3': {'total_kills': 4, 'players': ['Dono da Bola', 'Mocinha', 'Isgalamido', 'Zeh'], 'kills': {'Isgalamido': 1, 'Zeh': -2, 'Dono da Bola': -1}}}, {'game_4': {'total_kills': 105, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Assasinu Credi'], 'kills': {'Isgalamido': 19, 'Dono da Bola': 13, 'Zeh': 20, 'Assasinu Credi': 13}}}, {'game_5': {'total_kills': 14, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Assasinu Credi'], 'kills': {'Isgalamido': 2, 'Assasinu Credi': 1, 'Zeh': 1}}}, {'game_6': {'total_kills': 29, 'players': ['Fasano Again', 'Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'UnnamedPlayer', 'Maluquinho', 'Assasinu Credi', 'Mal'], 'kills': {'Oootsimo': 8, 'Isgalamido': 3, 'Zeh': 7, 'Dono da Bola': 2, 'Maluquinho': 0, 'Assasinu Credi': 1}}}, {'game_7': {'total_kills': 130, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi', 'Chessus!', 'Chessus'], 'kills': {'Zeh': 9, 'Dono da Bola': 12, 'Assasinu Credi': 22, 'Oootsimo': 20, 'Mal': -3, 'Isgalamido': 16}}}, {'game_8': {'total_kills': 89, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi'], 'kills': {'Oootsimo': 16, 'Isgalamido': 20, 'Assasinu Credi': 10, 'Zeh': 12, 'Dono da Bola': 3, 'Mal': -2}}}, {'game_9': {'total_kills': 67, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi', 'Chessus!', 'Chessus'], 'kills': {'Assasinu Credi': 10, 'Oootsimo': 9, 'Mal': 3, 'Dono da Bola': 2, 'Zeh': 12, 'Isgalamido': 1, 'Chessus': 8}}}, {'game_10': {'total_kills': 60, 'players': ['Oootsimo', 'Dono da Bola', 'Zeh', 'Chessus', 'Mal', 'Assasinu Credi', 'Isgalamido'], 'kills': {'Mal': 1, 'Assasinu Credi': 3, 'Dono da Bola': 3, 'Chessus': 5, 'Zeh': 7, 'Oootsimo': -1, 'Isgalamido': 6}}}, {'game_11': {'total_kills': 20, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'UnnamedPlayer', 'Mal'], 'kills': {'Dono da Bola': -2, 'Isgalamido': 5, 'Oootsimo': 4, 'Assasinu Credi': -3}}}, {'game_12': {'total_kills': 160, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Dono da Bola': 3, 'Assasinu Credi': 20, 'Mal': -6, 'Zeh': 13, 'Chessus': 13, 'Isgalamido': 26, 'Oootsimo': 13}}}, {'game_13': {'total_kills': 6, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Isgalamido': -1, 'Oootsimo': 2, 'Dono da Bola': -1, 'Zeh': 2}}}, {'game_14': {'total_kills': 122, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Isgalamido': 22, 'Chessus': 7, 'Mal': -2, 'Oootsimo': 9, 'Assasinu Credi': 7,'Dono da Bola': 2, 'Zeh': 5}}}, {'game_15': {'total_kills': 3, 'players': ['Zeh', 'Assasinu Credi', 'Dono da Bola', 'Fasano Again', 'Isgalamido', 'Oootsimo'], 'kills': {'Zeh': -3}}}, {'game_16': {'total_kills': 0, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh'], 'kills': {}}}, {'game_17': {'total_kills': 13, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh', 'UnnamedPlayer', 'Mal'], 'kills': {'Dono da Bola': -2, 'Zeh': 0, 'Assasinu Credi': -3, 'Oootsimo': 1, 'Isgalamido': 0, 'Mal': -1}}}, {'game_18': {'total_kills': 7, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Zeh': 2, 'Isgalamido': 1, 'Assasinu Credi': 2, 'Dono da Bola': -1, 'Mal': -1}}}, {'game_19': {'total_kills': 95, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Mal': 2, 'Zeh': 20, 'Isgalamido': 14, 'Oootsimo': 10, 'Dono da Bola': 14, 'Assasinu Credi': 9}}}, {'game_20': {'total_kills': 3, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Dono da Bola': 2, 'Oootsimo': 1}}}, {'game_21': {'total_kills': 131, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Dono da Bola': 14, 'Zeh': 19, 'Mal': 6, 'Isgalamido': 17, 'Assasinu Credi': 19, 'Oootsimo': 22}}}]
    valueReceived = mainFunc()
    print("\n\nprimeiro!!!!!\n\n")
    print(value)
    print("\n\nsegundo!!!!!\n\n")
    print(valueReceived)
    assert valueReceived == value, "Should be well parsed"


def newData(n):
    return {
        "game_{}".format(n): {
            "total_kills": 0,
            "players": [],
            "kills": {
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

    nGame = 1
    allGames = []
    oneGameCurrently = False
    data = newData(1)

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
            if(line.split('\\')[1] not in data["game_{}".format(nGame)]["players"]):
                data["game_{}".format(nGame)]["players"].append(
                    line.split('\\')[1])

        elif("Kill:" in line):
            try:
                separate = line.split("killed")
                matou = separate[0].split(":")
                morto = separate[1].split("by")
                if(matou[len(matou)-1].strip() != "<world>"):
                    data["game_{}".format(
                        nGame)]["kills"][matou[len(matou)-1].strip()] += 1
                else:
                    data["game_{}".format(nGame)]["kills"][morto[0].strip()] -= 1
                data["game_{}".format(nGame)]["total_kills"] += 1
            except:
                if(line.split()[5] != "<world>"):
                    data["game_{}".format(nGame)]["kills"][matou[len(matou)-1].strip()] = 1
                else:
                    data["game_{}".format(nGame)]["kills"][morto[0].strip()] = -1
                data["game_{}".format(nGame)]["total_kills"] += 1

    allGames.append(data)
    if(isFromInternet):
        print(allGames)
    
    return allGames


if __name__ == "__main__":
    if(sys.argv[2] == "test"):
        test_parser()
        print("Everything passed")
    else:
        mainFunc(sys.argv[1])
    # arq = open('games.log','r')
    # arqLines = arq.readlines()
    # separate = arqLines[4741].split('killed')
    # matou = separate[0].split(':')
    # print(matou)
    # morto = separate[1].split('by')
    # print(morto)

# print(arqLines)

# navega(0,arqLines,data,nGame,oneGameCurrently)

# print(arqLines[39].split())

# print(arqLines[35].split('\\')[1])

# print(arqLines[31].split()[1] == 'Kill:')

# print(data['game_1']['kills']['Isgalamido'])
