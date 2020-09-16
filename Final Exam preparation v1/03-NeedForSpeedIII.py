max_cars = int(input())
garage = {}

for _ in range(max_cars):
    car, mileage, fuel = input().split('|')

    if car not in garage:

        mileage = int(mileage)
        fuel = int(fuel)

        garage[car] = {}
        garage[car]['mileage'] = mileage
        garage[car]['fuel'] = fuel

while True:
    tokens = input().split(' : ')
    command = tokens[0]

    if command == 'Stop':
        break

    car = tokens[1]

    if command == 'Drive':

        distance, fuel = int(tokens[2]), int(tokens[3])

        if garage[car]['fuel'] < fuel:

            print('Not enough fuel to make that ride')
            continue

        garage[car]['mileage'] += distance
        garage[car]['fuel'] -= fuel

        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

        if garage[car]['mileage'] >= 100000:

            print(f'Time to sell the {car}!')
            del garage[car]

    elif command == 'Refuel':

        fuel = int(tokens[2])

        if garage[car]['fuel'] + fuel > 75:

            fuel = 75 - garage[car]['fuel']

        garage[car]['fuel'] += fuel

        print(f'{car} refueled with {fuel} liters')

    elif command == 'Revert':

        kms_reverted = int(tokens[2])

        if garage[car]['mileage'] - kms_reverted < 10000:

            garage[car]['mileage'] = 10000
            continue

        garage[car]['mileage'] -= kms_reverted

        print(f'{car} mileage decreased by {kms_reverted} kilometers')

sort_key = lambda item: (-garage[item]['mileage'], item)

[print(f'{car} -> Mileage: {garage[car]["mileage"]} kms, Fuel in the tank: {garage[car]["fuel"]} lt.')
 for car in sorted(garage, key=sort_key)]
