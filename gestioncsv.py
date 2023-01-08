import csv
import os
import copy

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def masseMolecule(formule_brut, masseElement):
    """fonction permetant de calculer la masse
    d'un marqueur a partir de sa formule brut(str) """

    masseMarqeur = 0
    chaineEtudiee = ""
    compteur = 0

    while compteur < len(formule_brut):

        if formule_brut[compteur] not in Alphabet:
            multiple = formule_brut[compteur]
            while compteur != len(formule_brut)-1 and formule_brut[compteur+1] not in Alphabet:
                multiple += formule_brut[compteur+1]
                compteur += 1

            masseMarqeur += (int(multiple) - 1) * masseElement[chaineEtudiee]
            compteur += 1

        elif (len(formule_brut[compteur:])) > 1 \
                and (formule_brut[compteur + 1] in Alphabet) \
                and (str.lower(formule_brut[compteur + 1]) == formule_brut[compteur + 1]):

            chaineEtudiee = formule_brut[compteur] + formule_brut[compteur + 1]
            masseMarqeur += masseElement[chaineEtudiee]
            compteur += 2

        else:
            chaineEtudiee = formule_brut[compteur]
            masseMarqeur += masseElement[chaineEtudiee]
            compteur += 1

    return masseMarqeur


def convert_masse_str_to_float(liste_marqueur_brut):

    """fonction nécessaire pour pouvoir utiliser
    la liste extraite du csv où les masse sont stockées en str
    en les convertisant en float"""

    intermediaire = copy.deepcopy(liste_marqueur_brut)
    for ligne in intermediaire:
        ligne[1] = float(ligne[1].replace(',', '.'))
    return intermediaire


def extract(file_name):

    """fonction qui extrait du fichier csv une liste de liste
    ou chaque elements est un [couple nom(str)/masse(float)],
    attention a bien mettre file_name etre crochets et de
    ne pas oublier l'extetion"""

    L = []
    f = open(file_name, 'r')
    cvs_f = csv.reader(f)

    for line in cvs_f:
        if line != []:
            L.append(line)
    return convert_masse_str_to_float(L)


masseElement = {}
a = extract('BDD_Standar_Atomic_Weights.csv')
for masse in a:
    masseElement[masse[0]] = float(masse[1])


def ajout_bdd(BDD, molecule):
    """ permet d'ajouter une molécule à la BDD"""

    massemolecule = str(masseMolecule(molecule, masseElement))
    f = open(BDD, 'a')
    writer = csv.writer(f)
    writer.writerow([molecule, massemolecule])
    f.close()


def renvoyer_masse(BDD, molecule):

    """## prend une molécule en entrée et renvoie sa masse"""

    f = open(BDD, 'r')
    lire = csv.reader(f)
    for i in lire:
        if i != []:
            if i[0] == molecule:
                return(i[1])
    return None
    f.close()


def supprime(BDD, molecule):

    """prend une molécule en entrée et
    la supprime de la base de données"""

    L = []
    L2 = []
    f = open(BDD, 'r')
    lire = csv.reader(f)
    for i in lire:
        if i != []:
            a = i[0]
            b = i[1]
            L.append([a, b])
    for i in range(len(L)):
        if L[i][0] != molecule:
            L2.append(L[i])
    f.close()
    os.remove(BDD)
    f = open(BDD, 'a')
    writer = csv.writer(f)
    for ligne in L2:
        writer.writerow(ligne)
    f.close()


def est_dans_bdd(BDD, marqueur):

    """permet de savoir si un marqueur est
    dans la BDD"""

    f = open(BDD, 'r')
    lire = csv.reader(f)
    for i in lire:
        if i != [] and i[0] == marqueur:
            return True
    f.close()
    return False

