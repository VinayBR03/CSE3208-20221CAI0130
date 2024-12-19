# -*- coding: utf-8 -*-
"""AIP(exp1-Uninformed Search).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1btzn6GasEVLl8r5-QMw4ufHrJK-wB7uP
"""

#1. Breadth First Search
from queue import Queue
w = 10
romaniaMap = {
    'Arad': [('Timisoara', w), ('Zerind',w), ('Sibiu',w)],
    'Zerind': [('Arad',w), ('Oradea',w)],
    'Oradea': [('Zerind',w), ('Sibiu',w)],
    'Sibiu': [('Arad',w), ('Oradea',w), ('Fagaras',w), ('Rimnicu',w)],
    'Timisoara': [('Arad',w), ('Lugoj',w)],
    'Lugoj': [('Timisoara',w), ('Mehadia',w)],
    'Mehadia': [('Lugoj',w), ('Drobeta',w)],
    'Drobeta': [('Mehadia',w), ('Craiova',w)],
    'Craiova': [('Drobeta',w), ('Rimnicu',w), ('Pitesti',w)],
    'Rimnicu': [('Sibiu',w), ('Craiova',w), ('Pitesti',w)],
    'Fagaras': [('Sibiu',w), ('Bucharest',w)],
    'Pitesti': [('Rimnicu',w), ('Craiova',w), ('Bucharest',w)],
    'Bucharest': [('Fagaras',w), ('Pitesti',w), ('Giurgiu',w), ('Urziceni',w)],
    #'Bucharest': [],
    'Giurgiu': [('Bucharest',w)],
    'Urziceni': [('Vaslui',w), ('Hirsova',w), ('Bucharest',w)],
    'Hirsova': [('Urziceni',w), ('Eforie',w)],
    'Eforie': [('Hirsova',w)],
    'Vaslui': [('Iasi',w), ('Urziceni',w)],
    'Iasi': [('Vaslui',w), ('Neamt',w)],
    'Neamt': [('Iasi',w)]
}

from queue import Queue
def bfs(romaniaMap, startingNode, destinationNode):
    # For keeping track of what we have visited
    visited = {}
    # keep track of distance
    distance = {}
    # parent node of specific graph
    parent = {}

    bfs_traversal_output = []
    # BFS is queue based so using 'Queue' from python built-in
    queue = Queue()

    # travelling the cities in map
    for city in romaniaMap.keys():
        # since intially no city is visited so there will be nothing in visited list
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    # starting from 'Arad'
    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()     # first element of the queue, here it will be 'arad'
        bfs_traversal_output.append(u)

        # explore the adjust cities adj to 'arad'
        for (v,d) in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + d
                queue.put(v)

        # reaching our destination city i.e 'bucharest'
    g = destinationNode
    path = []
    if destinationNode not in visited:
      print("Wrong destination node.")
      return
    if not visited[destinationNode]:
      print("No path found")
      return
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    # printing the path to our destination city
    print("Path:", path)
    print("Distance:", distance[destinationNode])

bfs(romaniaMap, 'Arad', 'Bucharest')

from collections import deque

def dfs(romaniaMap, startingNode, destinationNode):
  # For keeping track of what we have visited
    visited = {}
    # keep track of distance
    distance = {}
    # parent node of specific graph
    parent = {}

    dfs_traversal_output = []
    # DFS is stack based so using 'Deque' from python built-in
    stack = deque()

    # travelling the cities in map
    for city in romaniaMap.keys():
        # since intially no city is visited so there will be nothing in visited list
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    # starting from 'Arad'
    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    stack.append(startingCity)

    while len(stack) != 0:
        u = stack.pop()     # first element of the queue, here it will be 'arad'
        dfs_traversal_output.append(u)

        # explore the adjust cities adj to 'arad'
        for (v,d) in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + d
                stack.append(v)

        # reaching our destination city i.e 'bucharest'
    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    # printing the path to our destination city
    print("Path:", path)
    print("Distance:", distance[destinationNode])

dfs(romaniaMap, 'Arad', 'Bucharest')

#Read the information from a file
#File format will be vertex->(Neighbour1,Distance1),(Neighbour2,Distance2)...(NeighbourN,DistanceN)
RomaniaMapFile = dict()
fileName = "Graph.txt"
f1 = open(fileName, "r")
lines = f1.readlines()
for line in lines:
  if(len(line.split("->")) != 2):
    continue
  parts = line.split("->")
  key = parts[0]
  neighbours = parts[1].split(",")
  value = []
  for neighbour in neighbours:
    #triple = (neighbour, 1)
    neighbouringVertex = neighbour.replace("(","").split("#")[0]
    distance = int(neighbour.replace(")","").split("#")[1])
    pair = (neighbouringVertex, distance)
    value.append(pair)
  RomaniaMapFile[key] = value
print(RomaniaMapFile)

bfs(RomaniaMapFile,'A','B')

dfs(RomaniaMapFile,'A','B')

#3. Uniform Cost Search
f1 = open("Graph.txt", "r")
lines = f1.readlines()
graph = dict()
for line in lines:
  if(len(line.split("\t")) != 2):
    continue
  parts = line.split("\t")
  key = parts[0]
  neighbours = parts[1].split(" ")
  value = []
  for neighbour in neighbours:
    #triple = (neighbour, 1)
    neighbouringVertex = neighbour.split(",")[0]
    distance = int(neighbour.split(",")[1])
    pair = (neighbouringVertex, distance)
    value.append(pair)
  graph[key] = value
#print(graph)
'''
for key in graph.keys():
  line = key + "->" + str(graph[key])
  print(line)
'''

from queue import PriorityQueue

def ucs(graph, start, goal):
  visited = set()
  frontier = PriorityQueue()
  frontier.put((0, start))
  parent = {}

  cost = {start:0}

  while not frontier.empty():
    current_cost, current_node = frontier.get()
    if current_node == goal:
      break
    visited.add(current_node)

    for nextNode, distance in graph[current_node]:
      newDistance = cost[current_node] + distance

      if nextNode not in cost or newDistance < cost[nextNode]:
        cost[nextNode] = newDistance
        priority = newDistance
        frontier.put((priority, nextNode))
        parent[nextNode] = current_node

  path = []
  #totalCost = 0
  if goal in parent:
    current = goal
    while current != start:
      path.append(current)
      #totalCost += graph[parent[current]][current]
      current = parent[current]
    path.append(start)
    path.reverse()
  return path #,totalCost

print(ucs(graph, 'A', 'B'))