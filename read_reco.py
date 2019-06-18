from numpy import *


def load(filename):
    f = open(filename)
    films = set()
    n = 0
    for l in f:
        if(l[0]=='-'):
            n = n + 1
        else:
            films.add(l)
    films = list(films)
    data = zeros((n,len(films)))
    i = -1
    f.seek(0)
    for l in f:
        if(l[0]=='-'):
            i=i+1
        else:
            data[i,films.index(l)] = 1
    return data
