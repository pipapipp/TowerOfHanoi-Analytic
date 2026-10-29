def initial_state(disks, initial_peg):
    return tuple(initial_peg for _ in range(disks))

def goal_state(disks, goal_peg):
    return tuple(goal_peg for _ in range(disks))

def successors(state, pegs):
    disks = len(state)
    top_disk = [None] * pegs

    for disk_index, peg in enumerate(state):
        if top_disk[peg] is None:
            top_disk[peg] = disk_index

    for source in range(pegs):
        disk_index = top_disk[source]
        if disk_index is None:
            continue
        for destination in range(pegs):
            if destination == source:
                continue
            destination_top = top_disk[destination]
           
            if destination_top is None or destination_top > disk_index:
                next_state = list(state)
                next_state[disk_index] = destination
                move = (disk_index + 1, source + 1, destination + 1)
                yield tuple(next_state), move

def reconstruct_path(parent, goal):
    moves = []
    state = goal
    while parent[state][0] is not None:
        previous, move = parent[state]
        moves.append(move)
        state = previous
    moves.reverse()
    return moves
