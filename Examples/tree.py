class TreeNode:
    def __init__(self , data, childern = []):
        self.data = data
        self.children = childern
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

# level 1
# traverse through ur tree
def tree_tra():
  for i in tree.children:
      c = i
      print(i.data, ":" )
      for j in c.children:
          print("  " , j.data)