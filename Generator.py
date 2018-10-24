import random
import sys
listaGraczy = ['A', 'B', 'C', 'D', 'E']
team1 = []
team2 = []
for el in range( len(listaGraczy) ):
    losowyGracz = random.choice( listaGraczy )
    listaGraczy.remove(losowyGracz)
    team1.append(losowyGracz)


def generujTeamy(lista):
    random.shuffle(lista)
    team2 = lista[0 : len(lista) // 2]
    team1 = lista[len(lista) // 2: ]
    return team1, team2

print( sys.argv)
