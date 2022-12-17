#username - complete info
#id1      - complete info 
#name1    - Noa Heller
#id2      - 322291758
#name2    - Elad Raveh

import random

"""
A class representing a node in an AVL tree
"""
class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	@type virtual: boolean
	@param virtual: indicates if the node is a virtual node
	"""
	def __init__(self, value, virtual=False):
		self.value = value
		if not virtual:
			self.left = AVLNode(None, True)
			self.left.setParent(self)
			self.right = AVLNode(None, True)
			self.right.setParent(self)
			self.height = 0
			self.size = 1
		else:
			self.left = None
			self.right = None
			self.height = -1
			self.size = 0
		self.parent = None
		self.BF = 0  # Balance factor

	"""Returns the left child.
	
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left

	"""Returns the right child.

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""Returns the parent.

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""Return the value.

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""Returns the height.

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""Returns the balance factor.

	@rtype: int
	@returns: the BF of self, -1 if the node is virtual
	"""
	def getBF(self):
		return self.BF
	
	"""Returns the size of the sub-tree (including the current node).

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def getSize(self):
		return self.size

	"""Sets left child.
	
	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		return

	"""Sets right child.

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		return None

	"""Sets parent.

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node
		return None

	"""Sets right child and sets the child's parent to be self.

	@type node: AVLNode
	@param node: a node
	"""
	def setRightAndParent(self, node):
		self.right = node
		node.setParent(self)
		return None

	"""Sets left child and sets the child's parent to be self.

	@type node: AVLNode
	@param node: a node
	"""
	def setLeftAndParent(self, node):
		self.left = node
		node.setParent(self)
		return None

	"""Sets parent and sets the parent's appropriate child to be self.
	
	@type node: AVLNode
	@param node: a node
	@type is_left: bool
	@param is_left: is self the left son of node    
	"""
	def setParentAndChild(self, node, is_left):
		self.parent = node
		if is_left:
			node.setLeft(self)
		else:
			node.setRight(self)
		return None

	"""Sets value.

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value
		return None

	"""Sets the height of the node.

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h
		return None

	"""
	Sets the height according to the node's children.
	"""
	def setToCurHeight(self):
		self.height = max(self.left.height, self.right.height) + 1
		return None

	"""Sets the balance factor of the node.

	@type bf: int
	@param bf: the balance factor
	"""
	def setBF(self):
		self.BF = self.left.height - self.right.height
		return None

	"""
	Sets the size of the node.
	"""
	def setSize(self):
		self.size = self.left.size + self.right.size + 1
		return None

	"""
	Increases the size of the node.
	"""
	def incSize(self):
		self.size += 1
		return None

	"""
	Decreases the size of the node.
	"""
	def decSize(self):
		self.size -= 1
		return None

	"""Returns whether self is not a virtual node.

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.size != 0:
			return True
		else:
			return False

	"""Turns a virtual node into a real leaf node.
	
	@pre: node is a virtual node
	@val type: string
	"""
	def realFromVirtual(self, val):
		self.setValue(val)
		self.left = AVLNode(None, True)
		self.right = AVLNode(None, True)
		self.left.setParent(self)
		self.right.setParent(self)
		self.height = 0
		self.size = 1
		self.BF = 0
		return None


"""
A class implementing the ADT list, using an AVL tree.
"""
class AVLTreeList(object):
	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = None
		self.first = None
		self.last = None

	"""Returns whether the list is empty.

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.root is None

	"""Retrieves the value of the i'th item in the list.

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str/node.
	@returns: the the value of the i'th item in the list/ the node that contains the i'th item.
	"""
	def retrieve(self, i):
		return AVLTreeList.recRetrieve(self.root, i).getValue()

	@staticmethod
	def recRetrieve(node, k):
		rank = node.left.size + 1
		if rank == k:
			return node
		elif k < rank:
			return AVLTreeList.recRetrieve(node.getLeft(), k)
		else:
			return AVLTreeList.recRetrieve(node.getRight(), k - rank)

	"""Inserts val at position i in the list.

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		if self.root is None:
			self.root = AVLNode(val)
			self.first = self.root
			self.last = self.root
			return 0
		node = self.root
		rank = node.getLeft().getSize() + 1
		while node.isRealNode():
			node, rank = self.__advance(node, i, rank)
		node.realFromVirtual(val)
		if i == 0:
			self.first = node
		elif i == self.root.getSize() - 1:
			self.last = node
		return self.__rebalance(node)

	"""Deletes the i'th item in the list.

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		node = self.root
		if i == node.getSize() - 1:
			self.last = self.__predecessor(self.last)
		if i == 0:
			self.first = self.__successor(self.first)
		rank = node.getLeft().getSize() + 1
		while rank != i + 1:
			node, rank = self.__advance(node, i, rank, False)
		return self.__rebalance(self.__removeFromTree(node), False)

	"""Removes a node from the tree.

	@type node: AVLNode
	@param node: the node we want to remove from the tree.
	@rtype: AVLNode
	@returns: the parent of the physically deleted node.
	"""
	def __removeFromTree(self, node):
		if node == self.first:
			self.first = self.__successor(node)
		elif node == self.last:
			self.last = self.__predecessor(node)
		real_left = node.getLeft().isRealNode()
		real_right = node.getRight().isRealNode()
		if self.root == node:
			return self.__removeRoot(node, real_left, real_right)
		return self.__removeNonRoot(node, real_left, real_right)

	"""Removes the root of the tree.

	@type node: AVLNode
	@param node: the node we want to remove from the tree.
	@type real_left = boolean
	@param real_left: does node have a left son
	@type real_right = boolean
	@param real_right: does node have a right son
	@rtype: AVLNode.
	@returns: the parent of the physically deleted node.
	"""
	def __removeRoot(self, node, real_left, real_right):
		parent = None
		if (not real_left) and (not real_right):
			self.root = self.first = self.last = None
		elif not real_left:
			self.root = node.getRight()
			self.root.setParent(None)
		elif not real_right:
			self.root = node.getLeft()
			self.root.setParent(None)
		else:
			node = self.__deleteSuccessor(node)
			parent = node.getParent()
			node.setParent(None)
			self.root = node
			parent.setSize()
			parent.setToCurHeight()
			node.setToCurHeight()
			node.setSize()
		return parent

	"""Removes a non-root node from the tree.

	@type node: AVLNode
	@param node: the node we want to remove from the tree.
	@type real_left = boolean
	@param real_left: does node have a left son
	@type real_right = boolean
	@param real_right: does node have a right son
	@rtype: AVLNode
	@returns: the parent of the physically deleted node.
	"""
	def __removeNonRoot(self, node, real_left, real_right):
		parent = node.getParent()
		left_son = node.getParent().getLeft() == node
		if (not real_left) and (not real_right):
			AVLNode(None, True).setParentAndChild(parent, left_son)
		elif not real_left:
			node.getRight().setParentAndChild(parent, left_son)
		elif not real_right:
			node.getLeft().setParentAndChild(parent, left_son)
		else:
			node = self.__deleteSuccessor(node)
			copy = parent
			parent = node.getParent()
			node.setParentAndChild(copy, left_son)
			parent.setToCurHeight()
			node.setToCurHeight
			node.setSize()
		parent.setToCurHeight()
		parent.setSize()
		return parent

	"""Deletes the successor to anode in case it has to sons.
	
	@type node: AVLNode
	@param node: 
	"""
	def __deleteSuccessor(self, node):
		next_node = node
		next_node = self.__successor(next_node, True)
		self.__removeFromTree(next_node)
		next_node.setRightAndParent(node.getRight())
		next_node.setLeftAndParent(node.getLeft())
		return next_node

	"""Goes to the next node for the search of the delete and insert functions.
	
	@type node: AVLNode
	@param node: a node
	@type i: int
	@param i: the index if the searched node
	@type delete: boolean
	@param delete: indicates if we are in insertion/deletion
	@rtype: (AVLNode, int)
	@returns: The next node and it's rank
	"""
	@staticmethod
	def __advance(node, i, rank, insert=True):
		if insert:
			node.incSize()
		else:
			node.decSize()
		if rank > i + 1 or (rank == i + 1 and insert):
			node = node.getLeft()
			if node.isRealNode():
				rank -= node.getRight().getSize() + 1
		elif rank < i + 1:
			node = node.getRight()
			if node.isRealNode():
				rank += node.getLeft().getSize() + 1
		return node, rank

	"""Rebalances the tree.

	@type node: AVLNode
	@param node: a node
	@type insert: boolean
	@param insert: indicates if rebalancing after insertion or deletion
	@rtype: int
	@returns: number of rotations made
	"""
	def __rebalance(self, node, insert=True):
		if node == None:
			return 0
		rotations = 0
		node = node.getParent()
		while node is not None:
			height = node.getHeight()
			node.setToCurHeight()
			node.setBF()
			if node.getBF() in [-1, 0, 1]:
				if node.getHeight() == height:
					break
				else:
					node = node.getParent()
			else:
				rotations += self.__rotate(node)
				if insert:
					break
		return rotations

	"""Rotates around a node.

	@type node: AVLNode
	@rtype: int
	@return: number of rotations made (single or double rotation)
	"""
	def __rotate(self, node):
		rotations = 1
		if node.getBF() == 2:
			left = node.getLeft()
			if left.getBF() == -1:
				self.__rotateLeft(left, left.getRight())
				rotations += 1
			self.__rotateRight(node, node.getLeft())
		else:
			right = node.getRight()
			if right.getBF() == 1:
				self.__rotateRight(right, right.getLeft())
				rotations += 1
			self.__rotateLeft(node, node.getRight())
		if self.root == node:
			self.root = node.getParent()
		return rotations

	"""Rotates an edge to the left.
	
	@type node1: AVLNode
	@type node2 = AVLNode
	@pre: node1 is the right son of node2
	"""
	@staticmethod
	def __rotateLeft(node, right):
		parent = node.getParent()
		node.setRightAndParent(right.getLeft())
		right.setLeftAndParent(node)
		right.setParent(parent)
		if parent is not None:
			if node == parent.getLeft():
				parent.setLeft(right)
			else:
				parent.setRight(right)
		if node.isRealNode():
			node.setBF()
			node.setToCurHeight()
			node.setSize()
		if right.isRealNode():
			right.setBF()
			right.setToCurHeight()
			right.setSize()
		return None

	"""Rotates an edge to the right.

	@type node1: AVLNode
	@type node2 = AVLNode
	@pre: node2 is the left son of node1
	"""
	@staticmethod
	def __rotateRight(node, left):
		parent = node.getParent()
		node.setLeftAndParent(left.getRight())
		left.setRightAndParent(node)
		left.setParent(parent)
		if parent is not None:
			if node == parent.getLeft():
				parent.setLeft(left)
			else:
				parent.setRight(left)
		if node.isRealNode():
			node.setBF()
			node.setToCurHeight()
			node.setSize()
		if left.isRealNode():
			left.setBF()
			left.setToCurHeight()
			left.setSize()
		return None

	"""Returns the value of the first item in the list.

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.first

	"""Returns the value of the last item in the list.

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.last

	"""Returns an array representing list (in order).

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		if self.root is None:
			return []
		node = self.first
		array = [node.getValue()]
		for i in range(self.root.getSize() - 1):
			next_node = self.__successor(node)
			if next_node.isRealNode():
				array.append(next_node.getValue())
			node = next_node
		return array

	def listToHeightsAndSizes(self):
		if self.root is None:
			return []
		node = self.first
		array = [[node.getHeight(), node.getSize()]]
		for i in range(self.root.getSize() - 1):
			next_node = self.__successor(node)
			if next_node.isRealNode():
				array.append([next_node.getHeight(), next_node.getSize()])
			node = next_node
		return array

	"""Returns the node that contains the next item in the list.

	@type node: AVLNode
	@param node: a node
	@rtype: node
	@returns: a node that contains the next item in the list
	"""
	@staticmethod
	def __successor(node, delete=False):
		if node.getRight().isRealNode():
			if delete:
				node.decSize()
			node = node.getRight()
			while node.getLeft().isRealNode():
				if delete:
					node.decSize()
				node = node.getLeft()
			return node
		else:
			parent = node.getParent()
			while parent is not None and node == parent.getRight():
				node = parent
				parent = node.getParent()
			return parent

	"""Returns the node that contains the previous item in the list.
	
	@type node: AVLNode
	@param node: a node
	@rtype: node
	@returns: a node that contains the previous item in the list
	"""
	@staticmethod
	def __predecessor(node):
		if node.getLeft().isRealNode():
			node = node.getLeft()
			while node.getRight().isRealNode():
				node = node.getRight()
			return node
		else:
			parent = node.getParent()
			while parent is not None and node == parent.getLeft():
				node = parent
				parent = node.getParent()
			return parent

	"""Sort the info values of the list.

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		return None

	"""Permute the info values of the list.

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		return None

	"""Concatenates lst to self.

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""Searches for a *value* in the list.

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None

	"""Returns the root of the tree representing the list.

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.root.isRealNode():
			return self.root
		return None


def Tester():
	tree = AVLTreeList()
	for i in range(31):
		tree.insert(i, i)
	for i in range(31):
		tree.delete(random.randint(0, 30 - i))
		print(tree.listToArray())
		print(tree.listToHeightsAndSizes())


if __name__ == "__main__":
	Tester()
