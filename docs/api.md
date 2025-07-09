# API Reference

## Functions

### `ranked_pairs_voting(candidates, votes)`

Performs Ranked Pairs voting on the given candidates and votes.

**Parameters:**

- **candidates** (`list[str]`): A list of candidate names in order. The position of each candidate in this list corresponds to their index in the vote rankings.

- **votes** (`list[list[int]]`): A list of preference rankings for each voter. Each vote is a list where:
  - The position corresponds to the candidate index in the `candidates` list
  - Lower numbers indicate higher preference (1 = most preferred)
  - Equal numbers indicate tied preferences
  - All votes must have the same length as the candidates list

**Returns:**

- `list[str]`: An ordered list of candidate names from winner (first place) to last place.

**Raises:**

- **ValueError**: If the input parameters are invalid (e.g., empty candidates list, mismatched vote lengths)

**Example:**

```python
from rankedpairsvoting import ranked_pairs_voting

candidates = ['Alice', 'Bob', 'Charlie']
votes = [
    [1, 2, 3],  # Alice > Bob > Charlie
    [2, 1, 3],  # Bob > Alice > Charlie
    [1, 3, 2],  # Alice > Charlie > Bob
]

result = ranked_pairs_voting(candidates, votes)
# Returns: ['Alice', 'Bob', 'Charlie'] (Alice wins)
```

**Algorithm Details:**

1. **Pairwise Comparison**: For each pair of candidates (i, j), count how many voters prefer candidate i over candidate j
2. **Margin Calculation**: Calculate the victory margin for each winning pair as the difference in pairwise votes
3. **Pair Sorting**: Sort all winning pairs by their victory margins in descending order
4. **Graph Construction**: Add pairs to a directed graph in order of margin strength, skipping pairs that would create cycles
5. **Topological Sort**: Generate the final ranking using a topological sort of the resulting graph

**Tie Handling:**

When two candidates are tied in pairwise comparison, the algorithm randomly determines the direction of the edge to add to the graph. This ensures fairness and prevents systematic bias toward any particular candidate ordering.

## Classes

### `PartialOrderGraph`

Internal class used to construct and maintain a directed acyclic graph for candidate ordering.

#### `__init__(nodes: int)`

Initialize a graph with the specified number of nodes.

**Parameters:**
- **nodes** (`int`): Number of nodes (must be at least 1)

**Raises:**
- **ValueError**: If nodes < 1

#### `add_edge(big: int, small: int)`

Add a directed edge from the `big` node to the `small` node, maintaining the partial order property.

**Parameters:**
- **big** (`int`): Source node (higher in ordering)
- **small** (`int`): Target node (lower in ordering)

**Behavior:**
- Updates transitive relationships automatically
- Ignores edges that would create cycles
- Maintains parent-child relationships for all nodes

**Raises:**
- **ValueError**: If either node is not in the graph or if adding edge to self

#### `add_edges(edges: list[tuple[int, int]])`

Add multiple directed edges to the graph in order of importance.

**Parameters:**
- **edges** (`list[tuple[int, int]]`): A list of (big, small) tuples representing edges to add, ordered from most to least important

**Behavior:**
- Calls `add_edge` for each pair in sequence
- Most important edges are added first and have priority

#### `get_total_order() -> list[int]`

Return the total ordering of nodes based on the current edge structure.

**Returns:**
- `list[int]`: Ordered list of node indices from highest to lowest in the total order

**Raises:**
- **ValueError**: If the graph does not represent a total order (e.g., has multiple heads or tails)

**Algorithm:**
The method finds the head of the graph (node with no parents) and follows the chain of direct children to construct the total ordering.

## Type Definitions

```python
# Type aliases for clarity
Candidate = str
Vote = list[int]
Candidates = list[Candidate]
Votes = list[Vote]
Ranking = list[Candidate]
```

## Error Handling

The package includes robust error handling for common issues:

### Input Validation

- Empty candidate lists
- Mismatched vote and candidate list lengths
- Invalid vote values (non-integers, negative numbers)
- Duplicate candidate names

### Runtime Errors

- Graph construction failures
- Memory issues with very large elections

## Performance Considerations

### Time Complexity

- **Pairwise Comparisons**: O(n² × v) where n = candidates, v = votes
- **Sorting Pairs**: O(n² log n)
- **Graph Construction**: O(n²)
- **Simple Topological Sort**: O(n)
- **Overall**: O(n² × v + n² log n)

### Space Complexity

- **Pairwise Matrix**: O(n²)
- **Graph Storage**: O(n²)
- **Overall**: O(n² + n × v)

## Examples

### Complete Election Example

```python
from rankedpairsvoting import ranked_pairs_voting

# Municipal election with 4 candidates
candidates = ['Smith', 'Johnson', 'Williams', 'Brown']

# 7 voters with different preferences
votes = [
    [1, 2, 3, 4],  # Smith > Johnson > Williams > Brown
    [2, 1, 4, 3],  # Johnson > Smith > Brown > Williams  
    [1, 3, 2, 4],  # Smith > Williams > Johnson > Brown
    [3, 1, 2, 4],  # Johnson > Williams > Smith > Brown
    [1, 2, 3, 4],  # Smith > Johnson > Williams > Brown
    [2, 1, 3, 4],  # Johnson > Smith > Williams > Brown
    [4, 3, 2, 1],  # Brown > Williams > Johnson > Smith
]

result = ranked_pairs_voting(candidates, votes)
print(f"Election Results:")
for i, candidate in enumerate(result, 1):
    print(f"{i}. {candidate}")
```

### Handling Edge Cases

```python
# Single candidate (trivial case)
result = ranked_pairs_voting(['Alice'], [[1]])
# Returns: ['Alice']

# All candidates tied
result = ranked_pairs_voting(
    ['A', 'B', 'C'], 
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
)
# Returns: Random ordering of ['A', 'B', 'C']

# Complex preference patterns
candidates = ['X', 'Y', 'Z']
votes = [
    [1, 2, 3],  # X > Y > Z
    [2, 3, 1],  # Z > X > Y  
    [3, 1, 2],  # Y > Z > X
]
# This creates a Condorcet cycle, resolved by margin strength
result = ranked_pairs_voting(candidates, votes)
```
