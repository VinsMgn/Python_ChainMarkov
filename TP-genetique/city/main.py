import itertools
import matplotlib.pyplot as plt
import matplotlib.animation as anim

from City import City
from Itineraire import Itineraire
from GPS import GPS
from random import randrange, sample, randint


NB_MAX_PERMS = 100
SELECTION_PERCENTAGE = 0.20
MUTATION_PERCENTAGE = 0.05


Bordeaux = City('bordeaux', randrange(10), randrange(10))
Montpellier = City('montpellier', randrange(10), randrange(10))
Barcelone = City('barcelone', randrange(10), randrange(10))
Strasbourg = City('strasbourg', randrange(10), randrange(10))
Paris = City('paris', randrange(10), randrange(10))
Londres = City('londres', randrange(10), randrange(10))
Nantes = City('nantes', randrange(10), randrange(10))
Nice = City('nice', randrange(10), randrange(10))
Toulouse = City('toulouse', randrange(10), randrange(10))
Monaco = City('monaco', randrange(10), randrange(10))

listOfCities = [Bordeaux, Montpellier, Paris, Barcelone, Toulouse,
                Monaco, Nantes, Londres]


perms = []


def generatePerms(a, nbPerm, k=0):
    b = a.copy()
    if k == len(a):
        perms.append(b)
    else:
        for i in range(k, nbPerm):
            if i >= len(a):
                break
            b[k], b[i] = b[i], b[k]
            generatePerms(b, nbPerm, k+1)
            b[k], b[i] = b[i], b[k]


def generateChemins():
    itineraires = []
    for tuplePerms in perms:
        itineraires.append(Itineraire(tuplePerms))
    return itineraires


generatePerms(listOfCities, 1000)
itineraires = generateChemins()

gps = GPS(itineraires, len(itineraires),
          SELECTION_PERCENTAGE, MUTATION_PERCENTAGE, len(listOfCities))


def connectpoints(x, y, point1, point2, ax):
    ax.plot([x, point1], [y, point2], 'k-')


def draw(ax):
    for city in listOfCities:
        ax.plot(city.x, city.y, 'ro')

    for index in range(len(gps.itineraires[0].chemin)):
        chemin = gps.itineraires[0].chemin[index]
        cheminDest = ""
        if index >= len(gps.itineraires[0].chemin) - 1:
            cheminDest = gps.itineraires[0].chemin[0]
        else:
            cheminDest = gps.itineraires[0].chemin[index + 1]
        connectpoints(chemin.x, chemin.y, cheminDest.x, cheminDest.y, ax)


def plot_cont(xmax):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def update(i):
        ax.clear()
        gps.iterrate()
        draw(ax)
    a = anim.FuncAnimation(fig, update, frames=xmax, repeat=False)
    plt.show()


plot_cont(50000)
