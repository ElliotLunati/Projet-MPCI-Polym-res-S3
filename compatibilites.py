from math import *

ECART_DERNIERE_BASE = 211.2
ECART_0_1 = 28
NB_1 = 5

def compatible(marqueur1, marqueur2): #masses seulement, on vérifie si les marquers sont compatibles à n'importe quelle position dans le polymère

    marqueur1Fin = marqueur1 - ECART_DERNIERE_BASE
    marqueur2Fin = marqueur2 - ECART_DERNIERE_BASE
    moduloMarqueur1 = floor(marqueur1) % ECART_0_1 + marqueur1 - floor(marqueur1)
    moduloMarqueur2 = floor(marqueur2) % ECART_0_1 + marqueur2 - floor(marqueur2)
    moduloMarqueur1Fin = floor(marqueur1Fin) % ECART_0_1 + marqueur1Fin - floor(marqueur1Fin)
    moduloMarqueur2Fin = floor(marqueur2Fin) % ECART_0_1 + marqueur2Fin - floor(marqueur2Fin)

    if abs(marqueur1 - marqueur2) > NB_1 * ECART_0_1 \
        or (abs(moduloMarqueur1 - moduloMarqueur2) > 3
            and abs(moduloMarqueur1Fin - moduloMarqueur2) > 3
            and abs(moduloMarqueur1 - moduloMarqueur2Fin) > 3):

        return True

    return False

def listeCompatible(listeMarqueurs):
    for i in range(len(listeMarqueurs)-1):
        for j in range(i+1, len(listeMarqueurs)):
            if not compatible(listeMarqueurs[i][1], listeMarqueurs[j][1]):
                return False
    return True

def compatibleMarqueurFinalDefini(marqueur1, marqueur2):  #masses seulement, on vérifie plus la position des marqueurs dans le polymère puisqu'on va les fixer
    moduloMarqueur1 = floor(marqueur1) % ECART_0_1 + marqueur1 - floor(marqueur1)
    moduloMarqueur2 = floor(marqueur2) % ECART_0_1 + marqueur2 - floor(marqueur2)

    if abs(marqueur1 - marqueur2) > NB_1 * ECART_0_1 \
        or abs(moduloMarqueur1 - moduloMarqueur2) > 3:
        return True
    return False

def listeCompatibleMarqueurFinalOptimal(listeMarqueurs):
    for i in range(len(listeMarqueurs)-1):
        for j in range(i+1, len(listeMarqueurs)):
            if not compatibleMarqueurFinalDefini(listeMarqueurs[i][1], listeMarqueurs[j][1]):
                return False
    return True