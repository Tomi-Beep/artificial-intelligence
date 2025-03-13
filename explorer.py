from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [7, 5]

    def successor(self, state):
        successors = {}

        poz_x = state[0][0]
        poz_y = state[0][1]
        o1 = list(state[1])
        o2 = list(state[2])
        max_x = self.grid_size[0]
        max_y = self.grid_size[1]

        if o1[2] == -1:
            if o1[1] == 0:
                o1[2] = 1
                o1[1] += 1
            else:
                o1[1] -= 1
        else:
            if o1[1] == 5:
                o1[2] = -1
                o1[1] -= 1
            else:
                o1[1] += 1

        if o2[2] == -1:
            if o2[1] == 0:
                o2[2] = 1
                o2[1] += 1
            else:
                o2[1] -= 1
        else:
            if o2[1] == 5:
                o2[2] = -1
                o2[1] -= 1
            else:
                o2[1] += 1

        # akcii = ("Right", "Left", "Down", "Up")
        if not (poz_x + 1 == o1[0] and poz_y == o1[1]) and not (
                poz_x + 1 == o2[0] and poz_y == o2[1]) and poz_x < max_x:
            successors["Right"] = ((poz_x + 1, poz_y), tuple(o1), tuple(o2))

        if not (poz_x - 1 == o1[0] and poz_y == o1[1]) and not (poz_x - 1 == o2[0] and poz_y == o2[1]) and poz_x > 0:
            successors["Left"] = ((poz_x - 1, poz_y), tuple(o1), tuple(o2))

        if not (poz_x == o1[0] and poz_y + 1 == o1[1]) and not (
                poz_x == o2[0] and poz_y + 1 == o2[1]) and poz_y < max_y:
            successors["Up"] = ((poz_x, poz_y + 1), tuple(o1), tuple(o2))

        if not (poz_x == o1[0] and poz_y - 1 == o1[1]) and not (poz_x == o2[0] and poz_y - 1 == o2[1]) and poz_y > 0:
            successors["Down"] = ((poz_x, poz_y - 1), tuple(o1), tuple(o2))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0][0], state[0][1])
        return position == self.goal


if __name__ == '__main__':
    initial_state = (int(input()), int(input()))
    goal_state = (int(input()), int(input()))
    obstacle_1 = (2, 5, -1)  # down
    obstacle_2 = (5, 0, 1)  # up
    explorer = Explorer((initial_state, obstacle_1, obstacle_2), goal_state)
    print(breadth_first_graph_search(explorer).solution())
    print(breadth_first_graph_search(explorer).solve())
