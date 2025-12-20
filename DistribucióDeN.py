import math
#from BoltzmannSamplerFinit import generatriu_avaluada
import matplotlib.pyplot as plt
#import numpy as np


# funció que retorna el grafic de la distribució de la variable aletoria N
# per a cada x>0 (coherent).

#cas de les seqüències binàries. Retorna P(N=t). Es necessari conèixer C_n per això se fa
# cada cas per separat
def DistrubucioNParaulesBinaries(x,t):

    return ((1-2*x))*2**t*x**t

#t = [i for i in range(50)]

#y = [DistrubucioNParaulesBinaries(0.4,i) for i in t]

#plt.plot(t,y)
#plt.show()


#cas dels arbres arrelats binaris ordenats amb funcio de mida donada pel nombre total de nodes
# Retorna P(N=t)
def DistrubucioNABOT(x,t):
    for i in range(t):
        if t % 2 == 0:
            return 0
        else:
            return (1/((1-math.sqrt(1-4*x**2))/(2*x)))*(1/((t//2)+1))*math.comb(2*(t//2),(t//2))*x**t #pagina 36 tfg carla


t = [i for i in range(15)]

y = [DistrubucioNABOT(0.4999,i) for i in t]

plt.plot(t,y)    #comprovar aquest darrer cas. Ara si funciona en principi
plt.show()
