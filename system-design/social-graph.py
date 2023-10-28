from collections import deque


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.connections = []

    def add_connection(self, user):
        self.connections.append(user)

    def show_user(self):
        return (
            "self.user_id:"
            + str(self.user_id)
            + " self.name: "
            + self.name
            # + " self.connections: "
            # + "".join(self.connections)
        )


class SocialGraph:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def add_connection(self, user_id_1, user_id_2):
        user_1 = self.users[user_id_1]
        user_2 = self.users[user_id_2]
        user_1.add_connection(user_2)
        user_2.add_connection(user_1)

    def print_users(self):
        for k in self.users.keys():
            print(self.users[k].show_user())

    def shortest_path(self, user_id_1, user_id_2):
        start = self.users[user_id_1]
        end = self.users[user_id_2]
        return self._bfs_shortest_path(start, end)

    def _bfs_shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start.user_id])])

        while queue:
            current, path = queue.popleft()

            if current == end:
                return path

            for connection in current.connections:
                if connection not in visited:
                    visited.add(connection)
                    new_path = list(path)
                    new_path.append(connection.user_id)
                    queue.append((connection, new_path))

        return None


# Usage:
graph = SocialGraph()
graph.add_user(1, "Alice")
graph.add_user(2, "Bob")
graph.add_user(3, "Charlie")
graph.add_user(4, "David")
graph.add_user(4, "Tim")

graph.add_connection(1, 2)
graph.add_connection(2, 3)
graph.add_connection(3, 4)

path = graph.shortest_path(1, 4)
print(path)  # Output: [1, 2, 3, 4]
graph.print_users()
