from modules import *
from help_text import *
from PIL import Image

print 'KTANE Defuser by Max Petschack'

def get_bomb_vars(strikes):
    batteries = int(raw_input('How many batteries on the bomb?: '))
    serial = int(raw_input("What's the last digit of the serial number?: "))
    vowel = True if raw_input('Is there a vowel in the serial number (y/n)?: ') == 'y' else False
    car = True if raw_input('Is there a lit CAR indicator on the bomb (y/n)?: ') == 'y' else False
    freak = True if raw_input('Is there a lit FRK indicator on the bomb (y/n)?: ') == 'y' else False
    parallel = True if raw_input('Is there a parallel port on the bomb (y/n)?: ') == 'y' else False
    bomb_vars = {'batteries':batteries,
                 'serial':serial,
                 'vowel':vowel,
                 'car':car,
                 'freak':freak,
                 'parallel':parallel,
                 'strikes':strikes}
    return bomb_vars

#setup tables
modules = {'wires':simple_wires,
           'button':button,
           'symbols':symbols,
           'simon':simon}

bomb_vars_lookup = [['batteries','Batteries:'],
                   ['serial','Last serial digit:'],
                   ['vowel','Vowel in serial:'],
                   ['car','Lit CAR indicator:'],
                   ['freak','Lit FRK indicator:'],
                   ['parallel','Parralel port:']]

#get the global variables
bomb_vars = get_bomb_vars(0)
strikes = 0

im = Image.open('ktanesymbols.png')

print 'Defuser ready'

while True:
    command = raw_input('Enter command: ').split()
    #to prevent breaking check empty
    command = command if len(command) > 0 else ['default']
    #Bomb commands (done, fail, add strike, etc)
    if command[0] == 'done':
        print 'We did it!'
        break
    elif command[0] == 'failed':
        print "We'll get it next time!"
        break
    elif command[0] == 'strike':
        if command[1] == 'add':
            strikes += 1
            bomb_vars['strikes'] = strikes
            print 'Added strike'
        elif commmand[1] == 'remove':
            strikes -= 1
            bomb_vars['strikes'] = strikes
            print 'Removed strike'
    #meta
    elif command[0] == 'help':
        #general help
        if len(command) == 1:
            print help_text
        #specific help
        elif command[1] in help_specifics:
            if command[1] == 'symbols':
                im.show()
            print help_specifics[command[1]]
        else:
            print 'That help page could not be found'
    elif command[0] == 'show_vars':
        for x in bomb_vars_lookup:
            print x[1],bomb_vars[x[0]]
    #update bomb variables without quitting
    elif command[0] == 'update':
        bomb_vars = get_bomb_vars(strikes)
    #modules
    elif command[0] in modules:
        print modules[command[0]](command[1:],bomb_vars)
    else:
        print 'Unknown command'
