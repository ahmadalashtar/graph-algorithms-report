class Graph:
    def __init__(self, num, fileName):
        self.vertices = num
        self.adjList = {}
        self.fileName = fileName
        self.edges = []

    def addEdge(self, s, d):
        self.edges.append((s,d))
        try:
            self.adjList[s].append(d)
        except:
            self.adjList[s] = []
            self.adjList[s].append(d)
        try:
            self.adjList[d].append(s)
        except:
            self.adjList[d] = []
            self.adjList[d].append(s)

    def write2File(self):
        file = open( self.fileName, 'w' )
        file.write( repr(self.adjList))
        file.close()