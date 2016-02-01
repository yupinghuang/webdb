import random
import json

f = open('states.txt', 'rb')
states = list()

for line in f:
    states.append(line.rstrip())
states.remove('')


data = { x:list() for x in states}
for i in range(1950, 2013):
    for state in states:
        dem = random.random()
        rep = random.random()
        pop = 1.4*dem + 1.1*rep
        data[state].append( (dem, rep, pop) )

with open('test.json', 'wb') as out:
    json.dump(data, out)
