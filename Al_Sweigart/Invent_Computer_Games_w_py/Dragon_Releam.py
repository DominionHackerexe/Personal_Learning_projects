import random
import time

# Delay between text messages
SLEEP_TIME_SECONDS = 2

def dragonRealm():
    yes_input = ['yes', 'y']
    no_input = ['no', 'n']

    def displayIntro():
        print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')
        print()

    def chooseCave():
        cave = ''
        while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()

        return cave

    def shouldPlayAgain():
        while True:
            playAgain = input().lower()
            if playAgain not in (yes_input + no_input):
                print(f'Invaild input. Valid inputs are: {yes_input + no_input}.')
                continue
            if playAgain in yes_input:
                return True
            else:
                return False


    def checkCave(chosenCave):
        print('You approach the cave...')
        time.sleep(SLEEP_TIME_SECONDS)
        print('It is dark and spooky...')
        time.sleep(SLEEP_TIME_SECONDS)
        print('A large dragon jumps out in front of you! He opens his jaws and...')
        print()
        time.sleep(SLEEP_TIME_SECONDS)

        friendlyCave = random.randint(1, 2)

        if chosenCave == str(friendlyCave):
            print('Gives you his treasure!')
        else:
            print('Gobbles you down in one bite!')

    while True:
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)

        print('Do you want to play again? ([Y]es or [N]o)')
        
        if not shouldPlayAgain():
            break


dragonRealm()















































# import random
# import time

# def intro():
#     print('''You are in a land full of dragons. In front of you, 
#     you see two caves. In one cave, a dragon is friendly and will share his treasure with you. 
#     The other dragon is greedy and hungry, and will eat you on sight.''')
#     print()
#     print('In which cave will you go? (1 or 2)')
#     choice = input('> ')
#     return choice

# def choosen_cave(choice):
#     print('You approach the cave...')
#     time.sleep(2)
#     print('It is dark and spooky...')
#     time.sleep(2)
#     print('A large dragon jumps out in front of you! He opens his jaws and...')
#     print()
#     time.sleep(2)

#     friendly_cave = random.randint(1, 2)

#     if choice == str(friendly_cave):
#         print('Gives you his treasure!')
#     else:
#         print('Gobbles you down in one bite!')

# play_again = 'yes'
# while play_again.lower() == 'yes' or play_again.lower() == 'y':
#     print('Do you want to play again? (yes or no)')
#     play_again = input('> ')
#     if play_again.lower() == 'yes' or play_again.lower() == 'y':
#         print('Okay!')
#         intro()
#     else:
#         print('Thanks for playing!')
#         break