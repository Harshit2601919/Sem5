import csv

# Initialize variables
data = {}
params = []
input_file = csv.DictReader(open("data.csv"))
total = 0

print("Dataset given:")
for row in input_file:
    print(row)
    total += 1
    if row["stolen"] not in params:
        params.append(row['stolen'])

print(f"Total rows in dataset: {total}\n")

# Analyze each parameter
for param in params:
    count_param = 0
    count_color = 0
    count_type = 0
    count_origin = 0

    # Reset the input file reader to read it again
    input_file = csv.DictReader(open("data.csv"))
    
    for row in input_file:
        if row["stolen"] == param:
            count_param += 1
            if row["color"] == "Red":
                count_color += 1
            if row["type"] == "SUV":
                count_type += 1
            if row["origin"] == "Domestic":
                count_origin += 1

    # Calculate probabilities
    if count_param > 0:  # Avoid division by zero
        p_param = count_param / total
        p_color_given_param = count_color / count_param if count_param > 0 else 0
        p_type_given_param = count_type / count_param if count_param > 0 else 0
        p_origin_given_param = count_origin / count_param if count_param > 0 else 0

        print(f"P(\"{param}\") = {p_param:.2f} \n"
              f"P(\"Red\" | \"{param}\") = {p_color_given_param:.2f} \n"
              f"P(\"SUV\" | \"{param}\") = {p_type_given_param:.2f} \n"
              f"P(\"Domestic\" | \"{param}\") = {p_origin_given_param:.2f}")

        bayes = (p_param * p_color_given_param * 
                 p_type_given_param * p_origin_given_param)

        print(f"P(\"Red\", \"SUV\", \"Domestic\" | \"{param}\") = {bayes:.4f}\n")
