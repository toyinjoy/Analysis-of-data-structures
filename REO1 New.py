# -*- coding: utf-8 -*-
"""
REO1
__author__: Oluwatoyin Joy Omole 
The data structure that was used is a matrix, printed row by row with the for statement.
The selection sort algorithim was used for sorting the degree list
"""

mat = [
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

for i in range(len(mat)): 
	print(mat[i])

#The list of each vertex Degree
Graph_Degree = [(0,3),(3,2),(4,2),(7,2),(5,2),(8,2),(1,2),(2,2),(6,2),(9,1)]

# Selection sort for the items in the list
def sorting(Graph_Degree):
	
	for i in range(len(Graph_Degree)-1):
		min_value = i
		for j in range(i+1,len(Graph_Degree)):
			if (Graph_Degree[j][1] < Graph_Degree[min_value][1]):
				min_value = j
		if min_value != i:
			temp = Graph_Degree[i]
			Graph_Degree[i] = Graph_Degree[min_value]
			Graph_Degree[min_value] = temp
	return Graph_Degree
print(sorting(Graph_Degree))
