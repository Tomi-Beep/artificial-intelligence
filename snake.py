from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def in_obstacles(snake, red_apples):
    head = snake[-1]
    if head in snake[:-1] or head in red_apples or head[0] > 9 or head[0] < 0 or head[1] > 9 or head[1] < 0:
        return True
    return False


def move_right(snake, direction, green_apples):
    head = snake[-1]
    snake = snake[:]
    green_apples = green_apples[:]
    if direction == 'right':
        direction = 'down'
        snake.append((head[0], head[1] - 1))
    elif direction == 'left':
        direction = 'up'
        snake.append((head[0], head[1] + 1))
    elif direction == 'down':
        direction = 'left'
        snake.append((head[0] - 1, head[1]))
    elif direction == 'up':
        direction = 'right'
        snake.append((head[0] + 1, head[1]))

    if snake[-1] in green_apples:
        green_apples.remove(snake[-1])
    else:
        snake = snake[1:]

    return snake, direction, green_apples


def move_left(snake, direction, green_apples):
    head = snake[-1]
    snake = snake[:]
    green_apples = green_apples[:]

    if direction == 'right':
        direction = 'up'
        snake.append((head[0], head[1] + 1))

    elif direction == 'left':
        direction = 'down'
        snake.append((head[0], head[1] - 1))

    elif direction == 'down':
        direction = 'right'
        snake.append((head[0] + 1, head[1]))

    elif direction == 'up':
        direction = 'left'
        snake.append((head[0] - 1, head[1]))

    if snake[-1] in green_apples:
        green_apples.remove(snake[-1])
    else:
        snake = snake[1:]

    return snake, direction, green_apples


def forward(snake, direction, green_apples):
    head = snake[-1]
    snake = snake[:]
    green_apples = green_apples[:]

    if direction == 'right':
        snake.append((head[0] + 1, head[1]))

    elif direction == 'left':
        snake.append((head[0] - 1, head[1]))

    elif direction == 'down':
        snake.append((head[0], head[1] - 1))

    elif direction == 'up':
        snake.append((head[0], head[1] + 1))

    if snake[-1] in green_apples:
        green_apples.remove(snake[-1])
    else:
        snake = snake[1:]

    return snake, direction, green_apples


class Snake(Problem):
    def __init__(self, red_apples, initial, goal=None):
        super().__init__(initial, goal)
        self.red_apples = red_apples

    def successor(self, state):
        successors = {}
        # state = snake, green, direction
        snake = list(state[0])
        green = list(state[2])
        direction = state[1]

        move = move_right(snake, direction, green)
        if not in_obstacles(move[0], self.red_apples):
            successors["SvrtiDesno"] = (tuple(move[0]), move[1], tuple(move[2]))

        move = move_left(snake, direction, green)
        if not in_obstacles(move[0], self.red_apples):
            successors["SvrtiLevo"] = (tuple(move[0]), move[1], tuple(move[2]))

        move = forward(snake, direction, green)
        if not in_obstacles(move[0], self.red_apples):
            successors["ProdolzhiPravo"] = (tuple(move[0]), move[1], tuple(move[2]))
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__ == '__main__':
    n = int(input())
    green = []
    red = []
    for i in range(n):
        green.append(tuple([int(num) for num in input().split(',')]))

    n = int(input())
    for i in range(n):
        red.append(tuple([int(num) for num in input().split(',')]))

    initial_state = (((0, 9), (0, 8), (0, 7)), 'down', tuple(green))
    snake = Snake(red, initial_state)
    solution = breadth_first_graph_search(snake)
    if solution is not None:
        print(solution.solution())
