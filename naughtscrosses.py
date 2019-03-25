from sense_emu import SenseHat

sense = SenseHat()
player_one = True

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
    
    grid = [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0
        ]
    
    #These are the indexes of the LEDs in grid that need to be white for the hash
    hash = [2,5,10,13,16,17,18,19,20,21,22,23,26,29,34,37,40,41,42,43,44,45,46,47,50,53,58,61]
    
    starting_pixels = [0,3,6,24,27,30,48,51,54]
    
    for index in range (0,9):
        starting_pixel = starting_pixels[index]
        if game_grid[index] == 1:
            # something
        if game_grid[index] == 2:
            # another thing
    
    starting_pixel = starting_pixels[id]
    
    grid[starting_pixel] = g
    grid[starting_pixel+1] = g
    grid[starting_pixel+8] = g
    grid[starting_pixel+9] = g
    
    
    for index in range (0,64):
        if index in hash:
            grid[index] = w
        if grid[index] == 0:
            grid[index] = b
    
    #print(grid)
    
    sense.set_pixels(grid)

def initialise_game_grid():
    global game_grid
    # 0 = not selected
    # 1 = O selected
    # 2 = X selected
    
    game_grid = [0,0,0,0,0,0,0,0,0]
    
def select_cells():
    global player_one
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
                
                if player_one:
                    game_grid[current_id] = 1
                    player_one = False
                else:
                    game_grid[current_id] = 2
                    player_one = True
                
                print(game_grid)
            
            # print current_id
            print(current_id)
            highlight_cell(current_id)
     

initialise_game_grid()
draw_hash()
select_cells()


'''
if id == 0:
        grid[0] = g
        grid[1] = g
        grid[8] = g
        grid[9] = g
    if id == 1:
        grid[3] = g
        grid[4] = g
        grid[11] = g
        grid[12] = g
    if id == 2:
        grid[6] = g
        grid[7] = g
        grid[14] = g
        grid[15] = g
    if id == 3:
        grid[24] = g
        grid[25] = g
        grid[32] = g
        grid[33] = g
    if id == 4:
        grid[27] = g
        grid[28] = g
        grid[35] = g
        grid[36] = g
    if id == 5:
        grid[30] = g
        grid[31] = g
        grid[38] = g
        grid[39] = g
    if id == 6:
        grid[48] = g
        grid[49] = g
        grid[56] = g
        grid[57] = g
    if id == 7:
        grid[51] = g
        grid[52] = g
        grid[59] = g
        grid[60] = g
    if id == 8:
        grid[54] = g
        grid[55] = g
        grid[62] = g
        grid[63] = g
'''


