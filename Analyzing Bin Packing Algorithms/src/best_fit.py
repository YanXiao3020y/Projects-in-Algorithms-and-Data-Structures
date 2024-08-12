from zipzip_tree import ZipZipTree, KeyType, ValType, Node
from CFloat import CFloat


class BFZipZipTree(ZipZipTree):
    root: Node = None

    def insert(self, key: KeyType, val: ValType, rank: int = -1):
        self.size += 1
        if rank == -1:
            rank = self.get_random_rank()
        x_new_node = Node(key, val, rank)
        self.root = self.insert_helper(self.root, x_new_node)
        self.update_node(self.root)

    def remove(self, key: KeyType):
        self.root = self.remove_helper(self.root, key)
        self.update_node(self.root)

    # def update_node(self, node: FFNode):
    #     node.val.best_remaining_capacity = max(
    #         node.left.val2.best_remaining_capacity,
    #         node.right.val2.best_remaining_capacity,
    #         node.val2.capacity
    #     )
    #     self.update_nodes_best_remaining_capcity(self.root)  # self.root ???

    # break down the update node to two parts. First is find the suitable position,
    # then update the current node with its best remaining capacity
    def update_node(self, node: Node):
        # using post order traversal to find the suitable position
        if node is None:
            return
        if node.left is not None:
            self.update_node(node.left)
        if node.right is not None:
            self.update_node(node.right)

        node.best_remaining_capacity = self.get_best_remaining_capacity(node)

    def get_best_remaining_capacity(self, cur: Node) -> KeyType:
        if cur.right is None:
            return cur.key
        return self.get_best_remaining_capacity(cur.right)

    def find_BF(self, key: KeyType) -> KeyType:
        if self.root is None:  # the case for empty tree
            return None

        return_key = None
        node = self.root
        while True:
            if key > node.best_remaining_capacity:
                return return_key

            if key <= node.key:
                return_key = node.key
                if node.left is None:
                    return return_key
                else:
                    node = node.left

            if key > node.key:
                if node.right is None:
                    return return_key
                else:
                    node = node.right


def best_fit(items: [float], assignment: [int], free_space: [float]):
    bin_index = 0
    capacity = 10e6
    tree = BFZipZipTree(capacity)  # initialize the best-fitZipZip tree
    tree.insert(CFloat(1.0), bin_index)  # add root
    free_space.append(1.0)  # initialize the first bin

    for i in range(len(items)):
        position = tree.find_BF(CFloat(items[i]))  # find the suitable position if exist.
        # position represents remaining capacity in this case
        if position is None:  # not find any suitable capacity in the tree, insert a new node
            bin_index += 1
            tree.insert(CFloat(1.0 - items[i]), bin_index)  # insert that node in the suitable position
            assignment[i] = bin_index
            free_space.append(1.0 - items[i])
        else:  # find suitable capacity, modify current node
            bin_index2 = tree.find(position)  # return the val of the suitable node.
            # In this case, val is bin index
            tree.remove(position)  # delete that node
            new_remaining_capacity = position - CFloat(items[i])  # calculate new capacity
            tree.insert(new_remaining_capacity, bin_index2)  # insert the new node with updated capacity
            assignment[i] = bin_index2
            free_space[bin_index2] = position.val - items[i]  # update waste


def best_fit_decreasing(items: [float], assignment: [int], free_space: [float]):
    best_fit(sorted(items, reverse=True), assignment, free_space)
