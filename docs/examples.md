# Examples and Use Cases

This document provides comprehensive examples of using the Ranked Pairs Voting package in various scenarios.

## Basic Examples

### Simple Three-Candidate Election

```python
from rankedpairsvoting import ranked_pairs_voting

# Define candidates
candidates = ['Alice', 'Bob', 'Charlie']

# Define votes (lower numbers = higher preference)
votes = [
    [1, 2, 3],  # Voter 1: Alice > Bob > Charlie
    [2, 1, 3],  # Voter 2: Bob > Alice > Charlie
    [1, 3, 2],  # Voter 3: Alice > Charlie > Bob
    [2, 1, 3],  # Voter 4: Bob > Alice > Charlie
    [1, 2, 3],  # Voter 5: Alice > Bob > Charlie
]

result = ranked_pairs_voting(candidates, votes)
print("Election result:", result)
```

### Election with Tied Preferences

```python
candidates = ['Option A', 'Option B', 'Option C']
votes = [
    [1, 1, 2],  # A = B > C (voters can express ties)
    [2, 1, 1],  # B = C > A
    [1, 2, 2],  # A > B = C
    [1, 2, 3],  # A > B > C
    [2, 1, 3],  # B > A > C
]

result = ranked_pairs_voting(candidates, votes)
print("Result with ties:", result)
```

## Real-World Use Cases

### 1. Committee Chair Selection

```python
# Academic department selecting a committee chair
candidates = [
    'Dr. Smith',
    'Dr. Johnson', 
    'Dr. Williams',
    'Dr. Brown',
    'Dr. Davis'
]

# Faculty members' preferences
votes = [
    [2, 1, 3, 4, 5],  # Faculty 1 prefers Johnson first
    [1, 3, 2, 5, 4],  # Faculty 2 prefers Smith first
    [3, 2, 1, 4, 5],  # Faculty 3 prefers Williams first
    [1, 2, 4, 3, 5],  # Faculty 4 prefers Smith first
    [2, 1, 4, 3, 5],  # Faculty 5 prefers Johnson first
    [1, 4, 2, 3, 5],  # Faculty 6 prefers Smith first
    [3, 1, 2, 5, 4],  # Faculty 7 prefers Williams first
]

chair = ranked_pairs_voting(candidates, votes)
print(f"Selected Committee Chair: {chair[0]}")
print(f"Full ranking: {chair}")
```

### 2. Restaurant Group Decision

```python
# Friends deciding where to eat
restaurants = [
    'Italian Bistro',
    'Sushi Palace', 
    'Burger Joint',
    'Thai Garden',
    'Pizza Corner'
]

# Each person's preferences
preferences = [
    [1, 3, 5, 2, 4],  # Person 1: Italian > Thai > Sushi > Pizza > Burger
    [2, 1, 4, 3, 5],  # Person 2: Sushi > Italian > Thai > Burger > Pizza
    [3, 4, 1, 5, 2],  # Person 3: Burger > Pizza > Italian > Sushi > Thai
    [4, 2, 3, 1, 5],  # Person 4: Thai > Sushi > Burger > Italian > Pizza
    [1, 2, 4, 3, 5],  # Person 5: Italian > Sushi > Thai > Burger > Pizza
]

choice = ranked_pairs_voting(restaurants, preferences)
print(f"Group choice: {choice[0]}")
```

### 3. Software Feature Prioritization

```python
# Development team prioritizing features
features = [
    'User Authentication',
    'Dashboard Analytics',
    'Mobile App',
    'API Integration',
    'Real-time Notifications'
]

# Team members' priority rankings
team_votes = [
    [1, 3, 4, 2, 5],  # Developer 1
    [2, 1, 5, 3, 4],  # Developer 2  
    [1, 2, 3, 5, 4],  # Product Manager
    [3, 1, 2, 4, 5],  # Designer
    [1, 4, 3, 2, 5],  # QA Engineer
    [2, 3, 4, 1, 5],  # DevOps
]

priority_order = ranked_pairs_voting(features, team_votes)
print("Feature Development Priority:")
for i, feature in enumerate(priority_order, 1):
    print(f"{i}. {feature}")
```

