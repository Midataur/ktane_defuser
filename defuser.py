from modules import *
from PIL import Image

print 'KTANE Defuser by Max Petschack'

#get the global variables
batteries = int(raw_input('How many batteries on the bomb?: '))
serial = int(raw_input("What's the last digit of the serial number?: "))
vowel = True if raw_input('Is there a vowel in the serial number (y/n)?: ') == 'y' else False
car = True if raw_input('Is there a lit CAR indicator on the bomb (y/n)?: ') == 'y' else False
freak = True if raw_input('Is there a lit FRK indicator on the bomb (y/n)?: ') == 'y' else False
parallel = True if raw_input('Is there a parallel port on the bomb (y/n)?: ') == 'y' else False
strikes = 0


bomb_vars = {'batteries':batteries,
             'serial':serial,
             'vowel':vowel,
             'car':car,
             'freak':freak,
             'parallel':parallel,
             'strikes':strikes}

help_text = '''Available commands:
    Meta Commands:
        done, failed, add strike, help
    Module Commands:
        wires, button, symbols
Type 'help' followed by a module command to see how that command works
Type 'help short' for a list of short colour names (for faster typing)'''
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
    elif command[0] == 'add':
        strikes += 1
        bomb_vars['strikes'] = strikes
        print 'Added strike'
        if strikes == 3:
            print '3 strikes, bomb failed'
            print "We'll get it next time!"
            break
    #meta
    elif command[0] == 'help':
        #general help
        if len(command) == 1:
            print help_text
        #specific help
        elif command[1] == 'short':
            print 'Colour short names: Blue (bu), Red (r), White (w), Green (g), Yellow (y), Black (bk)'
        elif command[1] == 'wires':
            print 'Usage "wires colour1 colour2 etc."'
        elif command[1] == 'button':
            print 'Usage "button colour text"'
        elif command[1] == 'symbols':
            im.show()
            print 'Match each symbol to its number using the image provided'
            print 'Usage "symbols number1 number2 number 3 number 4"'
        else:
            print 'That help page could not be found'
    #Figure out what module is being defused
    elif command[0] == 'wires':
        print simple_wires(command[1:],bomb_vars)
    elif command[0] == 'button':
        print button(command[1:],bomb_vars)
    elif command[0] == 'symbols':
        print symbols(command[1:])
    else:
        print 'Unknown command'


