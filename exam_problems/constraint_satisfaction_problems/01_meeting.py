from constraint import *

def checkMarija(vrednost, vreme):
    return vrednost == 1 and (vreme == 14 or vreme == 15 or vreme == 18) or vrednost == 0

def checkPetar(vrednost, vreme):
    return vrednost == 1 and (vreme == 12 or vreme == 13 or vreme == 16 or vreme == 17 or vreme == 18 or vreme == 19) or vrednost == 0

def checkSimona(vrednost,vreme):
    return vrednost == 1 and (vreme == 13 or vreme == 14 or vreme == 16 or vreme == 19)

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19])

    problem.addConstraint(lambda *a: sum(a) >= 2, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])
    problem.addConstraint(checkMarija,["Marija_prisustvo", "vreme_sostanok"])
    problem.addConstraint(checkSimona,["Simona_prisustvo", "vreme_sostanok"])
    problem.addConstraint(checkPetar,["Petar_prisustvo", "vreme_sostanok"])

    solutions = problem.getSolutions()
    for solution in solutions:
        reordered_solution = {
            'Simona_prisustvo': solution['Simona_prisustvo'],
            'Marija_prisustvo': solution['Marija_prisustvo'],
            'Petar_prisustvo': solution['Petar_prisustvo'],
            'vreme_sostanok': solution['vreme_sostanok']
        }
        print(reordered_solution)
    # [print(solution) for solution in problem.getSolutions()]
