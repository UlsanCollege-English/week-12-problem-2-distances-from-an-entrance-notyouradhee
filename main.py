from collections import deque


def bfs_distances(graph, start):
    """
    Compute shortest distances (in edges) from start to all reachable nodes
    in an unweighted graph.

    graph: dict mapping stage name (string) to list of neighbor stage names.
    start: starting stage name (string).

    Return value:
        - A dict dist where dist[node] is the minimum number of edges
          from start to node.
        - dist[start] should be 0.
        - Only include reachable nodes.
        - If start is not in graph, return {}.
    """
    # TODO Step 1: Read and understand the problem above.
    # TODO Step 2: Re-phrase what this function should do in a short comment.
    # TODO Step 3: Identify inputs, output, and key variables (queue, visited, dist).
    # TODO Step 4: Plan the BFS steps on paper or in comments.
    # TODO Step 5: Write pseudocode for BFS that fills the dist dictionary.
    # TODO Step 6: Turn your pseudocode into working Python code here.
    # TODO Step 7: Test using small graph examples to verify the distances.
    # TODO Step 8: Make sure your solution is O(V + E), not slower.

    if start not in graph:
        return {}
    
    dist = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        current_dist = dist[current]
        
        for neighbor in graph[current]:
            if neighbor not in dist:
                dist[neighbor] = current_dist + 1
                queue.append(neighbor)
    
    return dist


if __name__ == "__main__":
    # Optional simple check
    sample_graph = {
        "Gate": ["Stage1", "Stage2"],
        "Stage1": ["Gate", "Stage3"],
        "Stage2": ["Gate"],
        "Stage3": ["Stage1"],
    }
    d = bfs_distances(sample_graph, "Gate")
    print("Distances from Gate:", d)
