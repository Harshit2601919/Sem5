import numpy as np

def page_rank(matrix, damping_factor, iterations):
    nodes = len(matrix)
    matrix = np.array(matrix, dtype=float)
    for i in range(nodes):
        temp = np.sum(matrix[i])
        matrix[i] /= temp
    r = np.ones(nodes) / nodes
    print(f"Normalized Matrix is : \n{matrix}\n")
    print(f"Initial Page Rank is : \n{r}\n")
    for i in range(iterations):
        r = (np.dot(matrix.T, r)) * damping_factor
        r = r + (np.ones(shape=r.shape) * ((1 - damping_factor)))
        print(f"Iteration: {i+1} :::: PR => {r}")
    return r

# Input example for testing
if __name__ == "__main__":
    # Input number of nodes
    n = int(input("Enter the number of nodes: "))
    
    # Input adjacency matrix from the user
    print(f"Enter the adjacency matrix row by row (1 if there is a link, 0 if not):")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split(" ")))
        matrix.append(row) 
    damping_factor = float(input("Enter the damping factor (e.g., 0.85): "))
    iterations = int(input("Enter the number of iterations: "))
    
    # Perform PageRank
    page_ranks = page_rank(matrix, damping_factor, iterations)
    print("\nFinal Page Ranks:", page_ranks)


    #optionallllllll
    for i in range(len(page_ranks)):
        print(f"Page Rank of Page {i+1} is : {round(page_ranks[i], 3)}")
