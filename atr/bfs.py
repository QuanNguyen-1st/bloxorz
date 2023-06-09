from atr.node import BFS_Node
from atr.player import *
from atr.map import Map

class BFS:
    winPath = ""
    VNode_count = 1
    def __init__(self, map: Map):
        self.map = map
    
    def makeChildren(self, node: BFS_Node, visited: list, arr: list) -> list:
        children = []
        # if isinstance(node.player, DetachedPlayer):
        #     self.VNode_count += 8
        # else:
        #     self.VNode_count += 4
        for (playerMove, move, newMap) in self.map.legalMoves(node.player, arr):
            newNode = BFS_Node(newMap, playerMove, move, node)
            if newNode in visited:
                del newNode
                continue
            children.append(newNode)
        self.VNode_count += len(children)
        return children

    # def hasVisited(self, player: Player, visited: list, arr: list) -> bool:
    #     for node in visited:
    #         if player == node.player and arr == node.arr:
    #             return True
    #     return False

    def solve(self):
        visited = []
        node_queue = []
        start_node = BFS_Node(self.map.arr, Player(self.map.start, self.map.start), None, None)
        visited.append(start_node)
        node_queue.append(start_node)
        while node_queue:
            node = node_queue.pop(0)
            if self.map.hasWon(node.player):
                self.winPath = node.makePathTo()
                return
            children = self.makeChildren(node, visited, node.arr)
            for child in children:
                node_queue.append(child)
                visited.append(child)


        