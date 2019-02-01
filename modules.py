def simple_wires(wires,bomb_vars): #simple wires (p5 on manual)
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
