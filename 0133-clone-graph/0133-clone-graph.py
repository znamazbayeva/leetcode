"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m, visited, queue = {}, set(), collections.deque([node])
        while queue:
            top = queue.popleft()
            if top not in m:
                m[top] = Node(top.val)
            if top in visited:
                continue
            else: 
                visited.add(top)
            for i in top.neighbors:
                if i not in m:
                    m[i] = Node(i.val)
                queue.append(i)
                m[top].neighbors.append(m[i])
        return m[node]
            
        