## Advanced Examples

### 4. Municipal Election Simulation

```python
import random
from rankedpairsvoting import ranked_pairs_voting

# Large-scale municipal election
candidates = [
    'Mayor Rodriguez',
    'Council Member Johnson', 
    'Former Mayor Kim',
    'Business Leader Thompson',
    'Community Activist Davis'
]

# Simulate 1000 voters with varying preferences
def simulate_votes(num_voters=1000):
    votes = []
    
    # Simulate different voter groups with different preferences
    for _ in range(num_voters):
        # Create a random preference ordering
        vote = list(range(1, len(candidates) + 1))
        random.shuffle(vote)
        
        # Sometimes add ties
        if random.random() < 0.1:  # 10% chance of ties
            tie_positions = random.sample(range(len(vote)), 2)
            vote[tie_positions[1]] = vote[tie_positions[0]]
            
        votes.append(vote)
    
    return votes

# Run election
voter_preferences = simulate_votes(1000)
election_result = ranked_pairs_voting(candidates, voter_preferences)

print("Municipal Election Results:")
print("=" * 40)
for i, candidate in enumerate(election_result, 1):
    print(f"{i}. {candidate}")
```

### 5. Conference Paper Selection

```python
# Academic conference selecting best papers
papers = [
    'ML in Healthcare',
    'Quantum Computing Advances',
    'Blockchain Applications',
    'AI Ethics Framework', 
    'Robotics in Manufacturing',
    'Climate Data Analysis'
]

# Review committee rankings (some reviewers might not rank all papers)
reviewer_scores = [
    [2, 1, 4, 3, 6, 5],  # Reviewer 1 (AI specialist)
    [1, 3, 5, 2, 4, 6],  # Reviewer 2 (Healthcare focus)
    [4, 1, 3, 5, 2, 6],  # Reviewer 3 (Hardware specialist)
    [3, 2, 4, 1, 5, 6],  # Reviewer 4 (Ethics specialist)
    [2, 4, 3, 5, 1, 6],  # Reviewer 5 (Industry focus)
]

paper_ranking = ranked_pairs_voting(papers, reviewer_scores)
print("Conference Paper Selection:")
print("Top 3 Selected Papers:")
for i, paper in enumerate(paper_ranking[:3], 1):
    print(f"{i}. {paper}")
```

### 6. Handling Condorcet Paradox

```python
# Example of Condorcet paradox (rock-paper-scissors preferences)
candidates = ['Rock', 'Paper', 'Scissors']

# Cyclical preferences: Rock > Scissors, Scissors > Paper, Paper > Rock
paradox_votes = [
    [1, 3, 2],  # Rock > Scissors > Paper
    [1, 3, 2],  # Rock > Scissors > Paper
    [1, 3, 2],  # Rock > Scissors > Paper
    [3, 2, 1],  # Scissors > Paper > Rock
    [3, 2, 1],  # Scissors > Paper > Rock
    [3, 2, 1],  # Scissors > Paper > Rock
    [2, 1, 3],  # Paper > Rock > Scissors
    [2, 1, 3],  # Paper > Rock > Scissors
    [2, 1, 3],  # Paper > Rock > Scissors
]

# Ranked Pairs resolves the paradox by margin strength
result = ranked_pairs_voting(candidates, paradox_votes)
print("Condorcet Paradox Resolution:", result)
```

## Performance Testing

### Large Election Benchmark

