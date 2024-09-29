def who_are_you_and_hello():
    name = 0
    while name != 'Вася':
        name = input()
        if name == 'Вася':
            print('Привет, ', name)
        break

who_are_you_and_hello()