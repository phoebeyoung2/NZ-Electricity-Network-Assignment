from module_lab2_task2 import *


def test_add_node():
    """
    Tests whether the add_node function works correctly

    Notes
    -----
    Adds a node to the network and them attempts to access node value to check if it matches the expected output.
    """
    # Initialise an instance of a network
    network = Network()
    # Call the add node function
    network.add_node("A", 965)
    # Call the get_node function to check if it is in the network
    added_node = network.get_node("A")
    assert added_node.name == "A"
    assert added_node.value == 965


def test_add_arc():
    """
    Tests whether the function add_arc works correctly

    Notes
    -----
    Adds nodes (1 and 2) to the network and then uses add_arc to create an arc from 1 -> 2. Then checks
    that the arc is pointing in the correct direction and has the intended weight.
    """
    # Initialise an instance of a network
    network = Network()
    # Add 2 nodes to the network
    network.add_node(1, 765)
    network.add_node(2, 865)
    # Call the add arc function to create an arc from A to B
    node_a = network.get_node(1)
    node_b = network.get_node(2)
    added_arc = network.add_arc(node_a, node_b, 5)
    # Check the arcs in the network
    assert added_arc.weight == 5
    assert added_arc.from_node == node_a
    assert added_arc.to_node == node_b


def test_read_network():
    """
    Tests whether the read_network method in class Network works correctly

    Notes
    -----
    Reads in the 'network.txt' file using the read_network function and check whether the nodes and
    arcs interact as intended.
    """
    # Initialise instance of a network
    network = Network()
    # Apply read network function
    network.read_network('network.txt')
    # Assert the network has created nodes correctly
    assert network.get_node("A").name == "A"
    assert network.get_node("B").name == "B"
    # Assert the network has created arcs correctly
    assert len(network.arcs) == 9


