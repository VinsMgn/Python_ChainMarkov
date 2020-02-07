from Individu import Individu
from Population import Population
from random import seed

# Seed pour bloquer l'aléatoire
# seed(3)

END_WORDS = "Hello world"
NB_INDIVIDUAL = 1000
SELECTION_PERCENTAGE = 0.20
MUTATION_PERCENTAGE = 0.10


def generateIndividus():
    listOfIndividus = []
    for i in range(500):
        listOfIndividus.append(Individu(END_WORDS))
    return listOfIndividus


def main():
    listIndividus = generateIndividus()
    population = Population(listIndividus, END_WORDS,
                            NB_INDIVIDUAL, SELECTION_PERCENTAGE, MUTATION_PERCENTAGE)

    while population.goodWord() == False:
        population.iterrate()
    population.printStep()


main()
