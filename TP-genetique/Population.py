from random import randint
from Individu import Individu

class Population:

  def __init__(self, individus, targetWord, nbIndividus, selectionRate, mutationRate):
    super().__init__()
    self.individus = individus
    self.childs = []
    self.targetWord = targetWord
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
    seperation = randint(0, len(self.targetWord))
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
      while len(childDefaultValue) != len(self.targetWord):
        childDefaultValue = childDefaultValue[:-1]


      child = Individu(self.targetWord, childDefaultValue)
      self.childs.append(child)

    if len(self.childs) != self.nbIndividus:
      self.crossover()
    else:
      self.individus = self.childs
      self.childs = []
    return
  
  def mutation(self):
    for individu in self.individus:
      individu.randomMutation(self.mutationRate)
    return
  
  def iterrate(self):
    self.executeHomicide()
    self.crossover()
    self.mutation()
    self.printInformation()
    self.step = self.step + 1

  def printInformation(self):
    print(f"{self.individus[0].word} avec un fitness de {self.individus[0].generateFitness(self.targetWord)} / Generation n° {self.step}")

  def goodWord(self):
    self.individus = self.sortedArrayByFitness()
    if (self.individus[0].generateFitness(self.targetWord) > 0.99):
      return True
    else:
      return False
