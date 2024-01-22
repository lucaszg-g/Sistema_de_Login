import defs

while True:
    username = input('Username: ')
    password = input('Password: ')
    option = int(input('Option: '))

    if option == 1:
        defs.register(username, password)
    elif option == 2:
        defs.login(username, password)
        if True:
            break
