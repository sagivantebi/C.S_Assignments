from ways import compute_distance


class RoutingProblem:

    def __init__(self, s_start, goal, G):
        self.s_start = s_start
        self.goal = goal
        # The graph
        self.G = G

    def actions(self, s):
        list_actions = []
        for link in self.G[s][3]:
            list_actions.append(link[1])
        return list_actions

    def succ(self, s, a):
        if a in self.G:
            return a
        raise ValueError(f'No route from {s} to {a}')

    def is_goal(self, s):
        return s == self.goal

    def step_cost_a(self, s, a):
        return compute_distance(self.G[s][1], self.G[s][2], self.G[a][1], self.G[a][2])

    def get_link(self, s, a):
        for link in self.G[s][3]:
            if link[1] == a:
                return link
        return None

    def step_cost(self, s, a):
        # The actual distance from link
        return self.get_link(s, a)[2] / 1_000

    def step_cost_heuristic(self, s, a):
        return self.get_link(s, a)[2]
