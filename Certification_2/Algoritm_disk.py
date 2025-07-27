my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)], # This is a dictionary that represents a graff, the key is the nodes 
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''): #Definition of fucntion 3 parameters graph, start node start and target node destiny optional if omited it will show all roads at the nodes
    unvisited = list(graph) # list of nodes that have not been visited
    distances = {node: 0 if node == start else float('inf') for node in graph} # dictionary taht stores the shortest distance since start node
    paths = {node: [] for node in graph}  # dictionary that stores the complete full path since start to each node
    paths[start].append(start)
    
    while unvisited: # if repeat while nodes remain unvisited 
        current = min(unvisited, key=distances.get) # select the unvisited node with shotest distance
        for node, distance in graph[current]: # iterates over the neighbors at a distance
            if distance + distances[current] < distances[node]: # veryfies if the target to node is the shortest dintance
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current) # mark the node as  vitsited
    
    targets_to_print = [target] if target else graph # if specified this target print only one, else print all
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}') # print the distance and shortest target since start node
    
    return distances, paths
    
shortest_path(my_graph, 'A','F') # calcule node sice A to F