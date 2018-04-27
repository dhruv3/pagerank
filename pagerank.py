import sys
import numpy as np

n = 100
beta = 0.8
iterations = 50

def pagerank():
	adjList = dict()
	f = open("graph.txt")
	next = f.readline()
	while next != "":
		temp = next.split("\t")
		temp[0] = long(temp[0])
		temp[1] = long(temp[1])
		if temp[0] in adjList:
			adjList[temp[0]].append(temp[1])
		else:
			adjList[temp[0]] = []
			adjList[temp[0]].append(temp[1])
		next = f.readline()

	outDegree = []
	#this was required to initialize the list otherwise  error popped
	#couldn't access list based on index
	for i in range(0, n):
		outDegree.append(i)
	for key, value in adjList.iteritems():
		outDegree[key-1] = len(value)

	M = np.zeros((n,n))
	for key, value in adjList.iteritems():
		uniqList = list(set(value))
		for j in uniqList:
			M[j-1][key-1] = 1.0/outDegree[key-1]

	part1 = np.full((n,1), (1 - beta)/n)
	r = np.full((n,1), 1.0/n)

	for i in range(0, iterations):
		part2 =  beta * np.matmul(M,r)
		r = part1 + part2

	answer = []
	for i in range(n):
		answer.append([i,r[i]])

	answer = sorted(answer,key = lambda x: x[1])

	print(answer[:5])
	print(answer[95:])



pagerank()
