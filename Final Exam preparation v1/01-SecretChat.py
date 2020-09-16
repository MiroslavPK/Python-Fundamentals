message = input()

while True:
    tokens = input().split(":|:")
    command = tokens[0]

    if command == "Reveal":
        break

    if command == "InsertSpace":
        index = int(tokens[1])

        message = message[:index] + " " + message[index:]

        print(message)

    elif command == "Reverse":
        substring = tokens[1]

        if substring not in message:
            print("error")
            continue

        message = message.replace(substring, "", 1)
        message += substring[::-1]

        print(message)

    elif command == 'ChangeAll':
        substring, replacement = tokens[1], tokens[2]

        if substring not in message:
            continue

        message = message.replace(substring, replacement)

        print(message)

print(f'You have a new text message: {message}')
