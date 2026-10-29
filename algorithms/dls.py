from .common import initial_state, goal_state, successors

def dls(disks, limit, pegs, initial_peg, goal_peg):
    start = initial_state(disks, initial_peg)
    goal = goal_state(disks, goal_peg)
    path_moves = []
    path_states = {start}

    def visit(state, depth):
        if state == goal:
            return True
        if depth >= limit:
            return False

        for next_state, move in successors(state, pegs):
            if next_state in path_states:
                continue
            path_states.add(next_state)
            path_moves.append(move)
            if visit(next_state, depth + 1):
                return True
            path_moves.pop()
            path_states.remove(next_state)
        return False

    if visit(start, 0):
        return list(path_moves)
    return None