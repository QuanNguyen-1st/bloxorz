from atr.bfs_node import BFS_Node
from atr.player import Player
from atr.map import Map

class BFS:
    def __init__(self, map: Map) -> list:
        self.map = map
    
    def makeChildren(self, node: BFS_Node, visited: list, arr: list) -> list:
        children = []
        for (playerMove, move, newMap) in self.map.legalMoves(node.player, arr):
            if self.hasVisited(playerMove, visited, newMap):
                continue
            children.append(BFS_Node(newMap, playerMove, move, node))
        return children

    def hasVisited(self, player: Player, visited: list, arr: list) -> bool:
        for node in visited:
            if player == node.player and arr == node.arr:
                return True
        return False

    def BFS_solve(self) -> str:
        visited = []
        node_queue = []
        player = BFS_Node(self.map.arr, Player(self.map.start, self.map.start), None, None)
        visited.append(player)
        node_queue.append(player)
        while len(node_queue) > 0:
            node = node_queue.pop(0)
            if self.map.hasWon(node.player):
                return node.makePathTo()
            children = self.makeChildren(node, visited, node.arr)
            for child in children:
                node_queue.append(child)
                visited.append(child)


        