import unittest
from simple_tree import *


class TestSimpleTreeMethods(unittest.TestCase):

    def test_AddChild(self):
        simple_tree = SimpleTree(None)
        self.assertEqual(simple_tree.GetAllNodes(), [])

        node_1 = SimpleTreeNode(1, None)
        simple_tree.AddChild(None, node_1)
        self.assertEqual(simple_tree.GetAllNodes(), [node_1])
        self.assertIsNone(node_1.Parent)
        self.assertEqual(simple_tree.Root, node_1)

        node_2 = SimpleTreeNode(2, None)
        simple_tree.AddChild(None, node_2)
        self.assertEqual(simple_tree.GetAllNodes(), [node_2])
        self.assertEqual(simple_tree.Root, node_2)

        simple_tree.AddChild(None, node_1)
        simple_tree.AddChild(node_1, node_2)
        self.assertEqual(simple_tree.GetAllNodes(), [node_1, node_2])
        self.assertEqual(simple_tree.Root, node_1)
        self.assertEqual(node_2.Parent, node_1)
        self.assertEqual(node_1.Children, [node_2])

    def test_DeleteNode(self):
        simple_tree = SimpleTree(None)
        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, None)
        simple_tree.AddChild(None, node_1)
        simple_tree.AddChild(node_1, node_2)
        simple_tree.DeleteNode(node_2)
        self.assertEqual(simple_tree.GetAllNodes(), [node_1])
        simple_tree.DeleteNode(node_1)
        self.assertEqual(simple_tree.GetAllNodes(), [])
        self.assertIsNone(simple_tree.Root)

    def test_GetAllNodes(self):
        simple_tree = SimpleTree(None)
        self.assertEqual(simple_tree.GetAllNodes(), [])
        root = SimpleTreeNode(0, None)
        simple_tree.AddChild(None, root)
        node_1 = SimpleTreeNode(1, None)
        simple_tree.AddChild(root, node_1)
        node_2 = SimpleTreeNode(2, None)
        simple_tree.AddChild(root, node_2)
        node_1_1 = SimpleTreeNode(11, None)
        node_1_2 = SimpleTreeNode(12, None)
        simple_tree.AddChild(node_1, node_1_1)
        simple_tree.AddChild(node_1, node_1_2)
        node_2_1 = SimpleTreeNode(21, None)
        node_2_2 = SimpleTreeNode(22, None)
        simple_tree.AddChild(node_2, node_2_1)
        simple_tree.AddChild(node_2, node_2_2)
        self.assertEqual(simple_tree.GetAllNodes(), [root, node_1, node_1_1, node_1_2,
                                                     node_2, node_2_1, node_2_2])

    def test_FindNodesByValue(self):
        simple_tree = SimpleTree(None)
        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, None)
        node_3 = SimpleTreeNode(3, None)
        node_4 = SimpleTreeNode(4, None)
        node_5_1 = SimpleTreeNode(1, None)
        simple_tree.AddChild(None, node_1)
        simple_tree.AddChild(node_1, node_2)
        simple_tree.AddChild(node_2, node_3)
        simple_tree.AddChild(node_2, node_4)
        simple_tree.AddChild(node_4, node_5_1)
        self.assertEqual(simple_tree.FindNodesByValue(1), [node_1, node_5_1])
        self.assertEqual(simple_tree.FindNodesByValue(2), [node_2])
        self.assertEqual(simple_tree.FindNodesByValue(3), [node_3])
        self.assertEqual(simple_tree.FindNodesByValue(4), [node_4])

    def test_MoveNode(self):
        simple_tree = SimpleTree(None)
        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, None)
        node_3 = SimpleTreeNode(3, None)
        node_4 = SimpleTreeNode(4, None)
        simple_tree.AddChild(None, node_1)
        simple_tree.AddChild(node_1, node_2)
        simple_tree.AddChild(node_2, node_3)
        simple_tree.AddChild(node_3, node_4)
        self.assertEqual(len(node_1.Children), 1)
        self.assertEqual(len(node_2.Children), 1)
        self.assertEqual(node_3.Parent, node_2)
        self.assertEqual(node_4.Parent, node_3)
        simple_tree.MoveNode(node_3, node_1)
        self.assertEqual(len(node_2.Children), 0)
        self.assertEqual(len(node_1.Children), 2)
        self.assertEqual(node_3.Parent, node_1)
        self.assertEqual(node_4.Parent, node_3)

    def test_Count(self):
        simple_tree = SimpleTree(None)
        self.assertEqual(simple_tree.Count(), 0)

        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, None)
        node_3 = SimpleTreeNode(3, None)
        node_4 = SimpleTreeNode(4, None)

        simple_tree.AddChild(None, node_1)
        simple_tree.AddChild(node_1, node_2)
        simple_tree.AddChild(node_1, node_3)
        simple_tree.AddChild(node_1, node_4)
        self.assertEqual(simple_tree.Count(), 4)

    def test_LeafCount(self):
        simple_tree = SimpleTree(None)
        self.assertEqual(simple_tree.LeafCount(), 0)

        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, None)
        node_3 = SimpleTreeNode(3, None)
        node_4 = SimpleTreeNode(4, None)

        simple_tree.AddChild(None, node_1)
        simple_tree.AddChild(node_1, node_2)
        simple_tree.AddChild(node_1, node_3)
        simple_tree.AddChild(node_1, node_4)

        self.assertEqual(simple_tree.LeafCount(), 3)

    def test_set_the_level(self):
        simple_tree = SimpleTree(None)
        self.assertFalse(simple_tree.set_the_level())

        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, None)
        node_3 = SimpleTreeNode(3, None)
        node_4 = SimpleTreeNode(4, None)

        simple_tree.AddChild(None, node_1)
        simple_tree.AddChild(node_1, node_2)
        simple_tree.AddChild(node_2, node_3)
        simple_tree.AddChild(node_3, node_4)

        simple_tree.set_the_level()
        self.assertTrue(simple_tree.set_the_level())
        self.assertEqual(node_1.level, 0)
        self.assertEqual(node_2.level, 1)
        self.assertEqual(node_3.level, 2)
        self.assertEqual(node_4.level, 3)



if __name__ == '__main__':
    unittest.main()
