
import numpy as np

def page_rank(link_matrix, num_iterations=100, d=0.85):
    N = link_matrix.shape[0]
    M = link_matrix / np.sum(link_matrix, axis=0)
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)

    for i in range(num_iterations):
        v = d * np.matmul(M, v) + (1-d) / N
    return v

# Example usage
link_matrix = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
print("PageRank vector:", page_rank(link_matrix))
