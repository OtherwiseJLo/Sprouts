import networkx as nx
import ipycytoscape


class Sprouts:
    def __init__(self, n=2):
        self.board = nx.Graph()
        self.board.add_nodes_from(range(n))
    
    def make_move(self, src, dest):
        pass


if __name__ == "__main__":
    print("Testing script")
    board = Sprouts()
