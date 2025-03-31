from searching_framework import Problem, astar_search, greedy_best_first_graph_search


class House(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4),
                        (2, 4),
                        (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7), ]

    def successor(self, state):
        successors = {}
        person = state[0]
        house = state[1]
        direction = state[2]
        if direction == "desno":
            if house[0] == 4:
                house = (3, 8)
                direction = "levo"
            else:
                house = (house[0] + 1, 8)
        else:
            if house[0] == 0:
                house = (1, 8)
                direction = "desno"
            else:
                house = (house[0] - 1, 8)

        move = "Stoj"
        successors[move] = (person, house, direction)

        move = "Gore 1"
        new_person = (person[0], person[1] + 1)
        if (new_person in self.allowed or (new_person[1] == 8 and new_person[0] == house[0])) and new_person[0] >= 0 and \
                new_person[1] >= 0 and new_person[0] <= 4 and \
                new_person[1] <= 8:
            successors[move] = (new_person, house, direction)

        move = "Gore 2"
        new_person = (person[0], person[1] + 2)
        if (new_person in self.allowed or (new_person[1] == 8 and new_person[0] == house[0])) and new_person[0] >= 0 and \
                new_person[1] >= 0 and new_person[0] <= 4 and \
                new_person[1] <= 8:
            successors[move] = (new_person, house, direction)

        move = "Gore-desno 1"
        new_person = (person[0] + 1, person[1] + 1)
        if (new_person in self.allowed or (new_person[1] == 8 and new_person[0] == house[0])) and new_person[0] >= 0 and \
                new_person[1] >= 0 and new_person[0] <= 4 and \
                new_person[1] <= 8:
            successors[move] = (new_person, house, direction)

        move = "Gore-desno 2"
        new_person = (person[0] + 2, person[1] + 2)
        if (new_person in self.allowed or (new_person[1] == 8 and new_person[0] == house[0])) and new_person[0] >= 0 and \
                new_person[1] >= 0 and new_person[0] <= 4 and \
                new_person[1] <= 8:
            successors[move] = (new_person, house, direction)

        move = "Gore-levo 1"
        new_person = (person[0] - 1, person[1] + 1)
        if (new_person in self.allowed or (new_person[1] == 8 and new_person[0] == house[0])) and new_person[0] >= 0 and new_person[1] >= 0 and new_person[0] <= 4 and \
                new_person[1] <= 8:
            successors[move] = (new_person, house, direction)

        move = "Gore-levo 2"
        new_person = (person[0] - 2, person[1] + 2)
        if (new_person in self.allowed or (new_person[1] == 8 and new_person[0] == house[0])) and new_person[0] >= 0 and new_person[1] >= 0 and new_person[0] <= 4 and \
                new_person[1] <= 8:
            successors[move] = (new_person, house, direction)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        person = node.state[0]
        house = node.state[1]
        return ((8 - person[1]) + abs(house[0] - person[0])) / 5

    def goal_test(self, state):
        person = state[0]
        house = state[1]
        return person[1] == 8 and person[0] == house[0]


if __name__ == '__main__':
    entry = input().split(',')
    person = (int(entry[0]), int(entry[1]))
    entry = input().split(',')
    house = (int(entry[0]), int(entry[1]))
    direction = input()

    problem = House((person, house, direction))
    solution = greedy_best_first_graph_search(problem)

    if solution:
        print(solution.solution())
    else:
        print("No solution found")
