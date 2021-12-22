class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


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
        return []

    def FindNodesByValue(self, val):

        return []

    def MoveNode(self, OriginalNode, NewParent):

        self.DeleteNode(OriginalNode)
        if NewParent is None:
            self.Root = OriginalNode
        else:
            NewParent.Children.append(OriginalNode)
            OriginalNode.Parent = NewParent

    def Count(self):
        # количество всех узлов в дереве
        return 0

    def LeafCount(self):
        # количество листьев в дереве
        return 0