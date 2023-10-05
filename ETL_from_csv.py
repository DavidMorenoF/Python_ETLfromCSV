import csv

def players_read_english(path):
    with open(path) as csv_file:
        players = csv.reader(csv_file, delimiter= ";")
        line = 0
        categories = []
        contingut_players = {}
        for i in players:
            if line != 0:
                actual_player = "player" + str(line)
                contingut_players[actual_player]= {}
                for j in range(0,len(categories)):
                    contingut_players[actual_player][categories[j]] = i[j]
            else:
                categories = i
            line += 1
    return contingut_players

def renombrar_capçelera(dict, nom_capçeleres):
    new_dict={}
    list = []
    for i in dict:
        new_dict[i] = {}
        if len(list) == 0:
            for key in dict[i].keys():
                list.append(key)
        for j in range(0,len(nom_capçeleres)):
           new_dict[i][nom_capçeleres[j]] = dict[i][list[j]]
    
    return new_dict

def cambiar_posicions(dict):
    new_dict={}
    for i in dict:
        new_dict[i] = {}
        for j in dict[i]:
            if (j == "Posicio"):
                match dict[i][j]:
                    case "Point Guard":
                        new_dict[i][j]= "Base"
                    case "Shooting Guard":
                        new_dict[i][j]= "Escolta"
                    case "Small Forward":
                        new_dict[i][j]= "Aler"
                    case "Power Forward":
                        new_dict[i][j]= "Ala-Pivot"
                    case "Center":
                        new_dict[i][j]= "Pivot"
            else:
                new_dict[i][j] = dict[i][j]
    return new_dict

def main():
    player_english = players_read_english("basket_players.csv")
    capçelera_cambiada = renombrar_capçelera(player_english, ["Nom", "Equip", "Posicio", "Alçada", "Pes", "Edat"])
    posicions_actualitzades= cambiar_posicions(capçelera_cambiada)
    print(posicions_actualitzades)
main()