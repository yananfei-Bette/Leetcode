#Rover Control
def roverMove(size, cmds):
    location = [0,0]
    dicCmds = {'UP':[-1, 0], 'DOWN':[1, 0], 'LEFT':[0, -1], 'RIGHT':[0, 1]}
    for cmd in cmds:
        action = dicCmds[cmd]
        if location[0]+action[0]<0 or location[0]+action[0]>=size or location[1]+action[1]<0 or location[1]+action[1]>=size:
            continue
        else:
            location[0] += action[0]
            location[1] += action[1]
        #print(location)
    return location[0]*size+location[1]

cmds = ["RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"]
cmds2 = ["RIGHT", "UP", "DOWN", "LEFT", "LEFT", "DOWN", "DOWN"]
print(roverMove(4, cmds))
print('***********************')
print(roverMove(4, cmds2))
