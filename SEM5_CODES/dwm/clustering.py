import numpy as np
import random

# Dataset points (X, Y)
points = np.array([
    [1,1],
    [2,1],
    [4,3],
    [5,4]
    
])

# Step 1: Randomly select k points as initial centroids
def initialize_centroids(points, k):
    return np.array(random.sample(list(points), k))

# Step 2: Assign each point to the nearest centroid
def assign_clusters(points, centroids):
    clusters = {}
    for i, point in enumerate(points):
        # Calculate the Euclidean distances from the point to each centroid
        distances = [np.linalg.norm(point - centroid) for centroid in centroids]
        
        # Display distances
        for j, distance in enumerate(distances):
            print(f"Distance to Centroid {j + 1} from Point ({point[0]}, {point[1]}) -> {distance:.2f}")
        
        # Find the index of the nearest centroid
        nearest_centroid = np.argmin(distances)
        print(f"Point ({point[0]}, {point[1]}) is assigned to Centroid {nearest_centroid + 1}\n")
        
        # Assign the point to the corresponding cluster
        clusters.setdefault(nearest_centroid, []).append(i)
    
    return clusters

# Step 3: Calculate new centroids as the mean of points in each cluster
def update_centroids(points, clusters):
    new_centroids = []
    for indices in clusters.values():
        cluster_points = points[indices]
        new_centroid = np.mean(cluster_points, axis=0)
        new_centroids.append(new_centroid)
    return np.array(new_centroids)

# Step 4: K-means algorithm
def kmeans(points, k, max_iterations=100):
    centroids = initialize_centroids(points, k)
    
    for iteration in range(max_iterations):
        print(f"\n--- Iteration {iteration + 1} ---")
        print("Current Centroids:\n", centroids)
        
        # Assign points to clusters
        clusters = assign_clusters(points, centroids)
        
        # Display clusters
        for cluster_id, indices in clusters.items():
            cluster_points = [points[i] for i in indices]
            print(f"Cluster {cluster_id + 1}: {cluster_points}")
        
        # Update centroids
        updated_centroids = update_centroids(points, clusters)
        print("\nUpdated Centroids:\n", updated_centroids)
        
        # Check if centroids have changed (convergence check)
        if np.array_equal(updated_centroids, centroids):
            print("\nCentroids have converged. K-means clustering is complete.")
            break
        centroids = updated_centroids
    
    return centroids, clusters

# Run the K-means algorithm with k=2 (for two clusters)
k = 2
final_centroids, final_clusters = kmeans(points, k)
