import random


class Itineraire:
    fitness = 0

    def __init__(self, chemin):
        super().__init__()
        self.chemin = chemin


    def randomMutation(self, percentage):
        mutate = random.random()
        if mutate < percentage:
            first = random.randint(0, len(self.chemin) - 1)
            second = random.randint(0, len(self.chemin) - 1)
            self.chemin[first], self.chemin[second] = self.chemin[second], self.chemin[first]
        return
