# Mathematical Background

This document provides the mathematical foundation and theoretical background for the Ranked Pairs voting method implemented in this package.

## Overview of Ranked Pairs

The Ranked Pairs method, also known as Tideman's method, is a Condorcet voting method that produces a complete ranking of candidates by constructing a directed acyclic graph based on pairwise comparisons.

## Algorithm Description

### Step 1: Pairwise Comparison Matrix

For each pair of candidates (i, j), we count the number of voters who prefer candidate i over candidate j.

Let **P(i,j)** = number of voters who prefer candidate i over candidate j

The pairwise comparison can be represented as a matrix where:
- Rows represent the "preferred" candidate
- Columns represent the "less preferred" candidate  
- Entry (i,j) contains P(i,j)

### Step 2: Victory Margins

For each pair of candidates (i, j), the victory margin is calculated as:

**M(i,j) = P(i,j) - P(j,i)**

If M(i,j) > 0, then candidate i defeats candidate j with margin M(i,j).

### Step 3: Pair Ranking

All winning pairs are sorted by their victory margins in descending order. This creates a priority ordering for adding edges to the graph.

### Step 4: Graph Construction

Starting with an empty directed graph:

1. Consider pairs in order of decreasing margin strength
2. For each pair (i,j) with i defeating j:
   - Add edge i → j if it doesn't create a cycle
   - Skip the edge if it would create a cycle

### Step 5: Topological Sort

The final ranking is determined by a topological sort of the resulting directed acyclic graph.

## Mathematical Properties

### Condorcet Criterion

**Definition**: A voting method satisfies the Condorcet criterion if it always selects the Condorcet winner when one exists.

**Condorcet Winner**: A candidate who defeats every other candidate in pairwise comparison.

**Proof**: Ranked Pairs satisfies the Condorcet criterion because:
1. The Condorcet winner defeats all other candidates
2. No edge towards the Condorcet winner is established
3. The Condorcet winner will only have outgoing edges, making them the top-ranked candidate

### Monotonicity

**Definition**: A voting method is monotonic if improving a candidate's position in some votes cannot worsen their final ranking.

**Proof Sketch**: Ranked Pairs is monotonic because:
1. Improving a candidate's ranking increases their pairwise victory margins
2. Higher margins increase the priority of their winning pairs
3. Higher priority pairs are more likely to be included in the final graph
4. More included winning pairs improve the candidate's final position

### Independence of Clones

**Definition**: Adding or removing a set of similar candidates should not affect the relative ranking of dissimilar candidates.

Ranked Pairs satisfies this criterion with some technical conditions related to how "clones" are defined. A good definition would be that all clones are always voted sequentially. It can be proved that you could collapse this block into a single node and that the order between them also does not impact the final graph.

### Smith Criterion

**Definition**: The winner should come from the Smith set (the smallest non-empty set of candidates who defeat all candidates outside the set).

Ranked Pairs satisfies the Smith criterion by definition since the partial order it defines will always satisfy this. You can see this collapsing the set into a single node maintaining the minimum margin outwards which would still be winning.

## Tie Resolution

### Handling Tied Pairwise Comparisons

When P(i,j) = P(j,i), we have a tied pairwise comparison. The algorithm handles this by:

1. Randomly selecting the direction of the edge (i→j or j→i)
2. Assigning this edge a margin of 0
3. Adding tied pairs to the graph after all decisive pairs

This approach ensures:
- **Fairness**: No systematic bias toward any candidate
- **Completeness**: All candidates receive a ranking
- **Determinism**: Given the same random seed, results are reproducible

### Mathematical Justification

The random tie-breaking method is mathematically sound because:

1. **Symmetry**: Each tied pair has equal probability of either direction
2. **Independence**: Tie resolution doesn't affect decisive pairs
3. **Neutrality**: The method treats all candidates equally

### Derived Questions

#### Wouldn't randomness be unrepresentative?

A tie has already be caused, if you treat the pairwise-margins as a knowledgebase of preferences, there is no preference between either one winning.

#### Aren't some ties different than others?

Yes, a 50-50 tie is not the same as a tie because everyone voted two options the same. We could consider the first more _controversial_. However, you really cannot take controversy into account a lot or the algorithm starts to break.

#### Why can't there be ties in the final ranking?

