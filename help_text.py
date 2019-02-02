help_text = '''Available commands:
    Meta Commands:
        done, failed, strike, help, update, show_vars
    Module Commands:
        wires, button, symbols, simon
Type 'help' followed by a command to see how that command works
Type 'help short' for a list of short colour names (for faster typing)'''

help_specifics = {'short':'Colour short names: Blue (bu), Red (r), White (w), Green (g), Yellow (y), Black (bk)',
             'wires':'Usage "wires colour1 colour2 etc."',
             'button':'Usage "button colour text"',
             'symbols':'Match each symbol to its number using the image provided\nUsage "symbols number1 number2 number 3 number 4"',
             'simon':'Input a colour sequence to recieve the corresponding sequence\nUsage "simon colour1 colour2 etc."',
             'done':'Quits program with success message',
             'failed':'Quits program with failure message',
             'strike':'Adds or removes a strike\nUsage "strike add/remove"',
             'update':'Reprompts for bomb variables',
             'show_vars':'Displays bomb variables'}
