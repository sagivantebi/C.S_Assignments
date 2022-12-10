
from main import find_astar_route
import re


def solve_problems():
    with open('results/AStarRuns.txt', 'w', encoding='utf8', newline='') as fw:
        fr = open("results/problems.csv", "r")
        the_problems_string = fr.read()
        the_problem = re.split("\n|,", the_problems_string)
        count = 0
        for i in range(100):
            source, target = int(the_problem[count]), int(the_problem[count + 1])
            count += 2
            sol, time, heuristic_time = find_astar_route(source, target)
            sol_str = " ".join(str(x) for x in sol)
            fw.write(sol_str + " - " + str(time)[0:7] + " - " + str(heuristic_time)[0:7] + "\n")
        fr.close()


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    solve_problems()
