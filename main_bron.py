from fonctions_graph import *

"""vérifications rapides des compatibilités"""

masseElement = extract('BDD_Standar_Atomic_Weights.csv')
"""Pour 1"""
#print(listeCompatible([('C13H11', 167.22643999999997), ('C4H9', 57.11426), ('C11H20NO2', 198.282), ('C7H6NO2', 136.12804), ('C13H29OSi', 229.45425999999998)]))
"""Pour 2"""
#print(listeCompatibleMarqueurFinalOptimal([("C13H29OSi",229.45425999999998-211.2), ("C6H11O",99.15094), ("C11H15",147.23680000000002), ("C9H11O2",151.18244), ("C4H9",57.11426), ("C8F3H6",159.1284496), ("C7H14NO2",144.19156), ("C13H11",167.22643999999997), ("C8H7BrCl",218.49818000000002)]))

while True:
    print("Rentrer 1 si vous voulez les combinaisons maximales compatibles avec tous les marqueurs pouvant être le marqueur final")
    print("Rentrer 2 si vous voulez les combinaisons maximales avec le marqueur final optimal")
    a = int(input())
    if a == 1:
        G = get_adjacency_dict(BDD)
        P = G.keys()
        combinations = list(bron_kerbosch(P, G))
        print(combination_max(combinations))
    if a == 2:
        g = find_optimal_final_tag()
        solutions = g[0]  # combinaisons
        final_tag = g[1]  # marqueur final optimal qui permet d'obtenir ces combinaisons
        for i in solutions:
            print("La combianison ", i, " est solution avec " + final_tag + " en marqueur final")