In some cases these ties are unsolvable, meaning the is several valid and distinct rankings that satisfy it. You could always implement a way to evaluate this and add ties into the result if possible, I'm waiting for your PR ;)

## Complexity Analysis

### Time Complexity

Let n = number of candidates, v = number of voters.

1. **Pairwise Comparisons**: O(n² × v)
   - For each of the n² pairs, examine all v votes

2. **Margin Calculation**: O(n²)
   - Calculate margin for each pair

3. **Sorting**: O(n² log n)
   - Sort all pairs by margin

4. **Graph Construction**: O(n²)
   - For each of O(n²) pairs, check for cycles in O(1) time (due to extra space).

5. **Topological Sort**: O(n log n)
   - Standard topological sort on dense graph

**Overall**: O(n² × v + n² log n)

For typical elections where v >> n, this simplifies to **O(n² × v)**.

### Space Complexity

1. **Pairwise Matrix**: O(n²)
2. **Graph Representation**: O(n²)
3. **Vote Storage**: O(n × v)

**Overall**: O(n² + n × v)

## Examples with Mathematical Analysis

### Example 1: Simple Three-Candidate Election

**Candidates**: A, B, C  
**Votes**: 
- 3 voters: A > B > C
- 2 voters: B > C > A  
- 2 voters: C > A > B

**Pairwise Matrix**:
```
    A  B  C
A   -  3  5
B   4  -  2
C   2  5  -
```

**Victory Margins**:
- A defeats B: 3 - 4 = -1 (B defeats A by 1)
- A defeats C: 5 - 2 = 3
- B defeats C: 2 - 5 = -3 (C defeats B by 3)

**Sorted Pairs**:
1. A > C (margin 3)
2. C > B (margin 3)  
3. B > A (margin 1)

**Graph Construction**:
1. Add A → C ✓
2. Add C → B ✓
3. Add B → A ✗ (would create cycle A → C → B → A)

**Final Ranking**: A > C > B

### Example 2: Condorcet Paradox

**Candidates**: X, Y, Z  
**Votes**:
- 3 voters: X > Y > Z
- 3 voters: Y > Z > X
- 3 voters: Z > X > Y

**Pairwise Matrix**:
```
    X  Y  Z
X   -  3  6
Y   6  -  3
Z   3  6  -
```

**Victory Margins**:
- Y defeats X: 6 - 3 = 3
- Z defeats Y: 6 - 3 = 3
- X defeats Z: 6 - 3 = 3

All margins are equal! The tie-breaking mechanism determines the final order.

## Theoretical Guarantees

### Arrow's Impossibility Theorem

Arrow's theorem states that no voting method can simultaneously satisfy all of the following criteria:
1. Unrestricted domain
2. Non-dictatorship  
3. Pareto efficiency
4. Independence of irrelevant alternatives

Ranked Pairs satisfies criteria 1, 2, and 3, but not 4 (independence of irrelevant alternatives).

### Gibbard-Satterthwaite Theorem

This theorem proves that no deterministic voting method can be both strategy-proof and non-dictatorial. Ranked Pairs is not strategy-proof, but this is unavoidable for any meaningful voting system.

## Computational Considerations

### Efficiency

1. **Total Order Graph**: This part is probably very optimizable

### Parallel Processing

Several parts of the algorithm can be parallelized:

1. **Pairwise Comparisons**: Independent for each pair
2. **Margin Calculation**: Embarrassingly parallel
3. **Total Order Graph**: Currently unbeknown to me

## Going forward

1. Explore how to include in the algorithm weak preferences, currently voters having to chose between risking including those and causing the No Show Paradox, or being underrepresented.

## References

1. Tideman, T. N. (1987). "Independence of clones as a criterion for voting rules". Social Choice and Welfare, 4(3), 185-206.

2. Schulze, M. (2003). "A new monotonic and clone-independent single-winner election method". Voting matters, 17, 9-19.

3. Arrow, K. J. (1951). "Social Choice and Individual Values". Yale University Press.

4. Gibbard, A. (1973). "Manipulation of voting schemes: a general result". Econometrica, 41(4), 587-601.

5. Condorcet, M. de (1785). "Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix".

## Mathematical Notation Summary

- **n**: Number of candidates
- **v**: Number of voters  
- **P(i,j)**: Number of voters preferring candidate i over j
- **M(i,j)**: Victory margin of candidate i over j
