from .common import initial_state, goal_state, successors

def dfs(disks, pegs, initial_peg, goal_peg):
    start = initial_state(disks, initial_peg)
    goal = goal_state(disks, goal_peg)
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)

        next_states = list(successors(state, pegs))

        for next_state, move in reversed(next_states):
            if next_state not in visited:
                stack.append((next_state, path + [move]))
    return None