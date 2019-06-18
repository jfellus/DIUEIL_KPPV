from numpy import *
from matplotlib import pyplot as plt
import matplotlib as mpl

# Jeu d'apprentissage
N = 500
Xtrain = random.rand(N,2)    # Points
Ytrain = where(sin(Xtrain[:,0]*3)*0.7>Xtrain[:,1], 'blue', 'magenta') # Classes associées


def dist(x,y):
    return sqrt(sum((x-y)**2))

def nn(x, X):
    mind = dist(x,X[0])
    imind = 0
    for i in range(1,X.shape[0]):
        d = dist(x,X[i])
        if d<=mind:
            mind = d
            imind = i
    return imind

def knn(k, x,X):
    dists = [float('inf')]*k
    inds = [-1]*k
    for i in range(1,X.shape[0]):
        d = dist(x,X[i])
        if d<=dists[0]:
            insere_liste_triee_limite(dists, inds, d, i)
    return inds

def insere_liste_triee_limite(l, indices, e, ind):
    l[0] = e
    indices[0] = ind
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            (l[i],l[i+1])=(l[i+1],l[i])
            (indices[i],indices[i+1])=(indices[i+1],indices[i])


for t in range(100):
    # On genère un point dont on doit predire la classe
    x = random.rand(2)

    # Prediction PPV
    ppv = knn(5, x, Xtrain)
    classe_predite = Ytrain[ppv]
    (classe,counts) = unique(classe_predite, return_counts=True)
    classe_predite = classe[argmax(counts)]
    
    # Affichage du jeu d'apprentissage, du point requete en rouge, et de son PPV en vert
    plt.ion()
    plt.clf()
    plt.scatter(Xtrain[:,0], Xtrain[:,1], c=Ytrain, s=10)
    plt.scatter(x[0], x[1], c='r', s=50)
    plt.scatter(Xtrain[ppv,0], Xtrain[ppv,1], c='g', s=50)
    plt.title("classe prédite : " + str(classe_predite))
    plt.show()
    plt.pause(1)
