import random
import string
from difflib import SequenceMatcher



class Individu:

  def __init__(self, finalWord, defaultValue=None):
    super().__init__()
    if defaultValue is not None:
      self.word = defaultValue
    else:
      self.word = self.__generateWord(len(finalWord))
    self.genFitness(finalWord)

  
  def __generateWord(self, length):
    # letters = string.ascii_lowercase + ' '
    letters = string.printable
    return ''.join(random.choice(letters) for i in range(length))

  def genFitness(self, finalWord):
    self.fitness = SequenceMatcher(None, self.word, finalWord).ratio()
    # arrDiff = [i for i in range(len(self.word)) if self.word[i] != finalWord[i]]
    # self.fitness = 1 - (len(arrDiff) / len(finalWord))
    return self.fitness

  def randomMutate(self, percentage):
    isMutate = random.random()
    if isMutate < percentage:
      pos = random.randint(0, len(self.word))
      letters = string.ascii_lowercase + ' '
      old = self.word
      self.word = self.word[:pos] + random.choice(letters) + self.word[pos + 1 :]
    return
