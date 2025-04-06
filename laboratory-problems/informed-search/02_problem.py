from searching_framework import Problem, astar_search

class Maze(Problem):
    def __init__(self, initial, goal, walls, n):
        super().__init__(initial, goal)
        self.walls = walls
        self.n = n

    def successor(self, state):
        successors = {}
        x, y = state

        for step in [2, 3]:
            new_x = x + step
            new_y = y
            if 0 <= new_x < self.n and (new_x, new_y) not in self.walls:
                valid = True
                for i in range(1, step + 1):
                    if (x + i, y) in self.walls:
                        valid = False
                        break
                if valid:
                    successors[f"Desno {step}"] = (new_x, new_y)

        new_x = x
        new_y = y + 1
        if 0 <= new_y < self.n and (new_x, new_y) not in self.walls:
            successors["Gore"] = (new_x, new_y)

        new_x = x
        new_y = y - 1
        if 0 <= new_y < self.n and (new_x, new_y) not in self.walls:
            successors["Dolu"] = (new_x, new_y)

        new_x = x - 1
        new_y = y
        if 0 <= new_x < self.n and (new_x, new_y) not in self.walls:
            successors["Levo"] = (new_x, new_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        x1, y1 = node.state
        x2, y2 = self.goal
        return (abs(x1 - x2) + abs(y1 - y2)) / 3

if __name__ == '__main__':
    n = int(input())
    num_walls = int(input())
    walls = []
    for _ in range(num_walls):
        wall = tuple(map(int, input().split(',')))
        walls.append(wall)
    human = tuple(map(int, input().split(',')))
    house = tuple(map(int, input().split(',')))

    problem = Maze(human, house, walls, n)
    solution = astar_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("No solution found")
