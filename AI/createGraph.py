from main import find_astar_route
import re
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

def create_graph():
    fr = open("results/problems.csv", "r")
    the_problems_string = fr.read()
    the_problem = re.split("\n|,", the_problems_string)
    count = 0
    x_heuristic_time, y_real_time = [], []
    for i in range(100):
        source, target = int(the_problem[count]), int(the_problem[count + 1])
        count += 2
        sol, time, heuristic_time = find_astar_route(source, target)
        x_heuristic_time.append(heuristic_time)
        y_real_time.append(time)
    fr.close()

    plt.scatter(x_heuristic_time, y_real_time, marker='o');
    # plt.plot(x_heuristic_time, y_real_time)

    plt.xlabel('x - Heuristic time')
    plt.ylabel('y - Real Time')

    # giving a title to my graph
    plt.title('The Connection Between Heuristic and Real time')

    # function to show the plot
    plt.show()



if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    create_graph()