import re

n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split('<->')

    if plant not in plants:
        plants[plant] = {}
        plants[plant]['rarity'] = 0
        plants[plant]['ratings'] = []
    plants[plant]['rarity'] += int(rarity)

while True:
    tokens = input().split(': ')
    command = tokens[0]

    # second option with regex - works a bit slower
    # tokens = re.split(r'([A-Za-z]+)[:] ([A-Za-z]+)( [\-] ([\d]+))*', input())
    # command = tokens[0] or tokens[1]

    if command == 'Exhibition':
        break

    # regex
    # plant, *other = tokens[2], tokens[4]
    plant, *other = tokens[1].split(' - ')

    if plant not in plants:
        print('error')
        continue

    if command == 'Rate':
        rating = int(other[0])
        plants[plant]['ratings'].append(rating)

    elif command == 'Update':
        rarity = int(other[0])
        plants[plant]['rarity'] = rarity

    elif command == 'Reset':
        plants[plant]['ratings'].clear()

for plant in plants:
    avg = 0

    total = sum(plants[plant]['ratings'])
    elements_count = len(plants[plant]['ratings'])

    if total > 0:
        avg = total / elements_count
    plants[plant]['rating'] = avg


sort_key = lambda item: (-plants[item]['rarity'], -plants[item]['rating'])

print('Plants for the exhibition:')

for plant in sorted(plants, key=sort_key):
    print(f'- {plant}; Rarity: {plants[plant]["rarity"]}; Rating: {plants[plant]["rating"]:.2f}')
