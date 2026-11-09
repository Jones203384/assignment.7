from collections import deque


class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side):
        if side not in ("left", "right") or self.root is None:
            return False

        queue = deque([self.root])
        while queue:
            parent = queue.popleft()
            if parent.name == parent_name:
                if getattr(parent, side) is not None:
                    return False
                setattr(parent, side, DoctorNode(employee_name))
                return True

            if parent.left is not None:
                queue.append(parent.left)
            if parent.right is not None:
                queue.append(parent.right)

        return False

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]



# Test your DoctorTree and DoctorNode classes here
