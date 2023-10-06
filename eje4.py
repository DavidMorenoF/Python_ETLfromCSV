def transformar_unidades_edad(dict):
    new_dict={}
    for i in dict:
        new_dict[i] = {}
        for j in dict[i]:
            if j == "Age" or j == "Edat":
                new_dict[i][j] = round(float(dict[i][j]))
            else:
                new_dict[i][j] = dict[i][j]
    
    return new_dict



