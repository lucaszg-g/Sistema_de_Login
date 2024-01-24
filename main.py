import defs
from colorama import init, Fore

init(autoreset=True)

while True:

    option = int(input(defs.print_colored_text(f'Select an option:\n\n0 - Register\n1 - Login\n2 - Leave\n-> ',
                                               Fore.LIGHTWHITE_EX)))
    if option == 2:
        print(defs.print_colored_text('Leaving de system...', Fore.LIGHTRED_EX))
        quit()

    username = input(defs.print_colored_text('Insert your username: ', Fore.LIGHTWHITE_EX))
    while len(username) < 5:
        print(defs.print_colored_text('The username must be longer than 5 characters.', Fore.RED))
        username = input(defs.print_colored_text('Insert your username: ', Fore.LIGHTWHITE_EX))

    password = input(defs.print_colored_text('Insert your password: ', Fore.LIGHTWHITE_EX))

    match option:
        case 0:
            defs.register(username, password)

        case 1:
            defs.login(username, password)
            if True:
                break
