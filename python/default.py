def robot(state, unit, debug):
    if state.turn % 2 == 0:
        return Action.move(Direction.East)
    else:
        return Action.attack(Direction.South)
