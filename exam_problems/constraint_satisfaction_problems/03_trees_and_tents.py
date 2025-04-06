from constraint import *


def areNotNeighbors(tent1, tent2):
    skros = True
    x1, y1 = tent1
    x2, y2 = tent2
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if x1 + i == x2 and y1 + j == y2:
                skros = False
                break
    return skros


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot

    n = int(input())
    trees = []
    for _ in range(n):
        trees.append(tuple(map(int, input().split())))

    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    variables = [i for i in range(n)]
    domain = [(i, j) for i in range(6) for j in range(6)]
    problem.addVariables(variables, domain)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------

    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(NotInSetConstraint(trees), variables)

    for i in range(n):
        for j in range(n):
            if i < j:
                problem.addConstraint(areNotNeighbors, (i, j))

    possible_tree_neighbor_spots = []
    for tree in trees:
        tx, ty = tree
        possible_tree_neighbor_spots.append((tx + 1, ty))
        possible_tree_neighbor_spots.append((tx - 1, ty))
        possible_tree_neighbor_spots.append((tx, ty + 1))
        possible_tree_neighbor_spots.append((tx, ty - 1))

    problem.addConstraint(InSetConstraint(possible_tree_neighbor_spots), variables)

    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----
    for key in solution.keys():
        print(f"{solution[key][0]} {solution[key][1]}")
