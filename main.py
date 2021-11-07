
class Graph:

    def __init__(self, vertexes):
        self.V = vertexes
        self.adj_list = {i: [] for i in range(1, vertexes+1)}
        self.SCC_count = 0
        self.id = 0
        self.ids = [None] * (vertexes+1)
        self.low = [None] * (vertexes+1)
        self.stack = []
        self.visited = []

    def add_edge(self, from_vert, to_vert):
        self.adj_list[from_vert].append(to_vert)

    def find_SCCs(self):
        for vert in self.adj_list.keys():
            if vert not in self.visited:
                self.dfs(vert)
        return self.low

    def dfs(self, at):
        self.stack.append(at)
        self.visited.append(at)
        self.ids[at] = self.low[at] = self.id
        self.id += 1

        for to in self.adj_list[at]:
            if to not in self.visited:
                self.dfs(to)
            if to in self.stack:
                self.low[at] = min(self.low[at], self.low[to])

        if self.ids[at] == self.low[at]:
            self.SCC_count += 1

            while len(self.stack) > 0:
                peek = self.stack.pop()
                if peek == at:
                    break


if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge(1, 5)
    graph.add_edge(5, 1)
    graph.add_edge(1, 2)
    graph.add_edge(5, 6)
    graph.add_edge(2, 6)
    graph.add_edge(3, 2)
    graph.add_edge(6, 3)
    graph.add_edge(6, 7)
    graph.add_edge(3, 7)
    graph.add_edge(3, 4)
    graph.add_edge(4, 7)
    graph.add_edge(7, 8)
    graph.add_edge(8, 4)
    print(graph.find_SCCs())

    graph2 = Graph(8)
    graph2.add_edge(1,5)
    graph2.add_edge(2,1)
    graph2.add_edge(5,2)
    graph2.add_edge(6,5)
    graph2.add_edge(6,2)
    graph2.add_edge(3,2)
    graph2.add_edge(6,7)
    graph2.add_edge(7,6)
    graph2.add_edge(4,3)
    graph2.add_edge(3,4)
    graph2.add_edge(7,3)
    graph2.add_edge(8,7)
    graph2.add_edge(8,4)
    graph2.add_edge(8,8)
    print(graph2.find_SCCs())
    print(graph2.SCC_count)