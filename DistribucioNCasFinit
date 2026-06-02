from cProfile import label

from BoltzmannSamplerFinit import generatriu_avaluada, BoltzmannSamplerFinit
import matplotlib.pyplot as plt
import numpy as np

#funcio que donada una classe combinatoria finita calcula el nombre d'elements de mida n
def ObjectesDeMidan(C,n):
    sum = 0
    for i in C:
        if C[i] == n:
            sum += 1

    return sum

#retorna P(N=n)=(C_nx^n)/C(x) per a la classe combinatoria finita C de l'exemple 3.1 de l'overleaf, per
# a cada x>0
def Distribucio(C,x,n):
    return ObjectesDeMidan(C,n)*(x**n)/generatriu_avaluada(C,x)


#graficam per a distints valors de x


classe = {"a": 3,"b": 1, "c": 2, "d": 1, "e": 4}

#t = [1,2,3,4]

#y1 = [Distribucio(classe,0.4,i) for i in t]
#y2 = [Distribucio(classe,3/2,i) for i in t]
#y3 = [Distribucio(classe,0.8,i) for i in t]

#plt.plot(t,y1, label = "x=0.4")
#plt.plot(t,y2, label = "x=1.5")
#plt.plot(t,y3, label = "x=0.8")
#plt.xticks([1, 2, 3, 4])
#plt.xlabel("$\mathcal{N}$")
#plt.ylabel("$\mathbb{P}_{\mathcal{C},x}(\mathcal{N})$")
#plt.legend()

#plt.show()


def mida_mitjana_executar_BS(dicc,x):
    n = 10000
    llista = []
    for i in range(n):
        mida = dicc[BoltzmannSamplerFinit(dicc,x)]
        llista.append(mida)
    suma = 0
    for i in range(n):
        suma += llista[i]

    return suma/n

x = np.linspace(0.005, 2, 1000)
y = [mida_mitjana_executar_BS(classe,i) for i in x]

plt.xlabel("$x$")
plt.ylabel("$\mathbb{E}_x(\mathcal{N})$")
plt.plot(x,y)
plt.show()
