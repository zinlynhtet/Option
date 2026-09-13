# from collections import deque

# my_deque =  deque(["Roger Federer", "Rafael Nadal", "Novak Djokovic"])
# my_deque.append("Andy Murray")
# my_deque.append("Pete Sampras")
# my_deque.popleft()
# print(my_deque)
# my_graph = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': [
#     'A', 'B', 'D', 'E'], 'D': ['B', 'C', 'E'], 'E': ['D', 'C']}
# def define_edges(my_graph):
#     edges = []
#     for node in my_graph:
#         for adj_nodes in my_graph[node]:
#             edges.append((node, adj_nodes))
#     return edges
# print(define_edges(my_graph))
class Tree:
    def __init__(self,info , left = None, right = None):
        self.info = info
        self.left = left
        self.right = right
    def __str__(self):
        return f"{str(self.info)} + 'Left node: {str(self.left)}, Right node: {str(self.right)}'"
    
tree = Tree("Root Node", Tree("Branch 1", "Leave 1", "Leave 2"), Tree("Branch 2", "Leave 3", "Leave 4"))
print(tree)