from VertexCover import VertexCover
from Utils import file2Graph
import os

if __name__ == "__main__":

    currentDirectory = os.getcwd()
    dataFolder = "\\data"
    files = os.listdir(currentDirectory + dataFolder)
    filesPath = currentDirectory + dataFolder + "\\"
    for fileName in files:
        graph = file2Graph(filesPath, fileName)
        vertexCover = VertexCover(graph)
        
