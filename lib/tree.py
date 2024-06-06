class Tree:
    def __init__(self, node):
        self.node = node
        self.children = []

    def get_element_by_id(self, id):
        def dfs(node, id):
            if node['id'] == id:
                return node
            for child in node.get('children', []):
                
              result = dfs(child, id)
              if result:
                  return result
            return None
        return dfs(self.node, id)


    from collections import deque

    class Tree:
        def __init__(self, node):
            self.node = node
            self.children = []

        def get_element_by_id(self, id):
            queue



    from collections import deque

    class Tree:
        def __init__(self, node):
            self.node = node
            self.children = []



        def get_element_by_id(self,)