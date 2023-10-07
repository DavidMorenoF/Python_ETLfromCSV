import csv
def cambiar_separador(dict, new_csv):
    try:
        with open(new_csv, 'w', newline='') as archivo_salida:
            escritor_csv = csv.writer(archivo_salida, delimiter="^")
            categories = []
            for player in dict:
                for category in dict[player]:
                    categories.append(category)
                break
            escritor_csv.writerow(categories)

            for player in dict:
                fila = []
                for i in dict[player].values():
                    fila.append(i)
                escritor_csv.writerow(fila)
    except NameError:
        print("Ha ocurrit un error:", NameError)
    finally:
        archivo_salida.close()

        