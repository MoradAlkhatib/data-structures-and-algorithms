from collections import defaultdict
 
class Graph:
    def __init__(self):
      
        self.graph = defaultdict(list)
 
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    
 
  
    def BFS(self, s):
        """Function to print a BFS of graph

        """
        arr = []
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            arr.append(s)
 

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return arr


 