```python
import time
from rankedpairsvoting import ranked_pairs_voting

def benchmark_election(num_candidates, num_voters):
    """Benchmark election performance."""
    
    # Generate candidates
    candidates = [f"Candidate_{i}" for i in range(num_candidates)]
    
    # Generate random votes
    votes = []
    for _ in range(num_voters):
        vote = list(range(1, num_candidates + 1))
        random.shuffle(vote)
        votes.append(vote)
    
    # Time the election
    start_time = time.time()
    result = ranked_pairs_voting(candidates, votes)
    end_time = time.time()
    
    print(f"Election with {num_candidates} candidates and {num_voters} voters:")
    print(f"Winner: {result[0]}")
    print(f"Time taken: {end_time - start_time:.3f} seconds")
    print(f"Memory usage: ~{num_candidates**2 * 8} bytes for pairwise matrix")
    print("-" * 50)

# Run benchmarks
benchmark_election(5, 100)    # Small election
benchmark_election(10, 500)   # Medium election  
benchmark_election(20, 1000)  # Large election
```

## Error Handling Examples

### Input Validation

```python
from rankedpairsvoting import ranked_pairs_voting

# Example of proper error handling
def safe_election(candidates, votes):
    """Safely conduct an election with error handling."""
    
    try:
        # Validate inputs
        if not candidates:
            raise ValueError("Candidates list cannot be empty")
            
        if not votes:
            raise ValueError("Votes list cannot be empty")
            
        # Check vote format
        for i, vote in enumerate(votes):
            if len(vote) != len(candidates):
                raise ValueError(f"Vote {i} has wrong length: {len(vote)} != {len(candidates)}")
                
        # Conduct election
        result = ranked_pairs_voting(candidates, votes)
        return {"success": True, "result": result}
        
    except Exception as e:
        return {"success": False, "error": str(e)}

# Test error handling
test_cases = [
    ([], [[1, 2, 3]]),  # Empty candidates
    (['A', 'B'], []),   # Empty votes
    (['A', 'B'], [[1, 2, 3]]),  # Mismatched lengths
]

for candidates, votes in test_cases:
    result = safe_election(candidates, votes)
    if result["success"]:
        print(f"Success: {result['result']}")
    else:
        print(f"Error: {result['error']}")
```

## Integration Examples

### Web Application Integration

```python
# Example Flask web application endpoint
from flask import Flask, request, jsonify
from rankedpairsvoting import ranked_pairs_voting

app = Flask(__name__)

@app.route('/election', methods=['POST'])
def conduct_election():
    """API endpoint for conducting elections."""
    
    try:
        data = request.json
        candidates = data['candidates']
        votes = data['votes']
        
        # Conduct election
        result = ranked_pairs_voting(candidates, votes)
        
        return jsonify({
            'success': True,
            'winner': result[0],
            'full_ranking': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# Example usage:
# POST /election
# {
#   "candidates": ["Alice", "Bob", "Charlie"],
#   "votes": [[1, 2, 3], [2, 1, 3], [1, 3, 2]]
# }
```

### Database Integration

```python
import sqlite3
from rankedpairsvoting import ranked_pairs_voting

def conduct_stored_election(election_id):
    """Conduct election using data from database."""
    
    conn = sqlite3.connect('elections.db')
    cursor = conn.cursor()
    
    try:
        # Get candidates
        cursor.execute("""
            SELECT name FROM candidates 
            WHERE election_id = ? 
            ORDER BY candidate_id
        """, (election_id,))
        candidates = [row[0] for row in cursor.fetchall()]
        
        # Get votes
        cursor.execute("""
            SELECT vote_data FROM votes 
            WHERE election_id = ?
        """, (election_id,))
        votes = [eval(row[0]) for row in cursor.fetchall()]  # Note: Use proper JSON in production
        
        # Conduct election
        result = ranked_pairs_voting(candidates, votes)
        
        # Store results
        cursor.execute("""
            INSERT INTO election_results (election_id, winner, full_ranking)
            VALUES (?, ?, ?)
        """, (election_id, result[0], str(result)))
        
        conn.commit()
        return result
        
    finally:
        conn.close()
```

These examples demonstrate the versatility and practical applications of the Ranked Pairs Voting package across various domains and integration scenarios.
