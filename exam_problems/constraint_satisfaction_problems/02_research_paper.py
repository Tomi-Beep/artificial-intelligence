from constraint import *


def print_sorted_results(result):
    sorted_papers = []
    for key, value in result.items():
        sorted_papers.append((key, value))

    sorted_papers.sort(key=lambda x: int(x[0].split()[0].replace('Paper', '')))

    for paper_info, time_slot in sorted_papers:
        print(f"{paper_info}: {time_slot}")


def countTIfNum3(a):
    t1 = a.count('T1')
    t2 = a.count('T2')
    t3 = a.count('T3')
    return t1 <= 4 and t2 <= 4 and t3 <= 4


def countTIfNum4(a):
    t1 = a.count('T1')
    t2 = a.count('T2')
    t3 = a.count('T3')
    t4 = a.count('T4')
    return t1 <= 4 and t2 <= 4 and t3 <= 4 and t4 <= 4


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    variablesAI = []
    variablesML = []
    variablesNLP = []
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        if topic == 'AI':
            variablesAI.append(f"{title} ({topic})")
        elif topic == 'ML':
            variablesML.append(f"{title} ({topic})")
        elif topic == 'NLP':
            variablesNLP.append(f"{title} ({topic})")
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = []
    for key in papers.keys():
        variables.append(f"{key} ({papers[key]})")

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    if len(variablesAI) <= 4 and len(variablesAI) != 0:
        problem.addConstraint(AllEqualConstraint(), variablesAI)
    if len(variablesML) <= 4 and len(variablesML) != 0:
        problem.addConstraint(AllEqualConstraint(), variablesML)
    if len(variablesNLP) <= 4 and len(variablesNLP) != 0:
        problem.addConstraint(AllEqualConstraint(), variablesNLP)

    if num == 3:
        problem.addConstraint(lambda *x: countTIfNum3(x), variables)
    else:
        problem.addConstraint(lambda *x: countTIfNum4(x), variables)

    result = problem.getSolution()

    print_sorted_results(result)
