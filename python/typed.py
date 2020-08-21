from rumblelib import *

def robot(state: State, unit: Obj):
    if state.turn % 2 == 0:
        return Action.attack(Direction.East)
    else:
        return Action.move(Direction.South)