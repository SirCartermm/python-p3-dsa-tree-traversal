import unittest
from lib.tree import Tree

class TestGetElementId(unittest.TestCase):
    def test_find_node_by_id(self):
        node = {'id': 'root','children': [
            {'id: 'child', 'children': [
                {'id': 'grandchild1', 'children': []},
                 {'id': 'grandchild2', 'children': []}}
                  
             ]},
             {'id': 'child2, 'children': []}
              
            []}
        tree = Tree(node)
        self.assertEqual(tree.get_element_by_id('grandchild1')['id'], 'grandchild' )
        self.assertEqual(tree.get_element_by_id('child'2)['id'], 'child2')

    def test_node_not_found(self):
        node = {'id': 'root', 'children': []}
        tree = Tree(node)
        self.assertIsNone(tree.get_element_by_id('non-existent -id'))

    def test_empty_tree(self)
        
        