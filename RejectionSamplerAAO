import sys

from BoltzmannSamplerFinit import generatriu_avaluada,BoltzmannSamplerFinit
from BSSeqüència import BoltzmannSamplerSequencia
import math
import numpy as np

sys.setrecursionlimit(10000)

atompuntejat = {"*·" : 1}

atom = {"*" : 1}

def A1(x):
    return (1-math.sqrt(1-4*x))/(2*x)

def Cbullet(x):
    return x/(math.sqrt(1-4*x))

# BS per a Seq(C), on C=(Z^\bullet)xSeq(C)
def BSSeqüènciaC(x):
    p_stop = 1.0 / A1(x)
    K1 = 0  #anam comptant els àtoms que es van generant
    nodes = []
    # la probabilitat de retornar la seqüència buida ve donada per  1/C(x)=1/A1(X), altrament es torna
    # s'afegeix un node puntejat i es torna a fer una crida a l'algorisme

    # Se fa d'aquesta manera i no amb una crida recursiva per que per a n gran s'arriba al limit
    # de recursions permeses a pycharm

    while True:
        u = np.random.uniform(0, 1)
        if u <= p_stop:
            break

        K1 += 1
        nodes.append("*·")

    # construim ara l'estructura de l'objecte
    result = ''
    for _ in  nodes:
        result = ("*·",result)

    return (K1,result)

#aqui hem de retornar s'objecte i sa mida
def BS(x):
    u = np.random.uniform(0, 1)
    if u <= (A1(x))/Cbullet(x):
        auxiliar = BSSeqüènciaC(x)
        mida = 1 + auxiliar[0]
        obj = ("*·",auxiliar[1])
        return (mida,obj)

    else:
        auxiliar1 = BSSeqüènciaC(x)
        subarbre = BS(x)
        auxiliar2 = BSSeqüènciaC(x)
        mida = 1 + auxiliar1[0] + subarbre[0] + auxiliar2[0]
        obj = ("*", auxiliar1[1], subarbre[1], auxiliar2[1])
        return (mida,obj)

def RejectionSampler(x,n,epsilon):
    gamma = BS(x)
    while gamma[0] > n*(1+epsilon) or gamma[0] < n*(1-epsilon):
        gamma = BS(x)

    return gamma


n = 600

x = (n*(n-1))/(2*n-1)**2

print(RejectionSampler(x,600,0.05)[1])

print(RejectionSampler(x, 600, 0.05)[0])
