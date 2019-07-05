class NotFoundFile(Exception):
    def __init__(self, path):
        self.path = path
        super().__init__(f"El path '{path}' no es válido")


class InvalidTree(Exception):
    def __init__(self, tree):
        self.tree = tree
        super().__init__(f"El árbol con raíz {tree} no es un AlgarroboTree")


class NotFoundValue(Exception):
    pass
