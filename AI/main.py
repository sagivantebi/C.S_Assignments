from Node import Node
from RoutingProblem import RoutingProblem
from best_first_graph_search import best_first_graph_search
from load_roads import roads, compute_distance


def heuristic_function(lat1, lon1, lat2, lon2):
    return compute_distance(lat1, lon1, lat2, lon2) / 110


def huristic_time_clac(problem):
    lat1 = problem.G[problem.s_start][1]
    lon1 = problem.G[problem.s_start][2]
    lat2 = problem.G[problem.goal][1]
    lon2 = problem.G[problem.goal][2]
    heuristic_time = heuristic_function(lat1, lon1, lat2, lon2)
    return heuristic_time


def find_ucs_rout(source, target):
    problem = RoutingProblem(source, target, roads)

    def g(node):
        return node.path_time

    return best_first_graph_search(problem, 0, g)


def find_astar_route(source, target):
    problem = RoutingProblem(source, target, roads)

    def g(node):
        return node.path_time

    def h(node):
        lat1 = problem.G[node.state][1]
        lon1 = problem.G[node.state][2]
        lat2 = problem.G[problem.goal][1]
        lon2 = problem.G[problem.goal][2]
        return heuristic_function(lat1, lon1, lat2, lon2)

    heuristic_time = huristic_time_clac(problem)
    return best_first_graph_search(problem, heuristic_time, f=lambda n: g(n) + h(n))


def DFS_Counter(node, f_limit, problem,heuristic_time):
    time_node = node.path_time + heuristic_time
    if time_node > f_limit:
        return None, time_node
    if problem.is_goal(node.state):
        return node.solution(), time_node
    next_f = float("inf")
    for child in node.expand(problem):
        solution, new_f = DFS_Counter(child, f_limit, problem,heuristic_time)
        if solution is not None:
            return solution, f_limit
        next_f = min(next_f, new_f)
    return None, next_f


def find_idastar_route(source, target):
    problem = RoutingProblem(source, target, roads)
    root = Node(problem.s_start)
    heuristic_time = huristic_time_clac(problem)
    f_limit = 0
    while True:
        solution, f_limit = DFS_Counter(root, f_limit, problem,heuristic_time)
        if solution is not None:
            return solution
        if f_limit == -1:
            return None


def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv

    dispatch(argv)
