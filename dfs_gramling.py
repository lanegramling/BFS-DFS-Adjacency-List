import sys # For sys args
import re  # for regex parsing of file input

# @ Name : Lane Gramling
# @ Due Date : March 22, 2019
# @ Brief: Depth-first graph search implementation using
#           adjacency list structure from a file as input.
#  		Usage: dfs_gramling.py <input-file>


edges = []      # Contains all edges, size |E|
graph = {}      # Contains the graph, constructed from edges
discovered = [] # Stores discovered states
s = None        # Head value

# Search algorithm
def search(s):
    stack = [s]
    while stack:
        node = stack.pop()
        if not discovered[node]:
            print(node, end=' ')
            discovered[node] = True
            for v in reversed(graph[node]):
                stack.append(v)

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
