import numpy as np

def calculate_pagerank(adjacecncy_matrix,num_iterations,d):
  num_nodes=adjacecncy_matrix.shape[0]

  page_rank=np.ones(num_nodes)/num_nodes
  print(f"ietation 0 :{np.round(page_rank,2)}")


  for iteration in range(num_iterations):
    new_pageramk=np.zeros(num_nodes)

    for i in range(num_nodes):
      incoming_rank=np.where(adjacecncy_matrix[:,i]>0)[0]
      incoming_rank=sum(
        (page_rank[j]/np.sum(adjacecncy_matrix[j]))*adjacecncy_matrix[j,i]
        for j in incoming_rank if np.sum(adjacecncy_matrix[j]>0)
      )

      new_pageramk[i]=(1-d)+d*incoming_rank

      new_pageramk[i]=np.floor(new_pageramk[i]*100)/100

      page_rank=new_pageramk
      print(f"PR({chr(65 + i)}) = (1 - {d}) + {d} * [{incoming_rank}]")

    page_rank=new_pageramk
    print(f"ieration {iteration+1}:{np.round(page_rank,2)}")

def main():
    # Input: number of nodes
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    # Input: adjacency matrix
    print("Enter the adjacency matrix row by row (use space to separate values):")
    adjacency_matrix = []
    for _ in range(num_nodes):
        row = list(map(float, input().split()))
        # Round down each input value to 2 decimal places
        #row = [np.floor(value * 100) / 100 for value in row]
        adjacency_matrix.append(row)
    
    adjacency_matrix = np.array(adjacency_matrix)

    # Input: number of iterations
    num_iterations = int(input("Enter the number of iterations: "))

    # Input: teleportation factor
    d = float(input("Enter the teleportation factor (0 < teleportation factor < 1): "))

    # Run PageRank algorithm
    calculate_pagerank(adjacency_matrix, num_iterations,d)

if __name__ == "__main__":
    main()
    
