import math

def minMax(current,currentNode,maxTurn,targetNodes,depth,branch):
	
	if current == depth:
		return targetNodes[currentNode]
    
	if maxTurn:
		maxTurn = False
		l = []
		
		for x in range(branch):
			l.append(minMax(current + 1,currentNode * branch + (x),maxTurn,targetNodes,depth,branch))
		return max(l)

	
	else:
		maxTurn = True
		l = []
		
		for x in range(branch):
			l.append(minMax(current + 1,currentNode * branch + (x),maxTurn,targetNodes,depth,branch))
		return min(l)

if __name__ == "__main__":
	targetNodes = []

	noNodes = int(input("Enter Number of target nodes: "))
	branch = int(input("Enter the Branching Factor: "))
	
	depth = math.log(noNodes,branch)

	
	if depth == int(depth):
		print("Enter the Target Nodes: ")
		
		for i in range(noNodes):
			targetNodes.append(int(input()))
		
		maxTurn = bool(input("Write 'True' for Player's turn and 'False' for Computer's turn: "))
		
		print("The optimal value is : ", end = "")
		print(minMax(0,0,maxTurn,targetNodes,depth,branch))
	
	else:
		print("Cannot construct a complete tree out of it")