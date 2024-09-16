class BinaryTree:
    def __init__(self, value):
        self.value = value  # Valor es un objeto de tipo BSTEntry
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)