# vector_clock.py
class VectorClock:
    def __init__(self, nodes):
        self.vector = {node: 0 for node in nodes}

    def increment(self, node):
        self.vector[node] += 1

    def update(self, other_vector):
        for node, time in other_vector.items():
            self.vector[node] = max(self.vector[node], time)

    def __getitem__(self, node):
        return self.vector[node]

    def __str__(self):
        return str(self.vector)
