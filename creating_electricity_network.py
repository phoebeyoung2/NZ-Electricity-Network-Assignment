from module_lab2_task2 import *

# Creating electricity_network.png
electric_network = NetworkElectricNZ()
electric_network.read_network('nz_network')
electric_network.plot_network('electricity_network.png')

# Code to help me answer questions for network_answers
number_nodes = len(electric_network.nodes)
print("Nodes:", number_nodes)
number_arcs = len(electric_network.arcs)
print("Arcs:", number_arcs)
# Print all the arcs from the source node to destination node, to find the largest and it's connecting nodes
print(electric_network.arcs)

