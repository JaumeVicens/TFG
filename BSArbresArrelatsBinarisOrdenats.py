import math
#import random
import numpy as np

def B(x):
    return (1-math.sqrt(1-4*x**2))/(2*x)

# Boltmzann Sampler per a la classe dels arbres arrelats binaris ordenats amb mida donada
# pel nombre total de nodes

def BSArbresArrelatsBinarisOrdenats(x):
    u = np.random.uniform(0,1)
    if u <= (x/B(x)):
        return '*'
    else:
        return ('*',BSArbresArrelatsBinarisOrdenats(x),BSArbresArrelatsBinarisOrdenats(x))

#print(BSArbresArrelatsBinarisOrdenats(0.499))    # el valor crític es 1/2

