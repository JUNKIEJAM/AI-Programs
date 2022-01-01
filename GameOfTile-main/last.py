from collections import deque


class Graph:
 
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1 

    def h(self, n):
        H = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0,
            'G': 0,
            'H': 0
        }

        return H[n]
    
    def printAllPathsUtil(self, s, d, visited, path):
        
        visited[s] = True
	    path.append(s)

	    if s == d:
			print(path)
		else:

			for i in self.adjacency_list[s]:
				if visited[i[0]] == False:
					self.printAllPathsUtil(i[0], d, visited, path)

		path.pop()
		visited[s] = False

    
    def printAllPaths(self, s, d):
		
        visited = {
			'A':False,
			'B': False,
			'C': False,
			'D': False,
			'E': False,
			'F': False,
			'G': False,
			'H': False
		}
		
        path = []

		
        self.printAllPathsUtil(s, d, visited, path)

    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        closed_list = set([])

        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
         
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            
            print("Open List: ")
            print(open_list)
            open_list.remove(n)
            print("Closed List: ")
            print(closed_list)
            closed_list.add(n)
            
        print('Path does not exist!')
        return None
        
    
 