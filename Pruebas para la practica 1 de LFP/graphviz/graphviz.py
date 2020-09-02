import pydot
import os
os.system("cls")
dot_txt = 'digraph G {\n    start -> end;\n}'
graph, = pydot.graph_from_dot_data(dot_txt)
graph.write_png('f.png')