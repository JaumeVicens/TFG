import sys
import math
import numpy as np

sys.setrecursionlimit(10000)

# -----------------------------------------------------------------------
# Funcions generatrius
# -----------------------------------------------------------------------

def A1(x):
    return (1 - math.sqrt(1 - 4 * x)) / (2 * x)

def Cbullet(x):
    return x / math.sqrt(1 - 4 * x)

# -----------------------------------------------------------------------
# BSSeqüènciaC — versió iterativa
# -----------------------------------------------------------------------

def BSSeqüènciaC(x):
    p_stop = 1.0 / A1(x)
    K = 0
    nodes = []
    while True:
        u = np.random.uniform(0, 1)
        if u <= p_stop:
            break
        K += 1
        nodes.append("*·")
    result = ''
    for _ in nodes:
        result = ("*·", result)
    return (K, result)

# -----------------------------------------------------------------------
# BS per a C^bullet — versió iterativa amb pila explícita
# -----------------------------------------------------------------------

def BS(x):
    p_base = A1(x) / Cbullet(x)
    stack = []
    while True:
        u = np.random.uniform(0, 1)
        if u <= p_base:
            aux = BSSeqüènciaC(x)
            mida_actual = 1 + aux[0]
            obj_actual  = ("*·", aux[1])
            break
        else:
            aux1 = BSSeqüènciaC(x)
            stack.append(aux1)
    while stack:
        aux1 = stack.pop()
        aux2 = BSSeqüènciaC(x)
        mida_actual = 1 + aux1[0] + mida_actual + aux2[0]
        obj_actual  = ("*", aux1[1], obj_actual, aux2[1])
    return (mida_actual, obj_actual)

# -----------------------------------------------------------------------
# Rejection Sampler
# -----------------------------------------------------------------------

def RejectionSampler(x, n, epsilon):
    gamma = BS(x)
    while gamma[0] > n * (1 + epsilon) or gamma[0] < n * (1 - epsilon):
        gamma = BS(x)
    return gamma

# -----------------------------------------------------------------------
# Conversió a string ITERATIVA — evita RecursionError en print()
# -----------------------------------------------------------------------

def tree_to_str(obj):
    """
    Converteix la tupla nidada a string sense recursió,
    usant una pila explícita. Equivalent a str(obj) però
    segur per a arbres molt profunds.
    """
    result = []
    # Cada element de la pila és (node, fase)
    # fase 0 = encara no hem processat
    stack = [(obj, 0)]
    while stack:
        node, fase = stack.pop()
        if isinstance(node, tuple):
            if fase == 0:
                result.append('(')
                # Posem els fills en ordre invers per processar-los en ordre
                # i afegim separadors
                children = list(node)
                # Primer processem el tancament
                stack.append((')', 1))
                for i in range(len(children) - 1, -1, -1):
                    if i < len(children) - 1:
                        stack.append((', ', 1))
                    stack.append((children[i], 0))
            else:
                result.append(node)
        elif isinstance(node, str):
            if fase == 1:
                result.append(node)
            else:
                result.append(repr(node))
        else:
            result.append(repr(node))
    return ''.join(result)

# -----------------------------------------------------------------------
# Paràmetre x òptim per a n = 10^5
# -----------------------------------------------------------------------

n = 10**5
x = (n * (n - 1)) / (2 * n - 1) ** 2

print(f"Generant arbre de mida ~{n} amb epsilon=0.05 ...")
resultat = RejectionSampler(x, n, 0.05)

print(f"Mida de l'arbre generat: {resultat[0]} nodes")

# Usam la funció iterativa per imprimir, evitant RecursionError
arbre_str = tree_to_str(resultat[1])
#print(arbre_str)
print("Primers 300 caràcters:")
print(arbre_str[:300], "...")