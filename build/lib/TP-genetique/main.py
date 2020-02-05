from Individu import Individu
from Population import Population
from random import seed

# Seed pour bloquer l'aléatoire
# seed(2)

END_WORDS = "Hello"
NB_INDIVIDUALS = 1000
SELECTION_RATE_PERCENTAGE = 0.20
MUTATION_RATE_PERCENTAGE = 0.10


def genIndividus():
  indivus = []
  for i in range(500):
    indivus.append(Individu(END_WORDS))
  return indivus

def main():
  listIndividus = genIndividus()
  population = Population(listIndividus, END_WORDS,
                          NB_INDIVIDUALS, SELECTION_RATE_PERCENTAGE, MUTATION_RATE_PERCENTAGE)


  while population.isGood() == False:
    population.iterrate()
  population.printStep()

  

main()

