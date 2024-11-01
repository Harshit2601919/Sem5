import numpy as np
import random

points=np.array([

  [2,3],
  [3,4],
  [6,8],
  [8,8],
  [9,10]
])
def initialize_centroid(points,k):
  return np.array(random.sample(list(points),k))


def assign_cluster(points,centroids):
  clusters={}
  for i,point in enumerate(points):
    distances=[np.linalg.norm(points-centroid)for centroid in centroids ]

    for j,distance in enumerate(distances):
      print(f"distnace to centorid {j+1} from points ({point[0]},{point[1]}) = {distance:.2f}")

    nearest_centroid=np.argmin(distances)
    print(f"point ({point[0]},{point[1]}) is assigned to centroid {nearest_centroid+1}")

    clusters.setdefault(nearest_centroid,[]).append(i)
  return clusters


def update_centroids(points,clusters):
  new_centroids=[]
  for indices in clusters.values():
    clusters_points=points[indices]
    new_centroid=np.mean(clusters_points,axis=0)
    new_centroids.append(new_centroid)
  return np.array(new_centroids)
    
    

      

      







def kmeans(points,k,max_iteration=100):
  centroids=initialize_centroid(points,k)


  for iteration in range(max_iteration):
    print(f"------iteraion : {iteration+1}----")
    print(f"current centoids",centroids)

    clusters=assign_cluster(points,centroids)

    for cluster_id,indices in clusters.items():
      cluster_points=[points[i]for i in indices]
      print(f"cluster {cluster_id+1} :{cluster_points}")

    updated_centroids=update_centroids(points,clusters)
    print(f"updated centroids",updated_centroids)

    if np.array_equal(updated_centroids,centroids):
      print("cannot be merged")
      break
    centroids=updated_centroids
  return centroids,clusters
k=2
final_centroids,final_clusters=kmeans(points,k)

