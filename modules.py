def short_to_long(colour): #changes short names to long names
    table = [['r','red'],['bu','blue'],['bk','black'],['y','yellow'],['g','green'],['w','white']]
    for x in table:
        colour = colour.replace(x[0],x[1])
    return colour

def simple_wires(wires,bomb_vars): #simple wires (p5 on manual)
    #usage "wires wire1 wire2 wire3..."
    serial = bomb_vars['serial']
    #3 wires
    if len(wires) == 3:
        if 'red' not in wires and 'r' not in wires:
            return 'Cut the second wire'
        elif wires[2] == 'white' or wires[2] == 'w':
            return 'Cut the last wire'
        elif wires.count('blue')+wires.count('bu') > 1:
            return 'Cut the last blue wire'
        else:
            return 'Cut the last wire'
    #4 wires
    elif len(wires) == 4:
        if serial % 2 != 0 and wires.count('red')+wires.count('r') > 1:
            return 'Cut the last red wire'
        elif (wires[3] == 'yellow' or wires[3] == 'y') and wires.count('red')+wires.count('r') == 0:
            return 'Cut the first wire'
        elif wires.count('blue')+wires.count('bu') == 1:
            return 'Cut the first wire'
        elif wires.count('yellow')+wires.count('y') > 1:
            return 'Cut the last wire'
        else:
            return 'Cut the second wire'
    #5 wires
    elif len(wires) == 5:
        if (wires[4] == 'black' or wires[4] == 'bk') and serial % 2 != 1:
            return 'Cut the fourth wire'
        elif wires.count('red')+wires.count('r') == 1 and wires.count('yellow')+wires.count('y') > 1:
            return 'Cut the first wire'
        elif wires.count('black')+wires.count('bk') == 0:
            return 'Cut the second wire'
        else:
            return 'Cut the first wire'
    #6 wires
    elif len(wires) == 6:
        if wires.count('yellow')+wires.count('y') == 0 and serial % 2 != 0:
            return 'Cut the third wire'
        elif wires.count('yellow')+wires.count('y') == 1 and wires.count('white')+wires.count('w') > 1:
            return 'Cut the fourth wire'
        elif wires.count('red')+wires.count('r') == 0:
            return 'Cut the last wire'
        else:
            return 'Cut the fourth wire'
    else:
        return 'Impossible combination of wires'

def button(button_vars,bomb_vars): #button (p6 manual)
    text = button_vars[1]
    colour = button_vars[0]
    #usage "button colour text"
    if (colour == 'blue' or colour == 'bu') and text == 'abort':
        return button_hold()
    elif bomb_vars['batteries'] > 1 and text == 'detonate':
        return 'Press and immediately release the button'
    elif (colour == 'white' or colour == 'w') and bomb_vars['car']:
        return button_hold()
    elif bomb_vars['batteries'] > 2 and bomb_vars['freak']:
        return 'Press and immediately release the button'
    elif colour == 'yellow' or colour == 'y':
        return button_hold()
    elif (colour == 'red' or colour == 'r') and text == 'hold':
        return 'Press and immediately release the button'
    else:
        return button_hold()

def button_hold(): #for when a button needs to be held down
    print 'Hold down the button'
    colour = raw_input('What colour is the lit strip (back to return to prompt)?: ')
    if colour == 'back':
        return 'Returning to prompt'
    elif colour == 'blue' or colour == 'bu':
        return 'Release button when the countdown timer has a 4 in any position'
    elif colour == 'white' or colour == 'w':
        return 'Release button when the countdown timer has a 1 in any position'
    elif colour == 'yellow' or colour == 'y':
        return 'Release button when the countdown timer has a 5 in any position'
    else:
        return 'Release button when the countdown timer has a 1 in any position'

def symbols(visible,bomb_vars): #symbols (p7 manual)
    #usage "symbols number1 number2 number3 number4" (ids found on help image)
    visible = [int(x) for x in visible]
    columns = [[1,2,3,4,5,6,7],
               [8,1,7,9,10,6,11],
               [12,13,9,14,15,3,10],
               [16,17,18,5,14,11,19],
               [20,19,18,21,17,22,23],
               [16,8,24,25,20,26,27]]
    #find the column
    for col in columns:
        found = True
        for symb in visible:
            if symb not in col:
                found = False
                break
        if found:
            break
    #check for impossible order
    if not found:
        return 'Impossible symbol combination'
    #order and serve
    visible = ', '.join([y[1] for y in sorted([[col.index(x),str(x)] for x in visible])])
    return 'Press the symbols in this order: '+visible

def simon(sequence,bomb_vars): #simon module (p8 of manual)
    strikes = bomb_vars['strikes']
    if bomb_vars['vowel']:
        table = {'red':['blue','yellow','green'],
                 'blue':['red','green','red'],
                 'green':['yellow','blue','yellow'],
                 'yellow':['green','red','blue']}
    else:
        table = {'red':['blue','red','yellow'],
                 'blue':['yellow','blue','green'],
                 'green':['green','yellow','blue'],
                 'yellow':['red','green','red']}
    new_seq = []
    for x in sequence:
        try:
            new_seq.append(table[short_to_long(x)][strikes])
        except:
            return 'Impossible combination'
    return 'New colour sequence: '+', '.join(new_seq)
