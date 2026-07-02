import math
import random
import sys

sys.setrecursionlimit(100000000)


# Boltzmann sampler per a la classe dels arbres de Cayley


# Excepció per abortar quan l'arbre és massa gran
class ArbreGranError(Exception):
    pass



#no passam per paràmetre el valor x ja que emprarem semrpe rho
def BSCayley(max_size, comptador):
    k = 0     # retornam el valor k amb k seguint una Poiss(\hat{A(\rho)})=Poiss(1)
    p = math.exp(-1)
    S = p
    u = random.random()
    while u >= S:
        p = p/(k+1)
        k += 1
        S += p



    comptador[0] += 1          #cada vegada que es crida a la funció la mida augmenta en 1
    if comptador[0] > max_size:
        raise ArbreGranError()

    fills = []
    for _ in range(k):
        _,fill = BSCayley(max_size, comptador)
        fills.append(fill)

    return comptador[0],('*',fills)

#assignam una permutació aleatòria als nodes de l'objecte construit
def etiqueta_arbre(arbre, etiquetes):
    idx = random.randrange(len(etiquetes))
    etiquetes[idx], etiquetes[-1] = etiquetes[-1], etiquetes[idx]
    label = etiquetes.pop()
    _, fills = arbre
    fills_etiquetats = [etiqueta_arbre(fill, etiquetes) for fill in fills]
    return (label, fills_etiquetats)



def RejectionSampler(n, epsilon):
    low          = n * (1 - epsilon)
    high         = n * (1 + epsilon)

    intents = 0
    while True:
        intents += 1
        comptador = [0]           # llista para poder modificar-ho dins de la recursió
        try:
            gamma = BSCayley(high, comptador)
            mida = gamma[0]
            if mida >= low:             # sabemos que gamma[0] <= high por el early stop
                print(f"Intents fins acceptar: {intents}")
                etiquetes = list(range(1, mida + 1))
                arbre_etiq = etiqueta_arbre(gamma[1], etiquetes)
                return mida, arbre_etiq
        except ArbreGranError:
            pass


# --- Main ---
import time
n       = 100000
epsilon = 0.1

t0 = time.perf_counter()
resultat = RejectionSampler(n, epsilon)
t1 = time.perf_counter()

print(f"Mida: {resultat[0]}")
print(f"Temps: {t1-t0:.3f} segundos")

print(resultat[1])