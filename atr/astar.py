from atr.node import A_star_Node
from atr.player import *
from atr.map import Map

class AStar:
    winPath = []
    VNode_count = 1
    def __init__(self, map: Map):
        self.map = map

    def chebDistance(self, player: Player):
        h1 = max(abs(player.p1.x - self.map.goal.x), abs(player.p1.y - self.map.goal.y))
        h2 = max(abs(player.p2.x - self.map.goal.x), abs(player.p2.y - self.map.goal.y))
        return max(h1, h2)
    
    def makeChildren(self, node: A_star_Node, arr: list) -> list:
        children = []
        # if isinstance(node.player, DetachedPlayer):
        #     self.VNode_count += 8
        # else:
        #     self.VNode_count += 4
        for (playerMove, move, newMap) in self.map.legalMoves(node.player, arr):
            h_child = self.chebDistance(playerMove)
            children.append(A_star_Node(newMap, playerMove, move, node, node.g + 1, h_child))
        # self.VNode_count += len(children)
        return children
    
    def inClosed_list(self, newNode: A_star_Node, closed_list: list):
        for node in closed_list:
            if newNode == node and newNode.g >= node.g:
                return True
        return False
    
    def inOpen_list(self, newNode: A_star_Node, open_list: list):
        for node in open_list:
            if newNode == node and newNode.g >= node.g:
                return True
        return False
        
    def solve(self):
        open_list = []
        closed_list = []
        player_start = Player(self.map.start, self.map.start)
        playerDisToWin = None
        playerDisToWin = self.chebDistance(player_start)
        start_node = A_star_Node(self.map.arr, player_start, None, None, 0, playerDisToWin)

        open_list.append(start_node)

        while open_list:
            open_list.sort()
            node = open_list.pop(0)
            closed_list.append(node)

            if self.map.hasWon(node.player):
                self.winPath = node.makePathTo()
                return
            
            children = self.makeChildren(node, node.arr)
            for child in children:
                if self.inClosed_list(child, closed_list):
                    del child
                    continue
                if self.inOpen_list(child, open_list):
                    del child
                    continue
                open_list.append(child)
                self.VNode_count += 1