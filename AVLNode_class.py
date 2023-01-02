#username - complete info
#id1      - 318969268
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

	"""Returns the left son, right son and parent of the node.
	@rtype: tuple of AVLNodes
	@returns: left son, right son, parent
	"""
	def getInfo(self):
		return self.left, self.right, self.parent

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
	Sets the size of the node according to the childrens' size.
	"""
	def setSize(self):
		self.size = self.left.size + self.right.size + 1
		return None

	"""Returns whether self is a virtual node.
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
		self.size = 1
		self.height = 0
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
		self.firstNode = None
		self.lastNode = None

	"""Returns whether the list is empty.
	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.root is None

	"""Returns the size of the list.
	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		if self.root is None:
			return 0
		return self.root.getSize()

	"""Retrieves the value of the i'th item in the list.
	@type i: int
	@param i: index in the list
	@rtype: str/node.
	@returns: the value of the i'th item in the list.
	@complexity: O(log n)
	"""
	def retrieve(self, i):
		if self.empty() or i < 0 or i >= self.length():
			return None
		return AVLTreeList.__recRetrieve(self.root, i).getValue()

	@staticmethod
	def __recRetrieve(node, k):
		rank = node.left.getSize()
		if rank == k:
			return node
		elif k < rank:
			return AVLTreeList.__recRetrieve(node.getLeft(), k)
		else:
			return AVLTreeList.__recRetrieve(node.getRight(), k - rank - 1)

	"""Inserts val at position i in the list.
	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	@complexity: O(log n)
	"""
	def insert(self, i, val):
		if self.root is None:
			self.root = AVLNode(val)
			self.firstNode = self.root
			self.lastNode = self.root
			return 0
		node = self.__treePosition(i)
		node.realFromVirtual(val)
		if i == 0:
			self.firstNode = node
		elif i == self.length():
			self.lastNode = node
		return self.__rebalance(node.getParent())

	"""Func searches for the virtual node which will be in the i'th position if it was real.
	@type i: int
	@param i: the index in which to insert the new node
	@rtype: AVLNode
	@return: The virtual node which will be made into a real node at the i'th location
	@complexity: O(log n)
	"""
	def __treePosition(self, i):
		node = self.root
		while node.isRealNode():
			rank = node.getLeft().getSize()
			if rank >= i:
				node = node.getLeft()
			else:
				node = node.getRight()
				i -= rank + 1
		return node

	"""Deletes the i'th item in the list.
	@type i: int
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	@complexity: O(log n)
	"""
	def delete(self, i):
		if i >= self.length() or i < 0:
			return -1
		if self.length() == 1:
			self.root = self.firstNode = self.lastNode = None
			return 0
		node = self.__recRetrieve(self.root, i)
		if node == self.firstNode:
			self.firstNode = self.__successor(node)
		elif node == self.lastNode:
			self.lastNode = self.__predecessor(node)
		if node == self.root:
			node = self.__removeRoot(node)
		else:
			node = self.__removeNonRoot(node)
		if node is None:
			return 0
		return self.__rebalance(node.getParent(), 1)

	"""Removes the root of the tree.
	@type node: AVLNode
	@param node: the node we want to remove from the tree.
	@rtype: AVLNode.
	@returns: the physically deleted node.
	@complexity: O(log n)
	"""
	def __removeRoot(self, node):
		real_left = node.getLeft().isRealNode()
		real_right = node.getRight().isRealNode()
		if (not real_left) and (not real_right):
			self.root = self.firstNode = self.lastNode = None
			return None
		elif not real_left:
			node = node.getRight()
			self.root = node
			node.setParent(None)
		elif not real_right:
			node = node.getLeft()
			self.root = node
			node.setParent(None)
		else:
			node = self.__removeNonRoot(self.__replaceWithSuccessor(node))
		return node

	"""Removes a non-root node from the tree.
	@type node: AVLNode
	@param node: the node we want to remove from the tree.
	@rtype: AVLNode
	@returns: the physically deleted node.
	@complexity: O(log n)
	"""
	def __removeNonRoot(self, node):
		parent = node.getParent()
		real_left = node.getLeft().isRealNode()
		real_right = node.getRight().isRealNode()
		left_son = parent.getLeft() == node
		if (not real_left) and (not real_right):
			AVLNode(None, True).setParentAndChild(parent, left_son)
		elif not real_left:
			node.getRight().setParentAndChild(parent, left_son)
		elif not real_right:
			node.getLeft().setParentAndChild(parent, left_son)
		else:
			node = self.__removeNonRoot(self.__replaceWithSuccessor(node))
		return node

	"""Replaces a node with it's successor
	@type node: AVLNode
	@param node: a node with 2 sons
	@rtype: AVLNode
	@returns: The new node which was put instead of the successor
	@complexity: O(log n)
	"""
	def __replaceWithSuccessor(self, node):
		parent = node.getParent()
		real_parent = parent is not None
		right = node.getRight()
		left = node.getLeft()
		next_node = AVLTreeList.__successor(node)
		next_node.setLeftAndParent(left)
		next_parent = next_node.getParent()
		if self.root == node:
			self.root = next_node
		if real_parent:
			next_node.setParentAndChild(parent, node == parent.getLeft())
		else:
			next_node.setParent(None)
		if next_node == right:
			node.setLeftAndParent(AVLNode(None, True))
			node.setRightAndParent(next_node.getRight())
			next_node.setRightAndParent(node)
		else:
			node = AVLNode(node.getValue())
			node.setRightAndParent(next_node.getRight())
			next_node.setRightAndParent(right)
			node.setParentAndChild(next_parent, True)
		node.setSize()
		node.setToCurHeight()
		node.setBF()
		next_node.setSize()
		next_node.setToCurHeight()
		next_node.setBF()
		return node

	"""Returns the node that contains the next item in the list.
	@type node: AVLNode
	@param node: a node
	@rtype: node
	@returns: a node that contains the next item in the list
	@complexity: O(log n)
	"""
	@staticmethod
	def __successor(node):
		if node.getRight().isRealNode():
			node = node.getRight()
			while node.getLeft().isRealNode():
				node = node.getLeft()
			return node
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
	@complexity: O(log n)
	"""
	@staticmethod
	def __predecessor(node):
		if node.getLeft().isRealNode():
			node = node.getLeft()
			while node.getRight().isRealNode():
				node = node.getRight()
			return node
		parent = node.getParent()
		while parent is not None and node == parent.getLeft():
			node = parent
			parent = node.getParent()
		return parent

	"""Rebalances the tree.
	@type node: AVLNode
	@param node: the parent of the physically deleted/inserted node, or the node which joins two trees.
	@type insert: int
	@param insert: indicates if rebalancing after insertion (0), deletion(1) or join(2)
	@rtype: int
	@returns: number of rotations made
	@complexity: O(log n)
	"""
	def __rebalance(self, node, insert=0):
		rotations = 0
		done = False
		while node is not None:
			height = node.getHeight()
			node.setToCurHeight()
			node.setSize()
			node.setBF()
			parent = node.getParent()
			if not done:
				if node.getBF() in [-1, 0, 1]:
					done = insert in [0, 1] and node.getHeight() == height
				else:
					rotations += self.__rotate(node)
					done = insert == 0
			node = parent
		return rotations

	"""Rotates around a node.
	@type node: AVLNode
	@rtype: int
	@return: number of rotations made (single or double rotation)
	@complexity: O(1)
	"""
	def __rotate(self, node):
		rotations = 1
		if node.getBF() == 2:
			left = node.getLeft()
			if left.getBF() == -1:
				AVLTreeList.__rotateLeft(left, left.getRight())
				rotations += 1
			AVLTreeList.__rotateRight(node, node.getLeft())
		else:
			right = node.getRight()
			if right.getBF() == 1:
				AVLTreeList.__rotateRight(right, right.getLeft())
				rotations += 1
			AVLTreeList.__rotateLeft(node, node.getRight())
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
		if self.empty():
			return None
		return self.firstNode.getValue()

	"""Returns the value of the last item in the list.
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.empty():
			return None
		return self.lastNode.getValue()

	"""Returns an array representing list (in order).
	@rtype: list
	@returns: a list of strings representing the data structure
	@complexity: O(n)
	"""
	def listToArray(self):
		if self.root is None:
			return []
		node = self.firstNode
		array = [node.getValue()]
		for i in range(self.root.getSize() - 1):
			next_node = AVLTreeList.__successor(node)
			if next_node.isRealNode():
				array.append(next_node.getValue())
			node = next_node
		return array

	"""Sort the info values of the list.
	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	@complexity: O(nlogn)
	"""
	def sort(self):
		arrayList = AVLTreeList.listToArray(self)
		AVLTreeList.mergeSort(arrayList)
		sortedTree = AVLTreeList.arrayToList(arrayList)
		
		return sortedTree
	"""
	Sorts arrays based on the known merge sort algorithm
	@type array: array
	@param array: array to sort
	@complexity: O(nlogn)
	"""
	def mergeSort(array):
		L = 0
		R = len(array)-1
		AVLTreeList.recMergeSort(array, L, R)
	
	"""
	Sorts arrays based on the known merge sort algorithm
	@type array: array
	@type L, R: int
	@param array: array to sort
	@param L: left index
	@param R: right index
	@complexity: O(nlogn)
	"""
	def recMergeSort(array, L, R):
		if R-L > 1:
			mid = (R-L)//2
			AVLTreeList.recMergeSort(array, L, mid-1)
			AVLTreeList.recMergeSort(array, mid, R)
			i = L
			j = mid
			k = 0
			while i < mid-1 and j < R:
				if array[i] <= array[j]:
					array[k] = array[i]
					i += 1
				else:
					array[k] = array[j]
					j += 1
				k += 1
			while i < mid-1:
				array[k] = array[i]
				i += 1
				k += 1
			while j < R:
				array[k] = array[j]
				j += 1
				k += 1

	"""Permute the info values of the list.
	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	@complexity: O(n)
	"""
	def permutation(self):
		arrayList = AVLTreeList.listToArray(self)
		shuffleArray = AVLTreeList.shuffle(arrayList)
		shuffleTree = AVLTreeList.arrayToList(shuffleArray)
		
		return shuffleTree

	"""Shuffle a given array.
	@type array: array
	@param array: the array to shuffle
	@rtype: array
	@returns: a shuffle array.
	@complexity: O(n)
	"""
	def shuffle(array):
		length = len(array)
		for i in range(length):
			j = random.randint(0, length-1)
			val1 = array[i]
			val2 = array[j]
			array[i] = val2
			array[j] = val1

		return array
	
	"""Concatenates lst to self.
	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	@complexity: o(logn - logm) when m is the size of shorter list. (n size of the longer list).
	"""
	def concat(self, lst):
		#edge cases empty lists:
		if self.getRoot() == None:
			if lst.getRoot() != None:
				self.setRoot(lst.getRoot())
				self.firstNode = lst.firstNode
				self.lastNode = lst.lastNode
				return lst.getRoot().getHeight() + 1
			else:
				return 0
		if lst.getRoot() == None:
			return self.getRoot().getHeight() + 1
		#regular cases:
		heightFirst = self.getRoot().getHeight()
		heightAfter = lst.getRoot().getHeight()
		dif = abs(heightFirst-heightAfter)
		sizeFirst = self.getRoot().getSize()
		if heightFirst >= heightAfter:
			newRoot = self.getRoot()
			curNode = self.getRoot()
			smallRoot = lst.getRoot()
			targetHeight = heightAfter
			Left = False
		else:
			newRoot = lst.getRoot()
			curNode = lst.getRoot()
			smallRoot = self.getRoot()
			targetHeight = heightFirst - 1
			Left = True
		nodeConnect = AVLNode("connection node")
		connectIndex = sizeFirst
		while curNode.getHeight() > targetHeight:
			if Left:
				curNode = curNode.getLeft()
			else:
				curNode = curNode.getRight()
		AVLTreeList.setChildsNRebalance(self, lst, curNode,smallRoot, nodeConnect, Left, newRoot, connectIndex)
		return dif

	"""
	Makes the necessary connections between nodes, and rebalance the tree.
	@type self, lst: AVLTreeList
	@type curNode: AVLNode
	@type smallRoot: AVLNode
	@type nodeConnect: AVLNode
	@type newRoot: AVLNode
	@type Left: boolean
	@type connectionIndex: int
	@param self: the origin list to concat
	@param lst: the list to concat
	@param curNode: the node in the larger tree that supposed to be the child of the connectNode
	@param smallRoot: the root of the smaller tree
	@param nodeConnect: the node that smallRoot and curNode supposed to be his children
	@param newRoot: the root of the new list
	@param Left: should it be left child?
	@param connectionIndex: index of the connection node
	@complexity: o(logn - logm) (m the size of the shorter list, n the size of the longer list)
	"""
	def setChildsNRebalance(self, lst, curNode,smallRoot, nodeConnect, Left, newRoot, connectIndex):
		newParent = curNode.getParent()
		if newParent == None:
			newParent = curNode
			if not Left:
				curNode = curNode.getRight()
			else:
				curNode = curNode.getLeft()
		curNode.setParentAndChild(nodeConnect, not Left)
		smallRoot.setParentAndChild(nodeConnect, Left)
		nodeConnect.setParentAndChild(newParent, Left)
		self.setRoot(newRoot)
		self.lastNode = lst.lastNode
		self.__rebalance(nodeConnect, 2)
		self.delete(connectIndex)
		self.__rebalance(nodeConnect.getParent(), 1)

	"""Searches for a *value* in the list.
	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	@complexity: O(n)
	"""
	def search(self, val):
		node = self.firstNode
		if node == None:
			return -1
		for i in range(self.getRoot().getSize()):
			if node.getValue() == val:
				return i
			node = self.__successor(node)
		return -1

	"""Returns the root of the tree representing the list.
	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root

	"""sets the root node of the tree
	@type: AVLNode
	@param: the new root.
	"""
	def setRoot(self, root):
		self.root = root
	
	"""
	makes a list from an array in O(n).
	@type: array
	@rtype: AVList
	@returns: the list
	@complexity: o(n)
	"""
	def arrayToList(array):
		if len(array) == 0:
			return AVLTreeList()
		tree = AVLTreeList.recArrayToList(array, 0, len(array)-1)
		tree.firstNode = AVLTreeList.edgeNode(tree.getRoot(), True)
		tree.lastNode = AVLTreeList.edgeNode(tree.getRoot(), False)
		return tree

	"""
	makes a list from an array in O(n).
	@ array type: array
	@ left, right type:
	@ array param: the array that will become a list
	@ left param: the smallest index
	@ right param: the largest index
	@rtype: AVList
	@returns: the list
	@complexity: O(n)
	"""
	def recArrayToList(array, left, right):
		mid = (left+right)//2
		tree = AVLTreeList()
		if right < left:
			tree.setRoot(AVLNode(None, True))
			return tree
		node = AVLNode(array[mid])
		node.setLeftAndParent(AVLTreeList.recArrayToList(array, left, mid-1).getRoot())
		node.setRightAndParent(AVLTreeList.recArrayToList(array, mid+1, right).getRoot())
		node.setBF()
		node.setToCurHeight()
		node.setSize()
		tree.setRoot(node)
		return tree

	"""
	finds the first element or last element in the list.
	@root type: AVLNode
	@ min type: boolean
	@root param: the root of the AVLTree
	@min param: true if we are looking for first item, false otherwise.
	@rtype: AVLNode
	@returns: the first/last element in the list
	@complexity: O(logn)
	"""
	def edgeNode(root, min = True):
		node = root
		if min == False:
			while node.getRight().isRealNode():
				node = node.getRight()
		else:
			while node.getLeft().isRealNode():
				node = node.getLeft()	
		return node
