from scipy.stats import binom

def calculate_binomial_probability(n, k, p):
    """
    Calculate the probability of exactly k successes in n trials with success probability p.

    Parameters:
    n (int): Number of trials
    k (int): Number of successes
    p (float): Probability of success in each trial

    Returns:
    float: Probability of exactly k successes
    """
    # Calculate the probability using binomial pmf
    probability = binom.pmf(k, n, p)
    return probability

# Example usage:
n = 1000  # total number of individuals
k = 10    # exact number of patients to have the event
p = 0.001 # probability of each individual dying due to breast cancer

# Calculate the probability
probability = calculate_binomial_probability(n, k, p)
print(f"The probability that exactly {k} out of {n} patients die of breast cancer is {probability:.4f}")
