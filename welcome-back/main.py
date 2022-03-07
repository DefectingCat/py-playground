import json

filename = 'user.json'


def restore_user():
    try:
        with open(filename, 'r') as f:
            str = f.read()
            if (len(str) == 0):
                return None
            user = json.loads(str)
            return user
    except FileNotFoundError:
        return None
    else:
        return None


def save_user(user_name):
    def write_file():
        user = [user_name]
        with open(filename, 'w') as f:
            json.dump(user, f)

    try:
        exist_user = restore_user()
        if (exist_user != None):
            exist_user.append(user_name)
            with open(filename, 'w') as f:
                json.dump(exist_user, f)
        else:
            write_file()
    except FileNotFoundError:
        write_file()


while True:
    name = input("What's your name? (q = quit) \n")
    if name == 'q':
        break
    exist_user = restore_user()
    if exist_user != None and name in exist_user:
        print(f'Welcome back {name}!')
    else:
        save_user(name)
        print("We'll remember you when you come back.")
