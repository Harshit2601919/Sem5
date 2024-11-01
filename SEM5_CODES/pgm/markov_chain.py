import numpy as np

# yeah function matrix multipy karne ke liyaaa
def matrix_power_manual(matrix, power):
    result = matrix  
    for _ in range(1, power):  
        result = result @ matrix  
    return result


transition_matrix = np.array([
    [0.7, 0.2, 0.1],
    [0.5, 0.1, 0.4],
    [0.6, 0.2, 0.2]
])

#  initial probabilities
initial_probabilities = np.array([0.6, 0.3, 0.1])

def main():
    
    probabilities_over_days = [initial_probabilities]
    for _ in range(10):
        next_day_prob = probabilities_over_days[-1] @ transition_matrix
        probabilities_over_days.append(next_day_prob)
    
    print("\nPurchase probabilities over the next 10 days:")
    for i, probs in enumerate(probabilities_over_days):
        print(f"Day {i}: A = {probs[0]:}, B = {probs[1]:}, C = {probs[2]:}")



    # 2. 
    transition_prob_matrix_3 = matrix_power_manual(transition_matrix, 3)
    prob_B_to_A_in_3_months = transition_prob_matrix_3[1, 0]
    
    print(f"\nProbability of transitioning from cereal B to cereal A in 3 months: {prob_B_to_A_in_3_months:.4f}")



    # 3.
    final_transition_matrix_4 = matrix_power_manual(transition_matrix, 4)
    final_probabilities_4_months = initial_probabilities @ final_transition_matrix_4
    
    print("\nOverall probabilities of buying each cereal after 4 months:")
    print(f"A = {final_probabilities_4_months[0]:.4f}, B = {final_probabilities_4_months[1]:.4f}, C = {final_probabilities_4_months[2]:.4f}")

if __name__ == "__main__":
    main()
