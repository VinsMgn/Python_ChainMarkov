import csv
import random
import itertools

wordList = []


# Fonction qui construit la chaine de markov, qui prend en entrée les données avec le niveau
def chainConstructor(data, n):
    chain = {
        '_depart': {},
        '_TownNames': set(data)
    }
    # Parcours de boucle pour spliter les données reçues et travailler sur les mots avec les enchaînements de lettre
    for word in data:
        splitWord = str(word) + '.'
        for i in range(0, len(splitWord) - n):
            tuple = splitWord[i:i + n]
            next = splitWord[i + 1:i + n + 1]

            # Différents tests pour construire le mot selon les lettres
            if tuple not in chain:
                entry = chain[tuple] = {}
            else:
                entry = chain[tuple]

            if i == 0:
                if tuple not in chain['_depart']:
                    chain['_depart'][tuple] = 1
                else:
                    chain['_depart'][tuple] += 1

            if next not in entry:
                entry[next] = 1
            else:
                entry[next] += 1
    return chain


def select_random_item(items):
    randomNumber = random.random() * sum(items.values())
    for item in items:
        randomNumber -= items[item]
        if randomNumber < 0:
            return item


def generate(chain):
    letter = select_random_item(chain['_depart'])
    result = [letter]

    while True:
        letter = select_random_item(chain[letter])
        lastChar = letter[-1]
        if lastChar == '.':
            break
        result.append(lastChar)

    generation = ''.join(result)
    if generation not in chain['_TownNames']:
        return generation
    else:
        return generate(chain)


# Exécution du programme principal, ouverture du csv, lecture et parsing du fichier, ajout dans tableau et construction de la chaine
with open('communes-01042019.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    counterLine = 0
    for row in csv_reader:
        wordList.append(row[6].split('-'))
        counterLine += 1
    wordArray = list(itertools.chain.from_iterable(wordList))
    chain = chainConstructor(wordArray, 7)

    print(generate(chain))
