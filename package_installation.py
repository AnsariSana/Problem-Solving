from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = defaultdict(list)

    def addEdge(self, source_vertex, dest_vertex):
        self.graph[source_vertex].append(dest_vertex)

    def installPackage(self, startpackage):
        queue = []
        stack = []
        queue.append(startpackage)
        stack.append(startpackage)

        while queue:
            current_package = queue.pop(0)
            for i in self.graph[current_package]:
                if not self.visited[i]:
                    if self.graph[i]:
                        stack.append(i)
                        queue.append(i)
                        self.visited[current_package] = True
                    else:
                        print(i, end=', ')
                else:
                    print("Cyclic")
                    return
            

        print(', '.join(stack[-1::-1]))

g1 = Graph()
# g1.addEdge('A', 'B')
# g1.addEdge('B', 'C')
# g1.addEdge('C', 'B')
# g1.addEdge('C', 'E')
# g1.addEdge('E', 'K')

g1.addEdge('A', 'B')
g1.addEdge('B', 'C')
g1.addEdge('C', 'D')
g1.addEdge('C', 'E')
g1.addEdge('E', 'K')


g1.installPackage('A')





