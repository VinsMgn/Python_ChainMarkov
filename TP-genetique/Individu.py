import random
import string
from difflib import SequenceMatcher



class Individu:

  def __init__(self, targetWord, defaultValue=None):
    super().__init__()
    if defaultValue is not None:
      self.word = defaultValue
    else:
      self.word = self.generateWord(len(targetWord))
    self.generateFitness(targetWord)

  
  def generateWord(self, length):
    letters = string.printable
    return ''.join(random.choice(letters) for i in range(length))

  def generateFitness(self, targetWord):
    self.fitness = SequenceMatcher(None, self.word, targetWord).ratio()
    return self.fitness

  def randomMutation(self, percentage):
    isMutate = random.random()
    if isMutate < percentage:
      pos = random.randint(0, len(self.word))
      letters = string.ascii_lowercase + ' '
      oldWord = self.word
      self.word = self.word[:pos] + random.choice(letters) + self.word[pos + 1 :]
    return
