import random

def play():
    flip = random.choice(('heads', 'tails'))
    choice = input('heads or tails? [htq] >> ')

    if choice not in 'htq':
        print('Sorry, that\'s not an option')
    elif choice.lower()[:1] == flip[:1]:
        print('Win!')
    else:
        print('Sorry, it was ' + flip + '.')
    replay()

def replay():
    answer = input('\nWould you like to flip again? [yn] >> ')
    if answer.lower().startswith('y'): play()
    else: exit('\n\nThanks for playing. Goodbye!')

def title():
    title = """
     _                    _                    _        _ _     ___ 
    | |__   ___  __ _  __| |___    ___  _ __  | |_ __ _(_) |___/ _ \ 
    | '_ \ / _ \/ _` |/ _` / __|  / _ \| '__| | __/ _` | | / __\// /
    | | | |  __/ (_| | (_| \__ \ | (_) | |    | || (_| | | \__ \ \/ 
    |_| |_|\___|\__,_|\__,_|___/  \___/|_|     \__\__,_|_|_|___/ () 
                                                                   
    """
    return '\033[0;32m' + title + '\033[0m'

print(title())
play()
