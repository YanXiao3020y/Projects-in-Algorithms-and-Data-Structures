# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from __future__ import annotations

import math
from typing import TypeVar
from dataclasses import dataclass
import random
import copy

from CFloat import CFloat

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


@dataclass
class Rank:
    geometric_rank: int
    uniform_rank: int

    def __lt__(self, other: Rank) -> bool:
        if other is None:  # in case of misuse
            return False

        # implement by the picture https://edstem.org/us/courses/38696/discussion/3076164
        # primarily on r1, but breaking ties by r2
        if self.geometric_rank == other.geometric_rank:
            return self.uniform_rank < other.uniform_rank
        return self.geometric_rank < other.geometric_rank

    # overwrite the original compare function in insert() "rank == cur.rank"
    def __eq__(self, other: Rank) -> bool:
        if other is None:  # in case of misuse
            return False

        # implement by the picture https://edstem.org/us/courses/38696/discussion/3076164
        # primarily on r1, but breaking ties by r2
        return self.geometric_rank == other.geometric_rank and self.uniform_rank == other.uniform_rank

    def __gt__(self, other: Rank) -> bool:
        if other is None:  # in case of misuse
            return False

        # implement by the picture https://edstem.org/us/courses/38696/discussion/3076164
        # primarily on r1, but breaking ties by r2
        if self.geometric_rank == other.geometric_rank:
            return self.uniform_rank > other.uniform_rank
        return self.geometric_rank > other.geometric_rank

    def __ge__(self, other: Rank) -> bool:
        return self.__gt__(other) or self.__eq__(other)


class Node:
    # key: KeyType
    # val: ValType  # capacity: float
    # rank: Rank
    # best_remaining_capacity: float
    # left: Node = None
    # right: Node = None

    def __init__(self, key: KeyType, val: ValType, rank: Rank = None):
        self.key = key
        self.val = val  # treat as capacity: float
        self.rank = rank
        self.best_remaining_capacity = CFloat(1.0)
        self.left = None
        self.right = None

    # def __deepcopy__(self, memo):
    #     new_instance = self.__class__(self.key, copy.deepcopy(self.val, memo), copy.deepcopy(self.rank, memo))
    #     new_instance.left = copy.deepcopy(self.left, memo)
    #     new_instance.right = copy.deepcopy(self.right, memo)
    #     return new_instance

