import csv
import eje1_p3, eje1_p4, eje1_p5, estadisticas_eje2, eje1_p1, eje1_p2
import pasarAJson_eje3

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

        
def main():
    print("Benvingut a NBA Data Advance.")
    player_english = players_read_english("basket_players.csv")
    capçelera_cambiada = eje1_p1.renombrar_capçelera(player_english, ["Nom", "Equip", "Posicio", "Alçada", "Pes", "Edat"])
    posicions_actualitzades= eje1_p2.cambiar_posicions(capçelera_cambiada)
    jugadors_amb_pes_altura = eje1_p3.transformar_unidades(posicions_actualitzades)
    jugadors_amb_edat = eje1_p4.transformar_unidades_edad(jugadors_amb_pes_altura)
    eje1_p5.cambiar_separador(jugadors_amb_edat, "jugadors_basket.csv")
    enunciats= [
        "Nom del jugador amb el pes més alt.",
        "Nom del jugador amb alçada més petita.",
        "Mitjana de pes i alçada de jugador per equip.",
        "Recompte de jugadors per posició.",
        "Distribució de jugadors per edat."
    ]
    estadisticas_eje2.estadisticas(jugadors_amb_edat, enunciats)
    pasarAJson_eje3.pasar_a_json("jugadors_basket.csv", "jugadors_basket.json")

try:
    main()
except NameError:
    print("Ha ocurrit un error:", NameError)