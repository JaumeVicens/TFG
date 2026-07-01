import sys
import math
import random

sys.setrecursionlimit(1000000)

def C(x):
    return (1 - math.sqrt(1 - 4*x)) / 2

def Cbullet(x):
    return x / math.sqrt(1 - 4*x)


# Excepción para abortar cuando el árbol es demasiado grande
class ArbreGranError(Exception):
    pass


def BSC(x, cx, one_minus_cx, max_size, comptador):
    k = 0
    while random.random() >= one_minus_cx:
        k += 1

    comptador[0] += 1                        #comptam el node arrel cada vegada que es crida a la funcio
    if comptador[0] > max_size:
        raise ArbreGranError()              # vol dir que ja hem superat la mida que volem, abortam l'execucio de l'obecto per a ser mes eficients

    fills = []
    for _ in range(k):
        _, fill = BSC(x, cx, one_minus_cx, max_size, comptador)
        fills.append(fill)

    return comptador[0], ("*", fills)


def BSAtomPxSequenciaC(x, cx, one_minus_cx, max_size, comptador):
    k = 0
    while random.random() >= one_minus_cx:
        k += 1

    comptador[0] += 1                        # nodo puntejat
    if comptador[0] > max_size:
        raise ArbreGranError()

    fills = []
    for _ in range(k):
        _, fill = BSC(x, cx, one_minus_cx, max_size, comptador)
        fills.append(fill)

    return comptador[0], ("*·", fills)


def BSZxSeqCxCbulletxSeqC(x, cx, one_minus_cx, max_size, comptador):
    # Primera Seq(C)
    k1 = 0
    while random.random() >= one_minus_cx:
        k1 += 1

    comptador[0] += 1                        # nodo Z raíz
    if comptador[0] > max_size:
        raise ArbreGranError()

    seq1 = []
    for _ in range(k1):
        _, fill = BSC(x, cx, one_minus_cx, max_size, comptador)
        seq1.append(fill)

    # C*
    _, cbullet = BSbullet(x, cx, one_minus_cx, max_size, comptador)

    # Segunda Seq(C)
    k2 = 0
    while random.random() >= one_minus_cx:
        k2 += 1

    seq2 = []
    for _ in range(k2):
        _, fill = BSC(x, cx, one_minus_cx, max_size, comptador)
        seq2.append(fill)

    return comptador[0], ("*", seq1, cbullet, seq2)


def BSbullet(x, cx, one_minus_cx, max_size, comptador):
    p = cx / Cbullet(x)
    if random.random() <= p:
        return BSAtomPxSequenciaC(x, cx, one_minus_cx, max_size, comptador)
    else:
        return BSZxSeqCxCbulletxSeqC(x, cx, one_minus_cx, max_size, comptador)


def RejectionSampler(n, epsilon):
    x            = (n * (n-1)) / (2*n - 1)**2
    cx           = C(x)
    one_minus_cx = 1 - cx
    low          = n * (1 - epsilon)
    high         = n * (1 + epsilon)

    intentos = 0
    while True:
        intentos += 1
        comptador = [0]           # llista para poder modificar-ho dins de la recursió
        try:
            gamma = BSbullet(x, cx, one_minus_cx, high, comptador)
            if gamma[0] >= low:             # sabemos que gamma[0] <= high por el early stop
                print(f"Intents fins acceptar: {intentos}")
                return gamma
        except ArbreGranError:
            pass                            # arbre massa gran, reintentam


# --- Main ---
import time
n       = 80
epsilon = 0.01

t0 = time.perf_counter()
resultat = RejectionSampler(n, epsilon)
t1 = time.perf_counter()

print(f"Mida: {resultat[0]}")
print(f"Temps: {t1-t0:.3f} segundos")

print(resultat[1])





