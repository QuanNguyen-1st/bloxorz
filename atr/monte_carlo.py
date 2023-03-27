from atr.node import MC_Node
from atr.player import Player
from atr.map import Map
import math
import random
import copy
import numpy as np

class MCTS:
    winPath = ""
    VNode_count = 1
    can_find_win_path = True
    def __init__(self, map: Map):
        self.map = map

    def reward(self):
        return (self.map.width*self.map.height)**2

    def isWinState(self, player: Player):
        return player.isStanding() and player.p1 == self.map.goal

    def isLoseState(self, player: Player, arr: list):
        return not self.map.canHold(player, arr)

    def isTerminalState(self, player: Player, arr: list):
        return self.isWinState(player) or self.isLoseState(player, arr)

    def expand(self, node: MC_Node, expanded: list):
        child_node = self.best_child(node)
        child_node.children = self.makeMoves(child_node.player, child_node.arr, expanded)
        expanded.append((child_node.player, child_node.arr))
        return child_node
    
    def makeMoves(self, player: Player, arr: list, expanded: list):
        moves = self.map.legalMoves(player, arr)
        return [(playerMove, move, newMap) for (playerMove, move, newMap) in moves if (playerMove, newMap) not in expanded]

    def rollout(self, node: MC_Node, expanded: list):
        expanded_and_rollout = copy.deepcopy(expanded)
        Player = node.player
        Map = node.arr
        count = 0
        while not self.isTerminalState(Player, Map) and count <= 100:
            # possible_moves = self.map.allMoves(Player, Map)
            possible_moves = self.makeMoves(Player, Map, expanded_and_rollout)
            count += 1
            if (len(possible_moves)) == 0:
                return -1
            (playerMove, move, newMap) = random.choice(possible_moves)
            expanded_and_rollout.append((playerMove, newMap))
            Player = playerMove
            Map = newMap
        return self.reward() if self.isWinState(Player) else -1

    def back_propagate(self, node: MC_Node, result):
        node.N += 1.
        node.Q += result
        if node.parent:
            self.back_propagate(node.parent, result)

    def best_child(self, node: MC_Node):
        max_value = node.children[0].value()
        for child in node.children:
            max_value = max(child.value(), max_value)
        max_nodes = [n for n in node.children if n.value() == max_value]
        best_child = random.choice(max_nodes)
        return best_child

    def _tree_policy(self, node: MC_Node, expanded: list):
        current_node = node
        while not self.isTerminalState(node.player, node.arr) and len(current_node.children) != 0:
            current_node = self.best_child(current_node)
        return current_node.expand()

    def best_action(self, node: MC_Node, expanded: list, simulation_no):

        for i in range(simulation_no):
            v = self._tree_policy(node, expanded)
            reward = self.rollout(v, expanded)
            self.back_propagate(v, reward)

        current_node = node
        while not self.isTerminalState(node.player, node.arr) and len(current_node.children) != 0:
            current_node = self.best_child(current_node)
        return current_node

    def solve(self, simulation_no = 4000):
        expanded = []
        start_node = MC_Node(self.map.arr, Player(self.map.start, self.map.start), None, None)
        possible_moves = self.map.allMoves(start_node.player, start_node.arr)
        start_node.children = [MC_Node(newMap, playerMove, move, start_node) for (playerMove, move, newMap) in possible_moves]
        expanded.append((start_node.player, start_node.arr))
        selected_node = self.best_action(start_node, expanded, simulation_no)
        self.VNode_count = len(expanded)
        if not self.map.hasWon(selected_node.player):
            self.can_find_win_path = False
            # print("Haven't found win path, best path so far is: ")
        self.winPath = selected_node.makePathTo()



