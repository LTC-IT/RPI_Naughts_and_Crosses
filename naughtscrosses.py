from sense_emu import SenseHat

sense = SenseHat()

'''
TODO
Problems to solve - no particular order
1 - //Move between "cells"
2 - Select a cell (not an existing cells)
3 - Indicate which is X and which is O
4 - swap between players
5 - Detect "win"
6 - Detect "loss" when drawn.
'''

def draw_hash():
    b = [0,0,0]
    w = [255,255,255]
    
    grid = [
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b
    ]
    
    sense.set_pixels(grid)
    
def highlight_cell(id):
    g = [0,255,0]
    b = [0,0,0]
    w = [255,255,255]
    
    if id == 0:
        grid = [
    g,g,w,b,b,w,b,b,    
    g,g,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b
    ]
    elif id == 1:
        grid = [
    b,b,w,g,g,w,b,b,    
    b,b,w,g,g,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b
    ]
    elif id == 2:
        grid = [
    b,b,w,b,b,w,g,g,    
    b,b,w,b,b,w,g,g,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b
    ]
    elif id == 3:
        grid = [
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    g,g,w,b,b,w,b,b,    
    g,g,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b
    ]
    elif id == 4:
        grid = [
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,g,g,w,b,b,    
    b,b,w,g,g,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b
    ]
    elif id == 5:
        grid = [
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,g,g,    
    b,b,w,b,b,w,g,g,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b
    ]
    elif id == 6:
        grid = [
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    g,g,w,b,b,w,b,b,    
    g,g,w,b,b,w,b,b
    ]
    elif id == 7:
        grid = [
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,g,g,w,b,b,    
    b,b,w,g,g,w,b,b
    ]
    elif id == 8:
        grid = [
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,b,b,    
    b,b,w,b,b,w,b,b,
    w,w,w,w,w,w,w,w,
    b,b,w,b,b,w,g,g,    
    b,b,w,b,b,w,g,g
    ] 
    
    sense.set_pixels(grid)

def initialise_game_grid():
    global game_grid
    # 0 = not selected
    # 1 = O selected
    # 2 = X selected
    
    game_grid = [0,0,0,0,0,0,0,0,0]
    
def select_cells():
    '''
    ids of the cells
    0,1,2,
    3,4,5,
    6,7,8
    '''
    
    current_id = -1
    
    while True:
        event = sense.stick.wait_for_event()
        if event.action == "pressed":
            #print("The joystick was {} {}".format(event.action, event.direction))
            # first move
            if event.direction == "right":
                current_id = current_id + 1
                if current_id == 9:
                    current_id = 0
            if event.direction == "middle":
                # store the id of the cell selected
                game_grid[current_id] = 99
                print(game_grid)
            
            # print current_id
            print(current_id)
            highlight_cell(current_id)
     

initialise_game_grid()
draw_hash()
select_cells()


