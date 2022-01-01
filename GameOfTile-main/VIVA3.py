from collections import deque
 
class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list 
 
    def get_neighbors(self, v):
        return self.adjacency_list [v]

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
 
    def a_star_algorithm(self, start, stop):
     
        open_lst = set([start])
        closed_lst = set([])
 
       
        poo = {}
        poo[start] = 0
 
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v
 
            if n == None:
                print('Path does not exist!')
                return None
 
           
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('1: Path found: {}'.format(reconst_path))
                print('2: Open List: ', open_lst)
                print('Closed List: ', closed_lst)
                
                return reconst_path
 
          
            for (m, weight) in self.get_neighbors(n):
            
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None

adjacency_list = {
    'A':[('B', 1), ('C', 3), ('D', 7)],
    'B':[('D', 5)],
    'C':[('D', 12)],
    'D':[('E',6)],
    'E':[('F',1)],
    'F':[('G',2)],
    'G':[('H',3)],
    'H':[('E',4)]
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'E')