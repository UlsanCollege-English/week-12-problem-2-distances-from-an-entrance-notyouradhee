# hw02 – Distances from an Entrance with BFS

## Story

You are designing a guide system for an **art festival**.  
The festival has many stages connected by **walkways**. Every walkway takes about the same time to walk.

From the **main gate**, you want to know how many **steps (edges)** away each stage is.  
You will again model this as an **unweighted graph** and use **BFS**.

---

## Task

Write a function:

```
bfs_distances(graph, start)
```
- `graph`: dictionary `stage -> list of neighbouring stages`

- `start`: the starting stage name (string), usually `"Gate"`

## Return:

- A dictionary dist where:

    - `dist[start] == 0`
    
    - `dist[stage]` = minimum number of edges from `start` to `stage`

- Only include reachable stages in `dist`.

- If `start` is not in `graph`, return an empty dictionary `{}`.

## Constraints

- At most 200 stages (nodes).

- All walkways are unweighted (same cost).

- Use BFS from a single source.

- Expected time complexity: O(V + E).
- 
---

## 8 Steps of Coding – Scaffold (hw02)

Use these steps in your comments.

1. Read & Understand

    - Write 1–2 sentences about what the function should compute.

1. Re-phrase

    - Simple English example:

        - “Find the smallest number of walkways from the gate to every reachable stage.”

1. Identify Input / Output / Variables

    - Inputs: `graph`, `start`

    - Output: `dist` dictionary

    - Data structures: `queue`, `visited`, `dist`
1. Break Down the Problem

    - Plan the BFS wave from start.

    - How do you update distance for each neighbor?

1. Pseudocode

    - Write clear pseudocode in comments:

        - Initialize `dist[start] = 0`

        - BFS loop; for each neighbor not visited, set `dist[neighbor] = dist[current] + 1`

1. Write the Code (Hint)

        - Turn your pseudocode into Python.

1. Debug (Hint)

    - Test with simple graphs:

        - Line shape, star shape, disconnected nodes.

1. Optimize (Hint)

    - Check you visit each node/edge only a small number of times.

---
## Hints
1. You do not need a parent dictionary here, only dist.

1. Remember to enqueue neighbors when you first discover them.

1. Use integers for distances; no need for float("inf").

---
How to Run Tests
```
python -m pytest -q

```
---
## FAQ
Q1: What if some stages are not reachable from `start`?
A1: Do not include them in `dist`. Only reachable stages appear.

Q2: Should I modify the input graph?
A2: No. Treat `graph` as read-only.

Q3: What Big-O time is expected here?
A3: O(V + E), same as hw01, because we still use BFS.

Q4: What if `start` is not a key in `graph`?
A4: Return an empty dictionary `{}`.

Q5: Can I assume the graph is undirected?
A5: In tests, edges are given both ways when the walkway is two-way. Your code should not assume this; just follow adjacency lists.

Q6: How do I debug wrong distances?
A6: Print `current`, ` neighbor`, and `dist[current]`, especially when you assign a new distance.

Q7: How is grading done?
A7: Same as hw01: test passing, correct BFS idea, and use of the 8 Steps scaffold.