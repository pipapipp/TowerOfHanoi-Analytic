from .dls import dls

def ids(disks, pegs, initial_peg, goal_peg):
    max_depth = (2 ** disks) - 1
    for limit in range(max_depth + 1):
        result = dls(disks, limit, pegs, initial_peg, goal_peg)
        if result is not None:
            return result
    return None