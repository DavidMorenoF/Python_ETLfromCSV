def transformar_unidades(dict):
    new_dict={}
    pol_cent = 2.54
    pou_kgs = 0.45
    for i in dict:
        new_dict[i] = {}
        for j in dict[i]:
            if j == "Heigth" or j == "Alçada":
                new_dict[i][j] = round(float(dict[i][j]) * pol_cent, 2)
            elif j == "Weigth" or j == "Pes":
                new_dict[i][j] = round(float(dict[i][j]) * pou_kgs, 2)
            else:
                new_dict[i][j] = dict[i][j]
    
    return new_dict