class ZipZipTree:
    root: Node = None

    def __init__(self, capacity: int = None):
        self.capacity = capacity
        self.size = 0

    def get_random_rank(self) -> Rank:
        # geometric_rank
        i = 0
        while True:
            # if random.randint(0, 1) == 1: # randint: Discrete uniform distribution, yielding integers.
            if random.choice([0, 1]) == 1:  # each number 0 & 1 with 50% chance. When equal 1, then done
                break
            i += 1
        geometric_rank = i

        # uniform
        uniform_max = int(math.log(self.capacity) ** 3 - 1)  # log(capacity)^3 - 1
        uniform_rank = random.randint(0, uniform_max)  # choose from 0 to log(capacity)^3 - 1

        return Rank(geometric_rank, uniform_rank)

    def update_node(self, node: Node):
        pass

    def insert(self, key: KeyType, val: ValType, rank: Rank = None):
        self.size += 1

        # from discussion, the different about ZipTree and ZipZipTree is about the ranking,
        # but the implementations are the same, so just use recursive one instead, less easy making typing typo.
        # pseudocode from page 13 https://www.ics.uci.edu/~goodrich/teach/cs165/notes/ZipTrees.pdf
        # ======================================================
        if rank is None:
            rank = ZipZipTree.get_random_rank(self)
        x_new_node = Node(key, val, rank)  # building x
        self.root = self.insert_helper(self.root, x_new_node)

    def insert_helper(self, root_node: Node, x_new_node: Node):  # ??? when revert the position of parameter, error pops
        if root_node is None:
            return x_new_node
        if x_new_node.key < root_node.key:
            if self.insert_helper(root_node.left, x_new_node) == x_new_node:
                if x_new_node.rank < root_node.rank:
                    root_node.left = x_new_node
                else:
                    root_node.left = x_new_node.right
                    x_new_node.right = root_node
                    return x_new_node
        else:
            if self.insert_helper(root_node.right, x_new_node) == x_new_node:
                if x_new_node.rank <= root_node.rank:
                    root_node.right = x_new_node
                else:
                    root_node.right = x_new_node.left
                    x_new_node.left = root_node
                    return x_new_node
        return root_node

    def zip(self, x_node: Node, y_node: Node):
        if x_node == None:
            return y_node
        if y_node == None:
            return x_node
        if x_node.rank < y_node.rank:
            y_node.left = self.zip(x_node, y_node.left)
            return y_node
        else:
            x_node.right = self.zip(x_node.right, y_node)
            return x_node

    def remove(self, key: KeyType):
        # pseudocode from page 13 https://www.ics.uci.edu/~goodrich/teach/cs165/notes/ZipTrees.pdf
        # ======================================================
        self.root = self.remove_helper(self.root, key)

    def remove_helper(self, root_node: Node, x_key: KeyType):  # ??? same issue as helper function insert. when revert the position of parameter, error pops
        if x_key == root_node.key:
            return self.zip(root_node.left, root_node.right)
        if x_key < root_node.key:
            if x_key == root_node.left.key:
                root_node.left = self.zip(root_node.left.left, root_node.left.right)
            else:
                self.remove_helper(root_node.left, x_key)
        else:
            if x_key == root_node.right.key:
                root_node.right = self.zip(root_node.right.left, root_node.right.right)
            else:
                self.remove_helper(root_node.right, x_key)
        return root_node


    # def insert(self, key: KeyType, val: ValType, rank: Rank = None):
    #     self.size += 1
    #
    #     # pseudocode from page 16 https://www.ics.uci.edu/~goodrich/teach/cs165/notes/ZipZipTrees.pdf
    #     # ======================================================
    #     if rank is None:
    #         rank = self.get_random_rank()
    #     x_new_node = Node(key, val, rank)  # building x
    #     cur = self.root
    #     while cur is not None \
    #             and (rank < cur.rank
    #                  or (rank == cur.rank
    #                      and key > cur.key)):
    #         prev = cur  # need deep copy???
    #         # prev = copy.deepcopy(cur)
    #         if key < cur.key:
    #             cur = cur.left
    #         else:
    #             cur = cur.right
    #
    #     if cur == self.root:
    #         self.root = x_new_node
    #     elif key < prev.key:
    #         prev.left = x_new_node
    #     else:
    #         prev.right = x_new_node
    #
    #     if cur is None:
    #         x_new_node.left = x_new_node.right = None
    #         return
    #     if key < cur.key:
    #         x_new_node.right = cur
    #     else:
    #         x_new_node.left = cur
    #
    #     prev = x_new_node
    #     while cur is not None:
    #         fix = prev
    #         if cur.key < key:
    #             while True:
    #                 prev = cur
    #                 cur = cur.right
    #                 if cur is None or cur.key > key:
    #                     break
    #         else:
    #             while True:
    #                 prev = cur
    #                 cur = cur.left
    #                 if cur is None or cur.key < key:
    #                     break
    #         if fix.key > key \
    #                 or (fix == x_new_node
    #                     and prev.key > key):
    #             fix.left = cur
    #         else:
    #             fix.right = cur
    #     # ======================================================
    #     self.update_node(self.root)  # ??? self.root



    # def remove(self, key: KeyType):
    #     self.size -= 1
    #
    #     # pseudocode from page 16 https://www.ics.uci.edu/~goodrich/teach/cs165/notes/ZipZipTrees.pdf
    #     # ======================================================
    #     x_delete_node = Node(key)  # building x
    #     cur = self.root
    #     while key != cur.key:
    #         prev = cur
    #         if key < cur.key:
    #             cur = cur.left
    #         else:
    #             cur = cur.right
    #     left = cur.left
    #     right = cur.right
    #
    #     if left is None:
    #         cur = right
    #     elif right is None:
    #         cur = left
    #     elif left.rank >= right.rank:
    #         cur = left
    #     else:
    #         cur = right
    #
    #     if self.root == x_delete_node:
    #         self.root = cur
    #     elif key < prev.key:
    #         prev.left = cur
    #     else:
    #         prev.right = cur
    #
    #     while left is not None and right is not None:
    #         if left.rank >= right.rank:
    #             while True:
    #                 prev = left
    #                 left = left.right
    #                 if left is None or left.rank < right.rank:
    #                     break
    #             prev.right = right
    #         else:
    #             while True:
    #                 prev = right
    #                 right = right.left
    #                 if right is None or left.rank >= right.rank:
    #                     break
    #             prev.left = left
    #     # ======================================================
    #     self.update_node(self.root)  # ???


    def find(self, key: KeyType) -> ValType:
        cur = self.root
        while True:
            if cur is None:  # if key does not exist, then return none as signal
                return None
            if cur.key == key:
                return cur.val
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

    def get_size(self) -> int:
        return self.size;

    def get_height_helper(self, node: Node):
        # the case of 0 or 1 node in the tree
        if node is None \
                or (node.left is None
                    and node.right is None):
            return 0

        # more than 1 node in the tree
        height_left_tree = self.get_height_helper(node.left)
        height_right_tree = self.get_height_helper(node.right)
        return 1 + max(height_left_tree, height_right_tree)

    def get_height(self) -> int:
        return self.get_height_helper(self.root)

    def get_depth(self, key: KeyType):
        # same implementation of find, but add a counter for return
        counter = 0

        cur = self.root
        while True:
            if cur.key == key:
                break
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
            counter += 1

        return counter

# feel free to define new methods in addition to the above
# fill in the definitions of each required member function (above),
# and for any additional member functions you define
