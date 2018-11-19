import random as rd

def play(grid) :
    mvmt = game.move_possible(grid)
    if mvmt[1] :
        return("d")
    elif mvmt[3] :
        return("b")
    else :
        return(rd.choice(["g","h"]))
pseudo="axel_le_bg"
