

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

def mitjana_pes_alçada_equips(enunciat, dict):
    print(enunciat)
    new_dict={}
    for player in dict:
        actual_equip= ""
        for clave, values in dict[player].items():
            if "Equip" == clave and values not in new_dict.keys():
                new_dict[values]= {"Pes": [], "Alçada": []}
                actual_equip = values
            if "Equip" == clave:
                actual_equip = values
            elif "Pes" == clave:
                new_dict[actual_equip]["Pes"].append(values)
            elif "Alçada" == clave:
                new_dict[actual_equip]["Alçada"].append(values)

    for equip in new_dict:
        for clave, values in new_dict[equip].items():
            if "Pes" == clave:
                pes = 0.0
                for valors in values:
                    pes += valors
                pes = pes / (len(values) + 1)
                print("La mitjana de pes de l'equip", equip, "es",round(pes,2),"kg")
            elif "Alçada" == clave:
                alçada = 0.0
                for valors in values:
                    alçada += valors
                alçada = alçada / (len(values) + 1)
                print("La mitjana de cm de l'equip", equip, "es",round(alçada,2),"cm")

def jugadors_posicio(enunciat, dict):
    print(enunciat)
    new_dict= {}
    for player in dict:
        actual_nom =""
        for clave, values in dict[player].items():
            if "Posicio" == clave and values not in new_dict.keys():
                new_dict[values]= {"Noms": []}
                new_dict[values]["Noms"].append(actual_nom)
            if "Posicio" == clave:
                new_dict[values]["Noms"].append(actual_nom)
            elif "Nom" == clave:
                actual_nom = values
    for posicio in new_dict:
        for clave, values in new_dict[posicio].items():
            print("Jugadors que juguen com",posicio,":")
            for valors in values:
                print(valors)

def jugadors_edat(enunciat, dict):
    print(enunciat)
    new_dict= {}
    for player in dict:
        actual_nom =""
        for clave, values in dict[player].items():
            if "Edat" == clave and values not in new_dict.keys():
                new_dict[values]= {"Noms": []}
                new_dict[values]["Noms"].append(actual_nom)
            if "Edat" == clave:
                new_dict[values]["Noms"].append(actual_nom)
            elif "Nom" == clave:
                actual_nom = values
    new_dict_keys = sorted(new_dict)
    for edat in new_dict_keys:
        for clave, values in new_dict[edat].items():
            print("Jugadors amb",edat,"anys:")
            for valors in values:
                print(valors)
        

def estadisticas(dict,enunciats):
    try:
        jugador_mes_pes(enunciats[0],dict)
        jugador_menys_cm(enunciats[1], dict)
        mitjana_pes_alçada_equips(enunciats[2], dict)
        jugadors_posicio(enunciats[3], dict)
        jugadors_edat(enunciats[4], dict)
    except NameError:
        print("Ha ocurrit un error:", NameError)