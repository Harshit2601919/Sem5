import numpy as np
data=list(map(int,input("enter the number").split(" ")))
# Define a 9-element input array 
#data = np.array([11,2,13,4,25,26,7,18,9]) 
print("Input Array: \n", data) 

# Sort the array 
sorted_data = np.sort(data) 

bin_size = int(input("enter the size of bin")) 
num_bins = len(sorted_data) // bin_size 

# Create bins for mean, boundaries, and median 
bin_means = np.zeros(num_bins) 
bin_boundaries = np.zeros((num_bins,2))  # Just min and max boundaries
bin_medians = np.zeros(num_bins) 

# Print initial bins (subarrays) 
print("\nInitial Bins (Subarrays):")
for i in range(num_bins):
    bin_data = sorted_data[i * bin_size:(i + 1) * bin_size]
    print(f"Bin {i + 1}: {bin_data}")

    # Calculate bin mean, boundaries, and median
    bin_means[i] = np.mean(bin_data)
    bin_boundaries[i] = [bin_data[0], bin_data[-1]]
    bin_medians[i] = np.median(bin_data)

# Print results in the desired format
print("\nBin Mean: \n", bin_means.reshape(-1, 1))
print("\nBin Boundaries: \n", bin_boundaries)
print("\nBin Median: \n", bin_medians.reshape(-1, 1))