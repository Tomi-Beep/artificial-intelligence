from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search


class Puzzle(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        """ *32
            415
            678"""
        successors = {}
        index = state.index("*")
        if index % 3 != 0:
            temp = list(state)
            temp[index], temp[index - 1] = temp[index - 1], temp[index]
            new_state = ''.join(temp)
            successors["Left"] = new_state

        if index % 3 != 2:
            temp = list(state)
            temp[index], temp[index + 1] = temp[index + 1], temp[index]
            new_state = ''.join(temp)
            successors["Right"] = new_state

        if not index in (6, 7, 8):
            temp = list(state)
            temp[index], temp[index + 3] = temp[index + 3], temp[index]
            new_state = ''.join(temp)
            successors["Down"] = new_state

        if not index in (0, 1, 2):
            temp = list(state)
            temp[index], temp[index - 3] = temp[index - 3], temp[index]
            new_state = ''.join(temp)
            successors["Up"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0
        for x, y in zip(node.state, self.goal):
            if x != y:
                counter += 1
        return counter


if __name__ == '__main__':
    initial = input()
    goal = input()
    puzzle = Puzzle(initial, goal)
    result1 = astar_search(puzzle)
    print(result1.solve())
    result2 = greedy_best_first_graph_search(puzzle)
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solve())
