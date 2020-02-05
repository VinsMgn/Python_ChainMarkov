from random import randint
from Itineraire import Itineraire
import itertools

class GPS:

  def __init__(self, itineraires, nbItineraires, selectionRate, mutationRate, nbVilles):
    super().__init__()
    self.itineraires = itineraires
    self.childs = []
    self.nbItineraires = nbItineraires
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
      begin = randint(0, len(mother.trajet) -1)
      end = randint(begin, len(mother.trajet) - 1)
      fromMother = mother.trajet[begin:end]
      # childCities = father.trajet[0: begin - 1]
      childCities = []
      for i in range(len(father.trajet)):
        # if is where mother begin, add to child
        if (len(childCities) == begin):
          childCities = childCities + fromMother
        # else if is not in child, add to follow
        if (not self.crossoverIsInChild(fromMother, father.trajet[i])):
          
          childCities.append(father.trajet[i])

      self.childs.append(Itineraire(childCities))

    if len(self.childs) != self.nbItineraires:
      self.crossover()
    else:
      self.itineraires = self.childs
      self.childs = []
    return



  
  def mutate(self):
    for itineraire in self.itineraires:
      itineraire.randomMutate(self.mutationRate)
    return
  
  def iterrate(self):
    self.executeHomicide()
    self.crossover()
    self.mutate()
    self.printStep()
    self.step = self.step + 1

  def printStep(self):
    print()
    print(f"{self.itineraires[0]} possede un fitness de {self.itineraires[0].calculFitness()} | Generation {self.step}")

  def isGood(self):
    self.itineraires = self.sortedArrayByFitness()
    if (self.itineraires[0].calculFitness() > 999999):
      return True
    else:
      return False

