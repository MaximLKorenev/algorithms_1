class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = 0


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):

        if ParentNode is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):

        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
        else:
            if self.Root == NodeToDelete:
                self.Root = None
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        list_nodes = []
        root = self.Root
        if root is None:
            return list_nodes

        def get_nodes(list_node, root):
            list_node.append(root)
            for child in root.Children:
                get_nodes(list_node, child)

        get_nodes(list_nodes, root)
        return list_nodes


    def FindNodesByValue(self, val):
        list_nodes = []
        for node in self.GetAllNodes():
            if node.NodeValue == val:
                list_nodes.append(node)
        return list_nodes

    def MoveNode(self, OriginalNode, NewParent):

        self.DeleteNode(OriginalNode)
        if NewParent is None:
            self.Root = OriginalNode
        else:
            NewParent.Children.append(OriginalNode)
            OriginalNode.Parent = NewParent

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        leaf_count = 0
        for node in self.GetAllNodes():
            if not node.Children:
                leaf_count += 1
        return leaf_count

    def set_the_level(self):
        list_nodes = self.GetAllNodes()
        if not list_nodes:
            return False

        for node in list_nodes:
            if node.Parent is None:
                node.level = 0
            else:
                node.level = node.Parent.level + 1
        return True

    def CountSubTree(node):

        def f(acc, x):
            return acc + 1

        return SimpleTree.FoldTree(f, 0, node)

    def FoldTree(f, acc, root_node):
        if root_node is None:
            return acc
        acc1 = f(acc, root_node)
        for elem in root_node.Children:
            acc1 = SimpleTree.FoldTree(f, acc1, elem)
        return acc1

    def EvenTrees(self):
        def isEven(num):
            return (num % 2) == 0

        def EvenTreesRec(node, parent):
            if len(node.Children) == 0:
                return []
            edges_to_remove = []
            count = SimpleTree.CountSubTree(node)
            if isEven(count) and parent is not None:
                edges_to_remove.append((parent, node))
            for c in node.Children:
                edges_to_remove.extend(EvenTreesRec(c, node))
            return edges_to_remove

        count = self.Count()
        if not isEven(count) or count == 0:
            return []

        edge_list = EvenTreesRec(self.Root, None)
        result = []
        for e in edge_list:
            (n1, n2) = e
            result.append(n1)
            result.append(n2)
        return result