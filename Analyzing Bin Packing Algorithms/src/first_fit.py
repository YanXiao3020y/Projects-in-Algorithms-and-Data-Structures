from zipzip_tree import ZipZipTree, KeyType, ValType, Node
from CFloat import CFloat

# explanations for member functions are provided in requirements.py


# @dataclass
# class FFValue:  # make it replace ValType
#     capacity: float
#     best_remaining_capacity: float
#
#
# class FFNode:
#     key: KeyType
#     val2: FFValue
#     left: FFNode = None
#     right: FFNode = None


class FFZipZipTree(ZipZipTree):
    root: Node = None

    def insert(self, key: KeyType, val: ValType, rank: int = -1):
        self.size += 1
        if rank == -1:
            rank = ZipZipTree.get_random_rank(self)
        x_new_node = Node(key, val, rank)
        self.root = self.insert_helper(self.root, x_new_node)
        self.update_node(self.root)  # discussion mention to update node each insert

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

    def get_best_remaining_capacity(self, cur: Node) -> ValType:
        if cur.left is None and cur.right is None:
            return cur.val

        if cur.left is None:
            right_best_remaining_capacity = self.get_best_remaining_capacity(cur.right)
            return max(cur.val, right_best_remaining_capacity)
        elif cur.right is None:
            left_best_remaining_capacity = self.get_best_remaining_capacity(cur.left)
            return max(cur.val, left_best_remaining_capacity)
        else:
            left_best_remaining_capacity = self.get_best_remaining_capacity(cur.left)
            right_best_remaining_capacity = self.get_best_remaining_capacity(cur.right)
            return max(cur.val, left_best_remaining_capacity, right_best_remaining_capacity)

    def find_FF(self, val: ValType) -> KeyType:
        if self.root is None:  # the case for empty tree
            return None

        fit_id = None
        node = self.root
        while True:
            if val > node.best_remaining_capacity and val > node.val:
                return fit_id

            if node.left is not None \
                    and val <= node.left.best_remaining_capacity:
                node = node.left
                continue
            elif val <= node.val:
                return node.key
            elif node.right is not None \
                    and val <= node.right.best_remaining_capacity:
                node = node.right
                continue
            return fit_id


def first_fit(items: [float], assignment: [int], free_space: [float]):
    bin_index = 0
    capacity = 10e6
    tree = FFZipZipTree(capacity)  # initialize the first-fit ZipZip tree
    tree.insert(bin_index, CFloat(1.0))   # add root
    free_space.append(1.0)  # initialize the first bin

    for i in range(len(items)):
        position = tree.find_FF(CFloat(items[i]))  # find the suitable position if exist.
        # position represents bin_index in this case
        if position is None:  # not find any suitable capacity in the tree, insert a new node
            bin_index += 1
            tree.insert(bin_index, CFloat(1.0 - items[i]))  # insert that node in the suitable position
            assignment[i] = bin_index
            free_space.append(1.0 - items[i])
        else:  # find suitable capacity, modify current node
            fit_cap = tree.find(position)  # return the val of the suitable node.
            # In this case, val is remaining capacity
            tree.remove(position)  # delete that node
            new_remaining_capacity = fit_cap - CFloat(items[i])  # calculate new capacity
            tree.insert(position, new_remaining_capacity)  # insert the new node with its suitable position
            # and updated capacity
            assignment[i] = position
            free_space[position] = fit_cap.val - items[i]  # update waste


def first_fit_decreasing(items: [float], assignment: [int], free_space: [float]):
    first_fit(sorted(items, reverse=True), assignment, free_space)
