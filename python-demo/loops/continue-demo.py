while True:
    print('Who are you?')
    name = input()
    if name.lower() != 'joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.') 