from random import randint
from Individu import Individu

class Population:

  def __init__(self, individus, finalWord, nbIndividus, selectionRate, mutationRate):
    super().__init__()
    self.individus = individus
    self.childs = []
    self.finalWord = finalWord
    self.nbIndividus = nbIndividus
    self.selectionRate = selectionRate
    self.mutationRate = mutationRate
    self.step = 0
    
  def executeHomicide(self):
    sortedArray = self.sortedArrayByFitness()
    toTake = round(len(sortedArray) * self.selectionRate)
    self.individus = sortedArray[:toTake]

  def sortedArrayByFitness(self):
    return sorted(self.individus, key=lambda individu: individu.fitness, reverse=True)

  def crossover(self):
    seperation = randint(0, len(self.finalWord))
    for index in range(len(self.individus)):
      # Check if we have reproduce the nbIndividus
      if len(self.individus) == self.nbIndividus:
        break;

      mother = self.individus[index].word
      father = ""
      if (index + 1 >= len(self.individus)):
        father = self.individus[0].word
      else:
        father = self.individus[index + 1].word
      
      childDefaultValue = mother[0:seperation] + father[seperation: len(father)]
      while len(childDefaultValue) != len(self.finalWord):
        childDefaultValue = childDefaultValue[:-1]
        # print(len(childDefaultValue), len(self.finalWord))

      child = Individu(self.finalWord, childDefaultValue)
      self.childs.append(child)

    if len(self.childs) != self.nbIndividus:
      self.crossover()
    else:
      self.individus = self.childs
      self.childs = []
    return
  
  def mutate(self):
    for individu in self.individus:
      individu.randomMutate(self.mutationRate)
    return
  
  def iterrate(self):
    self.executeHomicide()
    self.crossover()
    self.mutate()
    self.printStep()
    self.step = self.step + 1

  def printStep(self):
    print(f"{self.individus[0].word} possede un fitness de {self.individus[0].genFitness(self.finalWord)} | Generation {self.step}")

  def isGood(self):
    self.individus = self.sortedArrayByFitness()
    if (self.individus[0].genFitness(self.finalWord) > 0.99):
      return True
    else:
      return False
