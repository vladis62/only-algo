class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.read_users = set()
        self.write_users = set()


class Tree:
    def __init__(self):
        self.root = Node('/')

    def find_node(self, path):
        components = path.split('/')
        current_node = self.root
        for component in components:
            if not component:
                continue
            found = False
            for child in current_node.children:
                if child.name == component:
                    current_node = child
                    found = True
                    break
            if not found:
                return None
        return current_node

    def grant_access(self, user, mode, path):
        node = self.find_node(path)
        if node:
            if mode == "read":
                node.read_users.add(user)
            elif mode == "write":
                node.write_users.add(user)
            return "done"
        else:
            return "node not found"

    def block_access(self, user, mode, path):
        node = self.find_node(path)
        if node:
            if mode == "read":
                node.read_users.discard(user)
            elif mode == "write":
                node.write_users.discard(user)
            return "done"
        else:
            return "node not found"

    def check_access(self, user, mode, path):
        node = self.find_node(path)
        if node:
            if mode == "read" and self.check_read_access(user, node):
                return "allowed"
            elif mode == "write" and self.check_write_access(user, node):
                return "allowed"
            else:
                return "forbidden"
        else:
            return "node not found"

    def check_read_access(self, user, node):
        if user in node.read_users:
            return True
        if node == self.root:
            return False
        return self.check_read_access(user, node.parent)

    def check_write_access(self, user, node):
        if user in node.write_users:
            return True
        if node == self.root:
            return False
        return self.check_write_access(user, node.parent)


def main():
    tree = Tree()

    while True:
        command = input().split()
        operation = command[0]
        user = command[1]
        mode = command[2]
        path = command[3]

        if operation == "grant":
            result = tree.grant_access(user, mode, path)
        elif operation == "block":
            result = tree.block_access(user, mode, path)
        else:
            result = tree.check_access(user, mode, path)

        print(result)


if __name__ == '__main__':
    main()
