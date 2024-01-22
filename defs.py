from colorama import init, Fore

# Initialize colorama
init(autoreset=True)


def print_colored_text(text, color):
    return f'{color}{text}'


def register(username, password):
    username_exists = False
    with open('user.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if stored_username == username:
                username_exists = True
                print(print_colored_text('System: Username Already registered.', Fore.RED))
                break
        if not username_exists:
            with open('user.txt', 'a'):
                file.write(f'{username}:{password}\n')
                print(print_colored_text('System: Username successfully registered.', Fore.GREEN))


def login(username, password):
    with open('user.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if stored_username == username and stored_password == password:
                print(print_colored_text('System: Logged in successfully.', Fore.GREEN))
                print(print_colored_text(f'System: Welcome {username}.', Fore.LIGHTBLUE_EX))
                return True
        print(print_colored_text('System: Username not exists.', Fore.RED))
        return False


# register('aaa', '231')
# login('aaa', '231')
