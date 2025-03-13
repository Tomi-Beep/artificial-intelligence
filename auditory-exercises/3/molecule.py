from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def is_obstacle(x, y):
    obstacles = [(0, 1), (1, 1), (1, 3), (2, 5), (3, 1), (3, 6), (4, 2),
                 (5, 6), (6, 1), (6, 2), (6, 3), (7, 3), (7, 6), (8, 5)]
    return (x, y) in obstacles


def move_right(x, y, x2, y2, x3, y3):
    while x < 8 and not is_obstacle(x + 1, y) and not (x + 1 == x2 and y == y2) and not (x + 1 == x3 and y == y3):
        x += 1
    return x


def move_left(x, y, x2, y2, x3, y3):
    while x > 0 and not is_obstacle(x - 1, y) and not (x - 1 == x2 and y == y2) and not (x - 1 == x3 and y == y3):
        x -= 1
    return x


def move_up(x, y, x2, y2, x3, y3):
    while y < 6 and not is_obstacle(x, y + 1) and not (x == x2 and y + 1 == y2) and not (x == x3 and y + 1 == y3):
        y += 1
    return y


def move_down(x, y, x2, y2, x3, y3):
    while y > 0 and not is_obstacle(x, y - 1) and not (x == x2 and y - 1 == y2) and not (x == x3 and y - 1 == y3):
        y -= 1
    return y


class Molecule(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        
        # Unpack the state tuple
        h1_x, h1_y, h2_x, h2_y, o_x, o_y = state
        
        # H1 movements
        new_x = move_right(h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if new_x != h1_x:
            successors["RightH1"] = (new_x, h1_y, h2_x, h2_y, o_x, o_y)
            
        new_x = move_left(h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if new_x != h1_x:
            successors["LeftH1"] = (new_x, h1_y, h2_x, h2_y, o_x, o_y)
            
        new_y = move_up(h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if new_y != h1_y:
            successors["UpH1"] = (h1_x, new_y, h2_x, h2_y, o_x, o_y)
            
        new_y = move_down(h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if new_y != h1_y:
            successors["DownH1"] = (h1_x, new_y, h2_x, h2_y, o_x, o_y)
        
        # H2 movements
        new_x = move_right(h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if new_x != h2_x:
            successors["RightH2"] = (h1_x, h1_y, new_x, h2_y, o_x, o_y)
            
        new_x = move_left(h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if new_x != h2_x:
            successors["LeftH2"] = (h1_x, h1_y, new_x, h2_y, o_x, o_y)
            
        new_y = move_up(h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if new_y != h2_y:
            successors["UpH2"] = (h1_x, h1_y, h2_x, new_y, o_x, o_y)
            
        new_y = move_down(h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if new_y != h2_y:
            successors["DownH2"] = (h1_x, h1_y, h2_x, new_y, o_x, o_y)
        
        # O movements
        new_x = move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if new_x != o_x:
            successors["RightO"] = (h1_x, h1_y, h2_x, h2_y, new_x, o_y)
            
        new_x = move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if new_x != o_x:
            successors["LeftO"] = (h1_x, h1_y, h2_x, h2_y, new_x, o_y)
            
        new_y = move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if new_y != o_y:
            successors["UpO"] = (h1_x, h1_y, h2_x, h2_y, o_x, new_y)
            
        new_y = move_down(o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if new_y != o_y:
            successors["DownO"] = (h1_x, h1_y, h2_x, h2_y, o_x, new_y)
        
        return successors

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        h1_x, h1_y, h2_x, h2_y, o_x, o_y = state
        # H1 O H2 in a row horizontally and all on same y-level
        return (h1_y == o_y == h2_y and 
                h1_x + 1 == o_x and 
                o_x + 1 == h2_x)


if __name__ == '__main__':
    h1_x = int(input())
    h1_y = int(input())
    h2_x = int(input())
    h2_y = int(input())
    o_x = int(input())
    o_y = int(input())
    
    # State is represented as (h1_x, h1_y, h2_x, h2_y, o_x, o_y)
    initial_state = (h1_x, h1_y, h2_x, h2_y, o_x, o_y)
    molecule = Molecule(initial_state)
    
    result = breadth_first_graph_search(molecule)
    print(result.solution())
    print(result.solve())
