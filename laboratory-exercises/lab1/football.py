from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def is_around_obstacle(ball, obstacles):
    for obstacle in obstacles:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if ball[0] == obstacle[0] + i and ball[1] == obstacle[1] + j:
                    return True
    return False


def check_valid(player, ball, obstacles):
    return 0 <= player[0] < 8 and 0 <= ball[0] < 8 and \
        0 <= player[1] < 6 and 0 <= ball[1] < 6 and \
        not is_around_obstacle(ball, obstacles) and \
        not (player in obstacles or ball in obstacles)


class Football(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = [(3, 3), (5, 4)]

    def successor(self, state):
        successors = dict()
        player = state[0]
        ball = state[1]

        # state = player, ball

        all_moves = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
        move_names = [
            "gore",
            "dolu",
            "desno",
            "gore-desno",
            "dolu-desno"
        ]

        for i in range(len(all_moves)):
            new_player = (player[0] + all_moves[i][0], player[1] + all_moves[i][1])
            if check_valid(new_player, ball, self.obstacles):
                if new_player[0] == ball[0] and new_player[1] == ball[1]:
                    new_ball = (ball[0] + all_moves[i][0], ball[1] + all_moves[i][1])
                    if check_valid(new_player, new_ball, self.obstacles):
                        successors["Turni topka " + move_names[i]] = (new_player, new_ball)
                else:
                    successors["Pomesti coveche " + move_names[i]] = (new_player, ball)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal


if __name__ == '__main__':
    player = tuple([int(i) for i in input().split(',')])
    ball = tuple([int(i) for i in input().split(',')])
    football = Football((player, ball), ((7, 2), (7, 3)))
    graf = breadth_first_graph_search(football)
    print(graf.solution()) if graf is not None else print("No Solution!")
