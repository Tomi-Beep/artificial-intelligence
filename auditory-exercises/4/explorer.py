from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search


def check_valid(explorer, ob1, ob2):
    return not ((explorer[0], explorer[1]) == (ob1[0], ob1[1]) or (explorer[0], explorer[1]) == (ob2[0], ob2[1]))


class Explorer(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}
        # state = initial, obstacle1, obstacle2
        explorer = state[0]
        ob1 = state[1]
        ob2 = state[2]
        if ob1[2] == 1:
            if ob1[1] == 5:
                new_ob1 = (2, 4, -1)
            else:
                new_ob1 = (2, ob1[1] + 1, 1)
        else:
            if ob1[1] == 0:
                new_ob1 = (2, 1, 1)
            else:
                new_ob1 = (2, ob1[1] - 1, 1)

        if ob2[2] == 1:
            if ob2[1] == 5:
                new_ob2 = (5, 4, -1)
            else:
                new_ob2 = (5, ob2[1] + 1, 1)
        else:
            if ob2[1] == 0:
                new_ob2 = (5, 1, 1)
            else:
                new_ob2 = (5, ob2[1] - 1, 1)

        new_explorer = (explorer[0] + 1, explorer[1])
        if check_valid(new_explorer, new_ob1, new_ob2):
            successors["Right"] = (new_explorer, new_ob1, new_ob2)

        new_explorer = (explorer[0] - 1, explorer[1])
        if check_valid(new_explorer, new_ob1, new_ob2):
            successors["Left"] = (new_explorer, new_ob1, new_ob2)

        new_explorer = (explorer[0], explorer[1] + 1)
        if check_valid(new_explorer, new_ob1, new_ob2):
            successors["Up"] = (new_explorer, new_ob1, new_ob2)

        new_explorer = (explorer[0], explorer[1] - 1)
        if check_valid(new_explorer, new_ob1, new_ob2):
            successors["Down"] = (new_explorer, new_ob1, new_ob2)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal

    def h(self, node):
        x_man = node.state[0][0]
        y_man = node.state[0][1]
        x_house = self.goal[0]
        y_house = self.goal[1]

        return abs(x_man - x_house) + abs(y_man - y_house)


if __name__ == '__main__':
    initial = tuple([int(n) for n in input().split(',')])
    goal = tuple([int(n) for n in input().split(',')])
    obstacle1 = tuple([int(n) for n in input().split(',')])
    obstacle2 = tuple([int(n) for n in input().split(',')])
    explorer = Explorer((initial, obstacle1, obstacle2), goal)
    result = astar_search(explorer)
    print(result.solution())
