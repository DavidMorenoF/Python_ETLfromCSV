import csv
import json

def pasar_a_json(path, pathJSON):
    with open(path) as csv_players, open(pathJSON, mode='w') as json_players:
        csv_reader = csv.DictReader(csv_players, delimiter="^")
    
        jugadores = {}

        for i, row in enumerate(csv_reader):
            jugador = {
            "Nom": row["Nom"],
            "Equip": row["Equip"],
            "Posicio": row["Posicio"],
            "Alçada": float(row["Alçada"]),
            "Pes": float(row["Pes"]),
            "Edat": int(row["Edat"])
            }

            jugadores[f"jugador{i + 1}"] = jugador

        json.dump(jugadores, json_players, indent=4)