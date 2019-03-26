import sys # For sys args
import re  # for regex parsing of file input

# @ Name : Lane Gramling
# @ Due Date : March 22, 2019
# @ Brief: Breadth-first graph search implementation using
#           adjacency list structure from a file as input.
#  		Usage: bfs_gramling.py <input-file>


edges = []      # Contains all edges, size |E|
graph = {}      # Contains the graph, constructed from edges
discovered = [] # Stores discovered states
s = None        # Head value

# Search algorithm
def search(s):
    discovered[s] = True
    current_tree = {}
    L = {}
    L[0] = [s]
    i = 0
    while len(L[i]):                            # Main search loop
        L[i + 1] = []                           # Initialize next layer
        for u in L[i]:                          # Begin traversing layer
            current_tree[u] = []                # Initialize tree for current edge u
            for v in graph[u]:
                if not discovered[v]:           # Append undiscovered nodes
                    discovered[v] = True
                    current_tree[u].append(v)
                    L[i + 1].append(v)
        i += 1                                  # Increment layer
    for u in L:                        # Print search results
        for v in L[u]:
            print(v, end=" ")

# Generate graph structure from adjacency list
def generateTree(filename):
    global s, discovered
    for line in open(filename, 'r').read().split('\n'):                      # Read in file
        if line:
            edge = tuple(list(map(int, re.sub(r'\s', '', line).split(',')))) # Collect edges
            if len(edge) > 1: edges.append(edge)
            else:                                                            # Create HEAD node
                s = int(line)
                graph[s] = []
    for u in list(set([u for (u, v) in edges])):
        graph[u] = []                                                        # Create all nodes 1..n
    for (u, v) in edges: graph[u].append(v)                                  # Add all edges to all nodes
    discovered = [False] * len(graph)                                        # Initialize discovered states

# Execution on runtime
if len(sys.argv) == 1:
    print("No arguments provided. Please provide a filename.")
else:
    generateTree(sys.argv[1])
    search(s)
