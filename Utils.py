from Graph import Graph

def file2Graph(filesPath, fileName):
    filePath = filesPath + fileName
    linesToIgnore = 2
    vertices = 0

    with open(filePath, 'r') as f:
        lines = 0
        for line in f:
            lines = lines + 1
            if lines == linesToIgnore:
                vertices = int(line.split()[1])
                graph = Graph(vertices, fileName)
            elif lines > linesToIgnore:
                vertex1 = int(line.split()[0])
                vertex2 = int(line.split()[1])
                graph.addEdge(vertex1,vertex2)
    return graph