def ask_password():
    passw = '123'
    for i in range(3):
        password = input()
        if password == passw:
            return 'пароль принят!'
            break
    if password != passw: 
        return 'пароль не принят!'

ask_password()