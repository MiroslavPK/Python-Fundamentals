class Plant:
    def __init__(self, plant, rarity):
        self.plant = plant
        self.rarity = rarity
        self.__ratings = []

    def rate(self, rating):
        self.__ratings.append(rating)

    def update_rarity(self, new_rarity):
        self.rarity = new_rarity

    def delete_ratings(self):
        self.__ratings.clear()

    def get_avg_ratings(self):
        if not self.__ratings:
            return 0
        return sum(self.__ratings) / len(self.__ratings)

    def __repr__(self):
        return f'- {self.plant}; Rarity: {self.rarity}; Rating: {self.get_avg_ratings():.2f}'


n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split('<->')
    if plant not in plants:
        plants[plant] = Plant(plant, int(rarity))
    else:
        plants[plant].update_rarity(rarity)

while True:
    tokens = input().split(': ')
    command = tokens[0]

    if command == 'Exhibition':
        break

    plant, *other = tokens[1].split(' - ')

    if plant not in plants:
        print('error')
        continue

    if command == 'Rate':
        rating = int(*other)
        plants[plant].rate(rating)

    elif command == 'Update':
        rarity = int(*other)
        plants[plant].update_rarity(rarity)

    elif command == 'Reset':
        plants[plant].delete_ratings()


print('Plants for the exhibition:')
for plant in sorted(plants.values(), key=lambda item: (-item.rarity, -item.get_avg_ratings())):
    print(plant)
