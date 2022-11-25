from main import find_idastar_route
import re

from ways import load_map_from_csv
from ways.draw import plot_path

# roads = load_map_from_csv()

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError('Please install matplotlib:  http://matplotlib.org/users/installing.html#windows')


def solve_problems():
    fr = open("results/problems.csv", "r")
    the_problems_string = fr.read()
    the_problem = re.split("\n|,", the_problems_string)
    count = 0
    # for i in range(10):
    source, target = int(the_problem[count]), int(the_problem[count + 1])
    count += 2
    # sol = find_idastar_route(127, 53)
    plt.title('From 874776 to 120')
    # sol, roads = find_idastar_route(659, 43)
    # sol, roads = find_idastar_route(79161, 864777)
    # sol, roads = find_idastar_route(279, 485)
    # sol, roads = find_idastar_route(6934, 122)
    # sol, roads = find_idastar_route(521289, 797672)
    # sol, roads = find_idastar_route(882484, 190)
    # If you want to run it you will have to send back the roads from idastar
    sol, roads = find_idastar_route(43, 46)

    plot_path(roads, sol)
    fr.close()
    plt.show()


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1

    solve_problems()
