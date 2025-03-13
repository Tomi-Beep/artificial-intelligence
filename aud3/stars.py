from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def k1(k_x, k_y, b_x, b_y):
    move_x = k_x - 1
    move_y = k_y + 2
    if (move_x != b_x or move_y != b_y) and move_x >= 0 and move_y <= 7:
        return move_x, move_y
    return k_x, k_y


def k2(k_x, k_y, b_x, b_y):
    move_x = k_x + 1
    move_y = k_y + 2
    if (move_x != b_x or move_y != b_y) and move_x <= 7 and move_y <= 7:
        return move_x, move_y
    return k_x, k_y


def k3(k_x, k_y, b_x, b_y):
    move_x = k_x + 2
    move_y = k_y + 1
    if (move_x != b_x or move_y != b_y) and move_x <= 7 and move_y <= 7:
        return move_x, move_y
    return k_x, k_y


def k4(k_x, k_y, b_x, b_y):
    move_x = k_x + 2
    move_y = k_y - 1
    if (move_x != b_x or move_y != b_y) and move_x <= 7 and move_y >= 0:
        return move_x, move_y
    return k_x, k_y


def k5(k_x, k_y, b_x, b_y):
    move_x = k_x + 1
    move_y = k_y - 2
    if (move_x != b_x or move_y != b_y) and move_x <= 7 and move_y >= 0:
        return move_x, move_y
    return k_x, k_y


def k6(k_x, k_y, b_x, b_y):
    move_x = k_x - 1
    move_y = k_y - 2
    if (move_x != b_x or move_y != b_y) and move_x >= 0 and move_y >= 0:
        return move_x, move_y
    return k_x, k_y


def k7(k_x, k_y, b_x, b_y):
    move_x = k_x - 2
    move_y = k_y - 1
    if (move_x != b_x or move_y != b_y) and move_x >= 0 and move_y >= 0:
        return move_x, move_y
    return k_x, k_y


def k8(k_x, k_y, b_x, b_y):
    move_x = k_x - 1
    move_y = k_y + 1
    if (move_x != b_x or move_y != b_y) and move_x >= 0 and move_y <= 7:
        return move_x, move_y
    return k_x, k_y


def b1(b_x, b_y, k_x, k_y):
    move_x = b_x - 1
    move_y = b_y + 1
    if (move_x != k_x or move_y != k_y) and move_x >= 0 and move_y <= 7:
        return move_x, move_y
    return b_x, b_y


def b2(b_x, b_y, k_x, k_y):
    move_x = b_x + 1
    move_y = b_y + 1
    if (move_x != k_x or move_y != k_y) and move_x <= 7 and move_y <= 7:
        return move_x, move_y
    return b_x, b_y


def b3(b_x, b_y, k_x, k_y):
    move_x = b_x - 1
    move_y = b_y - 1
    if (move_x != k_x or move_y != k_y) and move_x >= 0 and move_y >= 0:
        return move_x, move_y
    return b_x, b_y


def b4(b_x, b_y, k_x, k_y):
    move_x = b_x + 1
    move_y = b_y - 1
    if (move_x != k_x or move_y != k_y) and move_x <= 7 and move_y >= 0:
        return move_x, move_y
    return b_x, b_y


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial)

    def successor(self, state):
        successors = dict()

        k_x = state[0]
        k_y = state[1]
        b_x = state[2]
        b_y = state[3]
        stars = state[4]

        move = k1(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K1'] = (
            move[0], move[1], b_x, b_y, tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = k2(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K2'] = (
            move[0], move[1], b_x, b_y, tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = k3(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K3'] = (
            move[0], move[1], b_x, b_y, tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = k4(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K4'] = (
            move[0], move[1], b_x, b_y, tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = k5(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K5'] = (
            move[0], move[1], b_x, b_y, tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = k6(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K6'] = (
            move[0], move[1], b_x, b_y, tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = k7(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K7'] = (
            move[0], move[1], b_x, b_y, tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = k8(k_x, k_y, b_x, b_y)
        if (k_x, k_y) != move:
            successors['K8'] = (move[0], move[1], b_x, b_y, tuple(stars))

        move = b1(b_x, b_y, k_x, k_y)
        if (b_x, b_y) != move:
            successors['B1'] = (
            k_x, k_y, move[0], move[1], tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = b2(b_x, b_y, k_x, k_y)
        if (b_x, b_y) != move:
            successors['B2'] = (
            k_x, k_y, move[0], move[1], tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = b3(b_x, b_y, k_x, k_y)
        if (b_x, b_y) != move:
            successors['B3'] = (
            k_x, k_y, move[0], move[1], tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        move = b4(b_x, b_y, k_x, k_y)
        if (b_x, b_y) != move:
            successors['B4'] = (
            k_x, k_y, move[0], move[1], tuple([s for s in stars if s[0] != move[0] or s[1] != move[1]]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__ == '__main__':
    knight = [int(input()), int(input())]
    bishop = [int(input()), int(input())]
    stars = ((int(input()), int(input())), (int(input()), int(input())), (int(input()), int(input())))
    initial_state = (knight[0], knight[1], bishop[0], bishop[1], stars)
    stars = Stars(initial_state)
    result = breadth_first_graph_search(stars)
    print(result.solution())
