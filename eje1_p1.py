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