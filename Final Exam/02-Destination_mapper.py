import re

pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'

text = input()
valid_places = []
travel_points = 0

matches = re.findall(pattern, text)

for match in matches:
    valid_places.append(match[1])
    travel_points += len(match[1])

print(f'Destinations: {", ".join(valid_places)}')
print(f'Travel Points: {travel_points}')
