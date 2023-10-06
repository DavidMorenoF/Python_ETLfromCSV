import csv
import eje3, eje4, eje5, estadisticas
import pasarAJson

def players_read_english(path):
    try:
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
    except NameError:
        print("Ha ocurrit un error:", NameError)
    finally:
        csv_file.close()

def renombrar_capçelera(dict, nom_capçeleres):
    try:
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
    except NameError:
        print("Ha ocurrit un error:", NameError)

def cambiar_posicions(dict):
    try:
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
    except NameError:
        print("Ha ocurrit un error:", NameError)
        
def main():
    print("Benvingut a NBA Data Advance.")
    player_english = players_read_english("basket_players.csv")
    capçelera_cambiada = renombrar_capçelera(player_english, ["Nom", "Equip", "Posicio", "Alçada", "Pes", "Edat"])
    posicions_actualitzades= cambiar_posicions(capçelera_cambiada)
    jugadors_amb_pes_altura = eje3.transformar_unidades(posicions_actualitzades)
    jugadors_amb_edat = eje4.transformar_unidades_edad(jugadors_amb_pes_altura)
    eje5.cambiar_separador(jugadors_amb_edat, "jugadors_basket.csv")
    enunciats= [
        "Nom del jugador amb el pes més alt.",
        "Nom del jugador amb alçada més petita.",
        "Mitjana de pes i alçada de jugador per equip.",
        "Recompte de jugadors per posició.",
        "Distribució de jugadors per edat."
    ]
    estadisticas.estadisticas(jugadors_amb_edat, enunciats)
    pasarAJson.pasar_a_json("jugadors_basket.csv", "jugadors_basket.json")

try:
    main()
except NameError:
    print("Ha ocurrit un error:", NameError)