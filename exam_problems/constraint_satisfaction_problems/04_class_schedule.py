from constraint import *


def differentTime(time1, time2):
    return extract_hour(time1) != extract_hour(time2)

def extract_day(slot):
    return slot.split("_")[0]


def extract_hour(slot):
    return int(slot.split("_")[1])

def twoHours(time1, time2):
    if extract_day(time1) == extract_day(time2):
        return abs(extract_hour(time1) - extract_hour(time2)) >= 2
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    variables1 = []
    variables2 = []
    variables3 = []
    variables4 = []

    for i in range(int(casovi_AI)):
        variables1.append(f"AI_cas_{i + 1}")
    for i in range(int(casovi_ML)):
        variables2.append(f"ML_cas_{i + 1}")
    for i in range(int(casovi_R)):
        variables3.append(f"R_cas_{i + 1}")
    for i in range(int(casovi_BI)):
        variables4.append(f"BI_cas_{i + 1}")

    problem.addVariables(variables1, AI_predavanja_domain)
    problem.addVariables(variables2, ML_predavanja_domain)
    problem.addVariables(variables3, R_predavanja_domain)
    problem.addVariables(variables4, BI_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    full = variables1 + variables2 + variables3 + variables4 + ["AI_vezbi", "ML_vezbi", "BI_vezbi"]
    for i in full:
        for j in full:
            if j == i:
                continue
            problem.addConstraint(twoHours, (i, j))

    for i in variables2:
        problem.addConstraint(differentTime, (i, "ML_vezbi"))
    # ----------------------------------------------------

    solution = problem.getSolution()

    print(solution)
