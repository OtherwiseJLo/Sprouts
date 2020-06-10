import networkx as nx
import ipycytoscape


class Sprouts:
    def __init__(self, n=2):
        self.board = nx.MultiGraph()
        self.board.add_nodes_from(range(n))
    
    def make_move(self, src, dest):
        new_node = self.board.number_of_nodes()
        self.board.add_node(new_node)
        self.board.add_edge(src, new_node)
        self.board.add_edge(new_node, dest)


if __name__ == "__main__":
    print("Testing script")
    board = Sprouts()
    board.make_move(0, 0)

    board2 = Sprouts()
    board2.make_move(0, 1)
