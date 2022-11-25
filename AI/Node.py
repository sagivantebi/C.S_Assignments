from ways import info


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, path_time=0):
        self.state = state
        self.parent = parent
        self.action = state
        self.path_cost = path_cost
        # self.heuristic_cost = heuristic_cost
        self.path_time = path_time
        # self.heuristic_time = heuristic_time
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.succ(self.state, action)

        # current two points cost
        cost_step = problem.step_cost(self.state, action)
        # compute total cost
        next_cost = self.path_cost + cost_step

        next_link = problem.get_link(self.state, action)
        # maximum speed limit in this link
        speed = info.SPEED_RANGES[next_link[3]][1]

        link_time = cost_step / speed
        next_time = self.path_time + link_time

        # # current two points heuristic cost
        # cost_heuristic_step = problem.step_cost_a(self.state, action)
        # # compute total heuristic cost
        # next_heuristic_cost = self.heuristic_cost + cost_heuristic_step
        # maximum_road_speed = 111
        # link_heuristic_time = cost_heuristic_step / maximum_road_speed
        # next_heuristic_time = self.heuristic_time + link_heuristic_time

        # next_node = Node(next_state, self, action, next_cost, next_heuristic_cost, next_time, next_heuristic_time)
        next_node = Node(next_state, self, action, next_cost, next_time)

        return next_node

    def solution(self):
        list_1 = [node.action for node in self.path()]
        return list_1

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return f"<{self.state}>"

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.state)
