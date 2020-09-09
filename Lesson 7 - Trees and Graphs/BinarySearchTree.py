# Author: Reecha Khanal
# Date: 8th Sept 2020
# BST class shows the implementation of insertion, removal and deletion methods in a binary search tree
class BST:
	def __init__(self, value):
		self.value = val
		self.left = None
		self.right = None

	def insert(self, value):
		
		root = self
		while root:
			# while loops stops when root reaches null hinting that we are at a leaf node
			if value < root.val:
				if root.left:
					# move to the left subtree
					root = root.left
				else:
					root.left = BST(value)
					# insertion complete
					break;
			# assuming that equal values are allowed in BST
			# and equal values go towards the right subtree
			elif value >= right:
				if root.right:
					# move to the right subtree
					root = root.right
				else:
					root.right = BST(value)
					# insertion complete
					break;
		return self

	def contains(self, value):
		root = self
		while root:
			if value < root.val:
				root = root.left
			elif value > root.val:
				root = root.right
			else:
				# the the value is equal to the value of the current Node
				return True
		# we were not able to find the value and exited the loop
		return False

	def remove(self, value, parentNode=None):
		# finding the value to be removed
		root = self
		while root:
			if value < root.val:
				# search in left subtree
				parentNode = root
				root = root.left
			elif value > root.val:
				# search in right subtree
				parentNode = root
				root = root.right
			else:
				# we found the value to be removed
				if root.left and root.right:
					# the root has both children
					# find minimum value in right subtree
					root.value = getMinNode(self)
					root.right.remove(root.value, root.right)

				elif parentNode is None:
					# we found our element of choice in the root
					if root.left:
						root.value = root.left.value
						root.left = root.left.left
						root.right = root.left.right
					elif root.right:
						root.value = root.right.value
						root.left = root.right.left
						root.right = root.right.right
					else:
						# this is a single node tree; # we do nothing in this case
						pass
				elif parentNode.left == current:
					parentNode.left = root.left if root.left else root.right
				elif parentNode.right == current:
					parentNode.right = root.left if root.left else root.right
		return self

	def getMinNode(self):
		root = self
		while root.left:
			root = root.left

		return root.value