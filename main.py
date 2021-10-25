import functools
from queue import PriorityQueue


def dijkstra(graph, start, n):
    adjacent_vertixes = PriorityQueue()
    adjacent_vertixes.put((0, start, None))
    distances = []
    sptSET = []
    parents = []

    while not adjacent_vertixes.empty():
        current = adjacent_vertixes.get()
        curr_name = current[1]
        curr_dist = current[0]
        prev = current[2]

        if curr_name not in sptSET:
            sptSET.append(curr_name)
            distances.append(curr_dist)
            parents.append(prev)
        elif curr_dist < distances[sptSET.index(curr_name)]:
            distances[sptSET.index(curr_name)] = curr_dist
            parents[sptSET.index(curr_name)] = prev

        if curr_name in graph:
            for vertex in graph[curr_name]:
                if vertex[0] not in sptSET:
                    adjacent_vertixes.put((curr_dist + vertex[1], vertex[0], curr_name))

    return sptSET, distances, parents


def find_way(vertex, sptSET, parents):

    way = []

    if vertex not in sptSET:
        return "There is no such vertex in graph😬!"

    while vertex is not None:
        way.append(vertex)
        vertex = parents[sptSET.index(vertex)]

    way.reverse()
    return way


if __name__ == "__main__":
    temp = input().split(" ")
    n = int(temp[0])
    s = int(temp[1])

    graph = dict()

    for i in range(n):
        temp = input().split(" ")

        from_vertex = int(temp[0])
        to_vertex = int(temp[1])
        weight = int(temp[2])

        if from_vertex not in graph:
            graph[from_vertex] = []

        graph[from_vertex].append([to_vertex, weight])

    sptSET, smallest_dist, parents = dijkstra(graph, s, n)

    average_dist = functools.reduce(lambda a, b: a+b, smallest_dist) / (len(smallest_dist)-1)
    print(average_dist)
    print(find_way(10, sptSET, parents))
