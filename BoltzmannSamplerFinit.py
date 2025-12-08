import numpy as np

#funcio que donada una classe combinatòria (en forma de diccionari) on cada objecte (clau)
# té associat una mida (valor) retorna sa funcio generatriu avaluada a x
def generatriu_avaluada(dicc,x):
    sum = 0
    for i in dicc:
        sum += x**dicc[i]     #dicc[i] se correspon amb sa mesura de s'objecte i
    return sum

#genera un element de sa classe W={w1,...,wr} de manera aleatòria on cada element té proba
# bilitat x^{|w_i|}/W(x) de ser seleccionat (fixat x>0)
def BoltmzannSamplerFinit(dicc,x):
    llista = []  #llista on anirem guardant els valors s_j
    sum = 0
    for i in dicc:
        sum += x**dicc[i]
        #print(sum/generatriu_avaluada(dicc,x))
        llista.append(sum/generatriu_avaluada(dicc,x))

    u = np.random.uniform(0, 1)  #genera un nombre aleatori en l'interval [0,1]
    #print(u)
    triat = None
    for j in range(len(dicc)):
        if u <= llista[j]:  #sempre es compleix per qualque j algo ja que 0<s1<···<sr=1 (si x>0)
            triat = j   #se correspon amb l'index j de l'element w_j que hem de
                        # retornar
            #print(triat)
            break       #d'aquesta manera seleccionam el primer que ho compleix

    #retornam l'element w_j de la classe
    iter = 0
    for i in dicc:
        #print(i)
        if iter == triat:
            return  i
        iter += 1


classe = {"a": 3,"b": 1, "c": 2, "d": 1, "e": 4}

# té funció generatriu 2x+x^2+x^3+x^4. que té arrels (reals) x = 0 i x = −1.3532099642 (aprox)
# per tant el model està definit per a tot x > 0.

#print(BoltmzannSampler(classe, 1.79632190325944))
#print(BoltmzannSampler(classe, 3/2))
#print(BoltmzannSampler(classe, 2))


#retorna sa mida mitjana dels objectes produits per BS en 1000 execucions
def mida_mitjana_executar_BS(dicc,x):
    n = 1000
    llista = []
    for i in range(n):
        mida = dicc[BoltmzannSamplerFinit(dicc,x)]
        llista.append(mida)
    suma = 0
    for i in range(n):
        suma += llista[i]

    return suma/n

#print(mida_mitjana_executar_BS(classe,1.79632190325944))  #es l'x (aproximat) talque E_x[N] = 3

#print(mida_mitjana_executar_BS(classe, 0.5))  # els objectes amb mida menor tenem mes probabilitats de ser generats


#funcio que ens calcula l'x talque E_x[N] = "mesura desitjada". Tenguent en compte que
# E_x[N] = x·C'(x)/C(x)   (pendent)

#def generatriu(dicc):
    #x = symbols('x')
    #f = 0
    #for i in dicc:
        #f += x**dicc[i]




