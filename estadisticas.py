

def jugador_mes_pes(enunciat,dict):
    print(enunciat)
    nom = ""
    pes_gran = 0.0
    player_num=""
    for player in dict:
        for clave, pes in dict[player].items():
            if "Pes" == clave and pes >= pes_gran:
                pes_gran = pes
                player_num= player
    nom = dict[player_num]["Nom"]
    print("El jugador amb més pes de la llista es", nom, "amb", pes_gran,"kg")

def jugador_menys_cm(enunciat,dict):
    print(enunciat)
    nom = ""
    cm_petit = 500.0
    player_num=""
    for player in dict:
        for clave, cm in dict[player].items():
            if "Alçada" == clave and cm <= cm_petit:
                cm_petit = cm
                player_num= player
    nom = dict[player_num]["Nom"]
    print("El jugador amb menys cm de la llista es", nom, "amb", cm_petit,"cm")


def estadisticas(dict,enunciats):
    jugador_mes_pes(enunciats[0],dict)
    jugador_menys_cm(enunciats[1], dict)