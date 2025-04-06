from searching_framework import *


# from utils import *
# from uninformed_search import *
# from informed_search import *

class Boxes(Problem):
    def __init__(self, n, boxes, initial, goal=None):
        super().__init__(initial, goal)
        self.n = n
        self.boxes = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == 0

    def successor(self, state):
        successors = {}

        x, y = state[0]
        remaining_balls = state[1]
        og = state[2]
        boxes_with_balls = list(state[2])

        # Move Up
        nx, ny = x, y + 1
        if self.check_valid(nx, ny, self.boxes):
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]:
                if (nx + dx, ny + dy) not in boxes_with_balls and (nx + dx, ny + dy) in self.boxes:
                    boxes_with_balls.append((nx + dx, ny + dy))
                    remaining_balls -= 1
            boxes_with_balls = tuple(boxes_with_balls)
            successors["Gore"] = ((nx, ny), remaining_balls, boxes_with_balls)

        # Move Right
        boxes_with_balls = list(og)
        remaining_balls = state[1]
        nx, ny = x + 1, y
        if self.check_valid(nx, ny, self.boxes):
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]:
                if (nx + dx, ny + dy) not in boxes_with_balls and (nx + dx, ny + dy) in self.boxes:
                    boxes_with_balls.append((nx + dx, ny + dy))
                    remaining_balls -= 1
            boxes_with_balls = tuple(boxes_with_balls)
            successors["Desno"] = ((nx, ny), remaining_balls, boxes_with_balls)



        return successors

    def check_valid(self, x, y, boxes):
        return 0 <= x < self.n and 0 <= y < self.n and not (x, y) in boxes


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    initial_state = (man_pos, num_boxes, ())
    problem = Boxes(n, tuple(boxes), initial_state)
    solution = breadth_first_graph_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("No Solution!")
