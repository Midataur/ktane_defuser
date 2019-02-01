def simple_wires(wires,bomb_vars): #simple wires (p5 on manual)
    #usage "wires wire1 wire2 wire3..."
    serial = bomb_vars['serial']
    #3 wires
    if len(wires) == 3:
        if 'red' not in wires:
            return 'Cut the second wire'
        elif wires[2] == 'white':
            return 'Cut the last wire'
        elif wires.count('blue') > 1:
            return 'Cut the last blue wire'
        else:
            return 'Cut the last wire'
    #4 wires
    elif len(wires) == 4:
        if serial % 2 != 0 and wires.count('red') > 1:
            return 'Cut the last red wire'
        elif wires[3] == 'yellow' and wires.count('red') == 0:
            return 'Cut the first wire'
        elif wires.count('blue') == 1:
            return 'Cut the first wire'
        elif wires.count('yellow') > 1:
            return 'Cut the last wire'
        else:
            return 'Cut the second wire'
    #5 wires
    elif len(wires) == 5:
        if wires[4] == 'black' and serial % 2 != 1:
            return 'Cut the fourth wire'
        elif wires.count('red') == 1 and wires.count('yellow') > 1:
            return 'Cut the first wire'
        elif wires.count('black') == 0:
            return 'Cut the second wire'
        else:
            return 'Cut the first wire'
    #6 wires
    elif len(wires) == 6:
        if wires.count('yellow') == 0 and serial % 2 != 0:
            return 'Cut the third wire'
        elif wires.count('yellow') == 1 and wires.count('white') > 1:
            return 'Cut the fourth wire'
        elif wires.count('red') == 0:
            return 'Cut the last wire'
        else:
            return 'Cut the fourth wire'
    else:
        return 'Impossible combination of wires'

def button(button_vars,bomb_vars): #button (p6 manual)
    text = button_vars[1]
    colour = button_vars[0]
    #usage "button colour text"
    if colour == 'blue' and text == 'abort':
        return button_hold()
    elif bomb_vars['batteries'] > 1 and text == 'detonate':
        return 'Press and immediately release the button'
    elif colour == 'white' and bomb_vars['car']:
        return button_hold()
    elif bomb_vars['batteries'] > 2 and bomb_vars['freak']:
        return 'Press and immediately release the button'
    elif colour == 'yellow':
        return button_hold()
    elif colour == 'red' and text == 'hold':
        return 'Press and immediately release the button'
    else:
        return button_hold()

def button_hold(): #for when a button needs to be held down
    print 'Hold down the button'
    colour = raw_input('What colour is the lit strip (back to return to prompt)?: ')
    if colour == 'back':
        return 'Returning to prompt'
    elif colour == 'blue':
        return 'Release button when the countdown timer has a 4 in any position'
    elif colour == 'white':
        return 'Release button when the countdown timer has a 1 in any position'
    elif colour == 'yellow':
        return 'Release button when the countdown timer has a 5 in any position'
    else:
        return 'Release button when the countdown timer has a 1 in any position'
