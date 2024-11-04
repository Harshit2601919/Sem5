import statistics

# Input for the number of bins
bin_count = int(input("Enter the Number of Bins: "))

# Input for the length of the array
count = int(input(f"Enter the length of the array in the multiple of {bin_count} value: "))
print(count)

arr = []
binarr = []

# Input for the elements in the array
print("Enter the elements in ARRAY:")
for i in range(count):
    arr.append(int(input()))

# Sort the array
arr.sort()
counter = 0

# Creating bins based on the specified number of bins
for i in range(bin_count):
    innerlist = []
    while counter < (i + 1) * int(count / bin_count):
        innerlist.append(arr[counter])
        counter += 1
    binarr.append(innerlist)

# Calculate statistics for each bin
for i in binarr:
    bin1 = []  # For mean smoothing
    bin2 = []  # For median smoothing
    bin3 = []  # For boundary smoothing

    # Calculate mean
    mean_result = statistics.mean(i)
    for k in range(int(count / bin_count)):
        bin1.append(mean_result)

    # Calculate median
    median_result = statistics.median(i)
    for j in range(int(count / bin_count)):
        bin2.append(median_result)

    # Determine boundaries
    for j in range(0, int(count / bin_count)):
        if abs(i[j] - i[0]) < abs(i[j] - i[int(count / bin_count) - 1]):
            bin3.append(i[0])
        else:
            bin3.append(i[int(count / bin_count) - 1])

    # Print results for the current bin
    print("Bin:", binarr.index(i) + 1, i)
    print("Data Smoothing by Bin Mean:", bin1)
    print("Data Smoothing by Bin Median:", bin2)
    print("Data Smoothing by Bin Boundaries:", bin3)

    # Clear temporary lists for next iteration
    bin1.clear()
    bin2.clear()
