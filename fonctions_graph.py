from gestioncsv import *
from compatibilites import *
from copy import *

BDD = extract('BDD_Bases.csv')

def get_adjacency_dict(list_tags):    # ex list_tags : [(C7H7, 91), ...]
    adjacency_dict = {}
    for tag1 in list_tags:
        adjacency_dict[tag1[0]] = set()
        for tag2 in list_tags:
            if compatible(tag1[1], tag2[1]):
                adjacency_dict[tag1[0]].add(tag2[0])
    return adjacency_dict            # compatibilité marqueurs

def get_adjacency_dict_no_tag_position(list_tags):    # ex list_tags : [(C7H7, 91), ...]
    adjacency_dict = {}
    for tag1 in list_tags:
        adjacency_dict[tag1[0]] = set()
        for tag2 in list_tags:
            if compatibleMarqueurFinalDefini(tag1[1], tag2[1]):
                adjacency_dict[tag1[0]].add(tag2[0])
    return adjacency_dict            # compatibilité marqueurs


def bron_kerbosch(P, G, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            P=P.intersection(G[v]), G=G, R=R.union([v]), X=X.intersection(G[v]))
        X.add(v)


def combination_max(output_bron):          # garde que les combinaisons max (parceque l'algo bron_kerbosch ne renvoie pas que les max)
    output = [output_bron[0]]
    max = len(output_bron[0])
    for i in output_bron:
        if len(i) > max:
            max = len(i)
            output = [i]
        elif len(i) == max:
            output.append(i)
    return output

def final_tag_in_solution(list_tag, final_tag):    # vérifie que le marqueur final est bien dans les solutions (absolument nécessaire)
    output = []
    for i in list_tag:
        if final_tag in i:
            output.append(i)
    return output

def find_optimal_final_tag():
    output = [[], None]               # [combinaisons solutions, tag_final]
    for i in range(len(BDD)):       # on fixe un à un chaque marqueur en position finale et on vérifie laquelle renvoie la combinaison max
        tag = BDD[i][0]
        current_list = deepcopy(BDD)
        current_list[i][1] -= ECART_DERNIERE_BASE     # on fixe un marqueur final
        adj_dict = get_adjacency_dict_no_tag_position(current_list)
        P = adj_dict.keys()
        combinations = final_tag_in_solution(combination_max(list(bron_kerbosch(P, adj_dict))), tag)
        if len(combinations) >= len(output[0]):
            output = [combinations, tag]
    return output