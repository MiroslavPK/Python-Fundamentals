trip = input()

while True:
    command, *other = input().split(':')

    if command == 'Travel':
        break

    if command == 'Add Stop':
        index, string = int(other[0]), other[1]

        if len(trip) > index >= 0:
            trip = trip[:index] + string + trip[index:]
        print(trip)

    elif command == 'Remove Stop':
        start_index, end_index = int(other[0]), int(other[1])

        if len(trip) > (start_index and end_index) >= 0:
            trip = trip[:start_index] + trip[end_index + 1:]
        print(trip)

    elif command == 'Switch':
        old_string, new_string = other[0], other[1]

        if old_string in trip:
            trip = trip.replace(old_string, new_string)
        print(trip)

print(f'Ready for world tour! Planned stops: {trip}')
