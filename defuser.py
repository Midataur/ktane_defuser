from modules import *

print 'KTANE Defuser by Max Petschack'

#get the global variables
batteries = int(raw_input('How many batteries on the bomb?: '))
serial = int(raw_input("What's the last digit of the serial number?: "))
vowel = True if raw_input('Is there a vowel in the serial number (y/n)?: ') == 'y' else False
car = True if raw_input('Is there a CAR indicator on the bomb (y/n)?: ') == 'y' else False
freak = True if raw_input('Is there a FRK indicator on the bomb (y/n)?: ') == 'y' else False
parallel = True if raw_input('Is there a parallel port on the bomb (y/n)?: ') == 'y' else False
strikes = 0


bomb_vars = {'batteries':batteries,
             'serial':serial,
             'vowel':vowel,
             'car':car,
             'freak':freak,
             'parallel':parallel,
             'strikes':strikes}

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
    #Figure out what module is being defused
    elif command[0] == 'wires':
        print simple_wires(command[1:],bomb_vars)
    elif command[0] == 'button':
        print button(command[1:],bomb_vars)
    else:
        print 'Unknown command'


