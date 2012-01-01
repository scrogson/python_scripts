import random
import time

def intro():
    return """
    You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight. 
    """

def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go into? (1 or 2) >> ')
    return cave

def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    time.sleep(2) 

    friendly = random.randint(1, 2)
    
    if chosen_cave == str(friendly):
        print('Gives you his treasure')
    else:
        print('Gobbles you down in one bite!')
    
replay = 'yes'
while replay == 'yes' or replay == 'y':
    print(intro())
    choice = choose_cave()
    check_cave(choice)
    replay = input('Do you want to play again? [yn] >> ')
