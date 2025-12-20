from BoltzmannSamplerFinit import BoltmzannSamplerFinit
from BoltzmannSamplerFinit import generatriu_avaluada
import numpy as np


# Boltzmann Sampler per a la classe combinatòria Seq(A), on A es una classe combinatòria
# finita qualsevol. '' representa l'atom de mida 0 (paraula buida)

def BoltmannSamplerSequencia(A,x):
    u = np.random.uniform(0,1)
    if u <= generatriu_avaluada(A,x):
        return (BoltmzannSamplerFinit(A,x),BoltmannSamplerSequencia(A,x))

    else:
        return ''

A = {'0': 1, '1': 1}

print(BoltmannSamplerSequencia(A,0.45))  #esta definida per x < 1/2 ja que s'ha de complir que 1 > A(x) = 2x
