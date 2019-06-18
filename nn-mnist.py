from read_mnist import *
from numpy import *
from plot import *

Xtrain = read_train_images()
Ytrain = read_train_labels()
Xtest = read_test_images()
Ytest = read_test_labels()

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



nb_succes = 0
for i in range(100):
    n = knn(5,Xtest[i], Xtrain)
    classe_predite = Ytrain[n]

    if n is not int:
        (classe,counts) = unique(classe_predite, return_counts=True)
        classe_predite = classe[argmax(counts)]
    else:
        n = [n]

    if classe_predite == Ytest[i]:
        nb_succes = nb_succes+1
    acc = nb_succes/(i+1)
    l = [Xtest[i],]
    l.extend(Xtrain[n])
    showm(l, anim=True)

    print(Ytest[i], '<=>', classe_predite,
        '  SUCCES!   ' if Ytest[i]==classe_predite else '  ERREUR!   ',
        '%.0f%%'%(acc*100),
        '           ', Ytrain[n] )
