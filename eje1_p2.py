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