from typing import Generator


class TotalOrderGraph:
    """Graph that interprets total order relations between nodes."""

    def __init__(self, nodes: int):
        if nodes < 1:
            raise ValueError("Number of nodes must be at least 1.")

        self.n = nodes
        self.lower: list[int] = [node + 1 for node in range(nodes)]
        self.upper: list[int] = [node - 1 for node in range(nodes)]
        self.lower[-1] = -1  # Last node points to no points
        self.upper[0] = -1  # First node is pointed by no points
        self.head = 0
        self.children: list[set[int]] = []
        for i in range(nodes):
            self.children.append(set(range(i + 1, nodes)))

    def add_edges(self, edges: list[tuple[int, int]]):
        """
        Add multiple edges to the graph.

        Args:
            edges (list[tuple[int, int]]): List of edges to add, where each edge is a
            tuple (big, small) and they are ordered from least to most important edge.
        """

        for big, small in edges:
            self.add_edge(big, small)

    def add_edge(self, big: int, small: int):
        if not (0 <= big < self.n and 0 <= small < self.n):
            raise ValueError("Both nodes must be in the graph.")

        if small in self.children[big]:
            return  # If big > small is already true, do nothing

        if self.head == small:
            self.head = big

        # Remove big from its current position
        low = self.lower[big]
        high: int = self.upper[big]
        self.lower[high] = low
        if low != -1:
            self.upper[low] = high

        if high != small:
            high = self.upper[high]
            while high != -1:
                self.children[high].remove(big)
                if high == small:
                    break
                high = self.upper[high]

        # Add big before small
        high = self.upper[small]
        if high != -1:
            self.lower[high] = big
        self.upper[big] = high
        self.lower[big] = small
        self.upper[small] = big

        self.children[big] = self.children[small].copy()
        self.children[big].add(small)

    def get_order(self) -> Generator[int, None, None]:
        yield self.head

        current = self.lower[self.head]
        while current != -1:
            yield current
            current = self.lower[current]


if __name__ == "__main__":
    candidates = [3, 1, 2, 4, 0]
    vote = [4, 3, 1, 5, 2]
    edges = [
        (4, 0),
        (0, 3),
        (2, 1),
        (4, 3),
        (1, 3),
        (2, 3),
        (1, 0),
        (4, 1),
        (2, 0),
        (2, 4),
    ]
    graph = TotalOrderGraph(5)
    graph.add_edges(edges)
    result = [candidates[node] for node in graph.get_order()]
    print(
        result,
        [(candidates[candidate], position) for candidate, position in enumerate(vote)],
        [result[position - 1] for candidate, position in enumerate(vote)],
    )
    assert all(
        result[position - 1] == candidates[candidate]
        for candidate, position in enumerate(vote)
    )
