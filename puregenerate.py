v = [[] for i in range(100)]

def addEdge(x, y):
	v[x].append(y)
	v[y].append(x)

def printPath(stack):
	for i in range(len(stack) - 1):
		print(stack[i], end = " -> ")
	print(stack[-1])


def DFS(vis, x, y, stack):
	stack.append(x)
	if (x == y):

	
		printPath(stack)
		return
	vis[x] = True

	if (len(v[x]) > 0):
		for j in v[x]:
			
			if (vis[j] == False):
				DFS(vis, j, y, stack)
				
	del stack[-1]

def DFSCall(x, y, n, stack):
	
	
	vis = [0 for i in range(n + 1)]

	DFS(vis, x, y, stack)

n = int(input("Enter the number of nodes: "))
stack = []

m = int(input("Enter the number of edges: "))
for i in range(m):
 a=int(input("Enter first node: "))
 b=int(input("Enter second node: "))    
 addEdge(a, b)

s=int(input("SOURCE NODE: "))
t=int(input("DESTINATION NODE: "))
DFSCall(s, t, n, stack)
	

