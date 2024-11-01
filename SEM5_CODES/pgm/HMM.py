import numpy as np

# Define the states and parameters
states = ["rainy", "sunny"]
hidden_states = ["walk", "shop", "clean"]

start_probability = [0.6, 0.4]
tsm = [
    [0.7, 0.3],  # Transition probabilities from rainy and sunny to rainy and sunny
    [0.4, 0.6],
]

tsm = np.array(tsm).astype(np.float32)# convert karta hai tsm ko numpy array meh

epm = [
    [0.1, 0.4, 0.5],  # Emission probabilities for rainy
    [0.6, 0.3, 0.1],  # Emission probabilities for sunny
]

def forward_algorithm(obs_sequence):
    n_states = len(states)
    n_observations = len(obs_sequence)

    # Initialize the temporary variable for alpha values
    alpha = np.zeros(n_states, dtype=np.float64)

    # First observation
    for i in range(n_states):
        alpha[i] = start_probability[i] * epm[i][hidden_states.index(obs_sequence[0])]

    # Print the alpha values for the first observation
    print("Alpha values for the first observation:", alpha)

    # Iterate over the rest of the observations
    for t in range(1, n_observations):
        new_alpha = np.zeros(n_states, dtype=np.float64)
        for j in range(n_states):
            new_alpha[j] = (alpha.dot(tsm[:, j])) * epm[j][hidden_states.index(obs_sequence[t])]
        
        # Update alpha for the next iteration
        alpha = new_alpha

        # Print the alpha values for the current observation
        print(f"Alpha values for observation {t+1} ({obs_sequence[t]}):", alpha)

    overall_probability = sum(alpha)
    print("Overall probability:", overall_probability)

    return alpha, overall_probability
  
# Example usage
forward_algorithm(["shop", "clean", "walk"])
print()

def viterbi(obs_sequence):
    n_states = len(states)
    n_observations = len(obs_sequence)

    # Initialize the best path
    best_sequence = []
    
    # Initialize the temporary variable for alpha values
    delta = np.zeros(n_states, dtype=np.float64)

    # First observation
    for i in range(n_states):
        delta[i] = start_probability[i] * epm[i][hidden_states.index(obs_sequence[0])]
    
    best_sequence.append(states[np.argmax(delta)]) #JO SABSE  NUMBER HAI USKA INDEX DETA HAI
    print("Alpha values for the first observation:", delta)
 
    # Iterate over the rest of the observations
    for t in range(1, n_observations):
        new_delta = np.zeros(n_states, dtype=np.float64)
        for j in range(n_states): 
            max_prob = max(delta[i] * tsm[i, j] for i in range(n_states))  # max probablity  deta hai 
            new_delta[j] = max_prob * epm[j][hidden_states.index(obs_sequence[t])]

        # Update alpha for the next iteration
        delta = new_delta
        best_sequence.append(states[np.argmax(delta)])
        print(f"Alpha values for observation {t+1} ({obs_sequence[t]}):", delta)

    print("Best sequence:", best_sequence)
    return best_sequence

# Example usage for Viterbi
sequence = viterbi(["shop", "clean", "walk"])