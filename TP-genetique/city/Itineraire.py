import random

class Itineraire:
  fitness = 0

  def __init__(self, trajet):
    super().__init__()
    self.trajet = trajet

  def calculFitness(self):
    for i in range(len(self.trajet)):
      if i == len(self.trajet) - 1:
        self.fitness = self.fitness + \
            self.trajet[i].calculateDistance(self.trajet[0])
        break;
      self.fitness = self.fitness + self.trajet[i].calculateDistance(self.trajet[i + 1])
    return self.fitness

  def randomMutate(self, percentage):
    isMutate = random.random()
    if isMutate < percentage:
      first = random.randint(0, len(self.trajet) - 1)
      second = random.randint(0, len(self.trajet) - 1)
      self.trajet[first], self.trajet[second] = self.trajet[second], self.trajet[first]
    return

