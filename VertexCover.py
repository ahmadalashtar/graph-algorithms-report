from itertools import chain
from copy import deepcopy
from pulp import *
import random

class VertexCover:
    def __init__(self,graph):
        self.graph = graph     
        
    def __listRight(self, listL=None):
        if listL is None:
            listL = dict(sorted(self.graph.adjList.items(), reverse=True))

        solution = []
        for vertex in listL:
            for neighbor in self.graph.adjList[vertex]:
                if neighbor > vertex:
                    if neighbor not in solution:
                        if vertex not in solution:
                            solution.append(vertex)
                            break

        return solution  

    def __gatherCPs(self):
        minCP = []
        trivialMinCP = []
        graph = deepcopy(self.graph)
        
        while graph.adjList:
            vertices = list(graph.adjList.keys())
            u = random.choice(vertices)

            if not graph.adjList[u]:
                del graph.adjList[u]
                continue

            v = random.choice(graph.adjList[u])

            trivialMinCP.append([u])
            trivialMinCP.append([v])
            minCP.append([u,v])

            newClique = []

            for vertex in graph.adjList[u]:
                if vertex in graph.adjList[v]:
                    newClique.append(vertex)
                graph.adjList[vertex].remove(u)
            
            for vertex in graph.adjList[v]:
                graph.adjList[vertex].remove(v)

            del graph.adjList[u]
            del graph.adjList[v]

            if len(newClique) > 1:
                minCP.append(newClique)

        return trivialMinCP + minCP
    
    def heurize(self):
        solution = self.__listRight()
        return solution
        
    def approximate(self):
        minCP = self.__gatherCPs()
        listL = list(chain(*minCP))
        solution = self.__listRight(listL)
        return solution
    
    
    def LP(self):
        model = LpProblem(sense=LpMinimize)

        # variables - x[i] binary based on if the i-th vertex is in the set
        variables = [LpVariable(name=f"x_{i}", cat=LpBinary) for i in range(self.graph.vertices)]

        # inequalities
        ## each edge must have at most one vertex from the set
        for u,v in self.graph.edges:
            model += variables[u - 1] + variables[v - 1] >= 1                

        # minimize the number of selected edges
        model += lpSum(variables)

        status = model.solve(PULP_CBC_CMD(msg=False))

        solution = sum(int(variables[i].value()) for i in range(len(variables)))
        return solution
