
maze = {
    "0,0": [("0,1", 1)],
    "0,1": [("0,2", 1)],
    "0,2": [("0,3", 1)],
    "0,3": [("0,4", 1), ("1,3", 1)],
    "0,4": [ ],
    "1,3": [("1,2", 1), ("2,3", 1), ("1,4", 1)],
    "1,2": [("1,1", 1)],
    "1,1": [("1,0", 1)],
    "1,0": [("2,0", 1)],
    "2,0": [("3,0", 1)],
    "3,0": [("3,1", 1)],
    "3,1": [("2,1", 1), ("3,2", 1)],
    "2,1": [ ],
    "3,2": [("2,2", 1), ("4,2", 1)],
    "2,2": [ ],
    "4,2": [("4,1", 1), ("4,3", 1)],
    "4,1": [("4,0", 1)],
    "4,0": [ ],
    "4,3": [("4,4", 1), ("3,3", 1)],
    "3,3": [ ],
    "4,4": [("3,4", 1)],
    "3,4": [("2,4", 1)],
    "2,4": [("1,4", 1)],
    "1,4": [("1,3", 1)],
    "2,3": [ ]
}



def bfs2(G, start, target):
    # helper data structures
    visited = set()
    Q = []
    Q.append( (None,start,0) )
    trace = {}

    # loop untill Q is not empty
    while (Q != []):
        # pick the first node in queue
        # and keep trak of parent node
        (p,u,c) = Q.pop(0)
        trace[u] = (p,c)
 
        # keep track of visited nodes
        visited.add(u)
        print("visited: ",u)

        # check if the goal is reached
        if u == target:
           print("reached target: ", target) 
           #print(trace) 
           break
        
        for (v,c) in G[u]:
          if (v not in visited) and ( (u,v,c) not in Q ): 
            Q.append( (u,v,c) )
            print("added neighbour: ", v)
        #print("Q: ", Q)
    return trace

# run BFS
start = "0,0"
target = "2,1"
tr = bfs2(maze, start, target)
print(tr)

# recover path by backtracing
path = []
cost = 0
if target in tr:
    (p,c) = tr[target]
    path = [target]
    cost += c
    while p != None:
        path.append(p)
        (p,c) = tr[p]
        cost += c
        
print("---------------------")
print("Path:", path[::-1])
print("Cost: ", cost)