import csv

with open("basket_players.csv") as csv_file:
    players = csv.reader(csv_file, delimiter= ";")
    line = 0
    categories = ["Nom", "Equip", "Posició", "Altura", "Pes", "Edat"]
    contingut_players = {}
    for i in players:
        if line != 0:
          actual_player = "player" + str(line)
          contingut_players[actual_player]= {}
          for j in range(0,len(categories)):
             contingut_players[actual_player][categories[j]] = i[j]
        line += 1
    
print(contingut_players)
