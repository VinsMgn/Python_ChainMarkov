from random import randint
from Itineraire import Itineraire
import itertools


class GPS:

    def __init__(self, itineraires, nbChemins, selectionRate, mutationRate, nbVilles):
        super().__init__()
        self.itineraires = itineraires
        self.childs = []
        self.nbChemins = nbChemins
        self.selectionRate = selectionRate
        self.mutationRate = mutationRate
        self.nbVilles = nbVilles
        self.step = 0

    def executeHomicide(self):
        sortedArray = self.sortedArrayByFitness()
        toTake = round(len(sortedArray) * self.selectionRate)
        self.itineraires = sortedArray[:toTake]

    def sortedArrayByFitness(self):
        return sorted(self.itineraires, key=lambda itineraire: itineraire.fitness, reverse=False)

    def crossoverIsInChild(self, currentChild, toAppend):
        fromMotherCitiesName = []
        for city in currentChild:
            fromMotherCitiesName.append(city.name)
        return toAppend.name in fromMotherCitiesName

    def crossover(self):
        childs = []
        for index in range(len(self.itineraires)):
            mother = self.itineraires[index]
            father = ""
            if (index + 1 >= len(self.itineraires)):
                father = self.itineraires[0]
            else:
                father = self.itineraires[index + 1]
            begin = randint(0, len(mother.chemin) - 1)
            end = randint(begin, len(mother.chemin) - 1)
            fromMother = mother.chemin[begin:end]
            childCities = []
            for i in range(len(father.chemin)):
                if (len(childCities) == begin):
                    childCities = childCities + fromMother
                if (not self.crossoverIsInChild(fromMother, father.chemin[i])):

                    childCities.append(father.chemin[i])

            self.childs.append(Itineraire(childCities))

        if len(self.childs) != self.nbChemins:
            self.crossover()
        else:
            self.itineraires = self.childs
            self.childs = []
        return

    def mutate(self):
        for itineraire in self.itineraires:
            itineraire.randomMutation(self.mutationRate)
        return

    def iterrate(self):
        self.executeHomicide()
        self.crossover()
        self.mutate()
        self.printStep()
        self.step = self.step + 1

    def printStep(self):
        print(
            f"Generation n°{self.step}")
