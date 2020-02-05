import itertools
import matplotlib.pyplot as plt
import matplotlib.animation as anim

from City import City
from Itineraire import Itineraire
from GPS import GPS
from random import randrange, sample, randint


NB_MAX_PERMS = 100
SELECTION_RATE_PERCENTAGE = 0.20
MUTATION_RATE_PERCENTAGE = 0.05


paris = City('paris', randrange(10), randrange(10))
londres = City('londres', randrange(10), randrange(10))
marseille = City('marseille', randrange(10), randrange(10))
madrid = City('madrid', randrange(10), randrange(10))
viennes = City('viennes', randrange(10), randrange(10))
montpellier = City('montpellier', randrange(10), randrange(10))
nice = City('nice', randrange(10), randrange(10))
perpignan = City('perpignan', randrange(10), randrange(10))
clermont = City('clermont', randrange(10), randrange(10))
toulouse = City('toulouse', randrange(10), randrange(10))

listOfCity = [paris, londres, marseille, madrid, viennes,
              montpellier]


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


def generateItineraires():
    itineraires = []
    for tuplePerms in perms:
        itineraires.append(Itineraire(tuplePerms))
    return itineraires


generatePerms(listOfCity, 1000)
itineraires = generateItineraires()

gps = GPS(itineraires, len(itineraires),
          SELECTION_RATE_PERCENTAGE, MUTATION_RATE_PERCENTAGE, len(listOfCity))


def connectpoints(x, y, p1, p2, ax):
    ax.plot([x, p1], [y, p2], 'k-')


def draw(ax):
    for city in listOfCity:
        ax.plot(city.x, city.y, 'ro')

    for index in range(len(gps.itineraires[0].trajet)):
        trajet = gps.itineraires[0].trajet[index]
        trajetDest = ""
        if index >= len(gps.itineraires[0].trajet) - 1:
            trajetDest = gps.itineraires[0].trajet[0]
        else:
            trajetDest = gps.itineraires[0].trajet[index + 1]
        connectpoints(trajet.x, trajet.y, trajetDest.x, trajetDest.y, ax)



def plot_cont(xmax):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def update(i):
        ax.clear()
        gps.iterrate()
        draw(ax)
        print(i)
    a = anim.FuncAnimation(fig, update, frames=xmax, repeat=False)
    plt.show()


plot_cont(50000)

