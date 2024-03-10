import os
import matplotlib.pyplot as plt
from scipy.stats import binom

def calculate_probabilities(n, p, x):
    """
    Calculate the binomial probabilities for a given number of trials, probability of success,
    and the desired number of successes.
    
    Parameters:
        n (int): Number of trials.
        p (float): Probability of success.
        x (int): Desired number of successes.
    
    Returns:
        dict: Dictionary containing the probabilities for the given values.
    """
    probabilities = {}
    # Calculate the Probability Mass Function (pmf) and the Cumulative Distribution Function (cdf)
    probabilities['pmf'] = binom.pmf(int(x), n, p)
    probabilities['cdf'] = binom.cdf(int(x), n, p)

    return probabilities

def main():
    # Given data
    n = int(input("Enter the number value of n: "))
    p = float(input("Enter the value of p: "))
    X_values = list(range(n + 1))  # List of possible values of X

    # Calculate probabilities for each X value
    probability_distribution = {x: calculate_probabilities(n, p, x) for x in X_values}

    # Print the probability distribution table
    print("X\tP(X)")
    for x in X_values:
        print(f"{x}\t{probability_distribution[x]['pmf']:.3f}")

    # Compute the mean
    mean = sum(x * probability_distribution[x]['pmf'] for x in X_values)
    print("\nThe mean is:", round(mean, 2))

    # Compute the standard deviation
    variance = sum((x - mean) ** 2 * probability_distribution[x]['pmf'] for x in X_values)
    std_dev = variance ** 0.5
    print("The standard deviation is:", round(std_dev, 2))

    # Plot histogram
    plt.bar(X_values, [probability_distribution[x]['pmf'] for x in X_values], edgecolor='black')
    plt.title('Probability Distribution of X')
    plt.xlabel('X')
    plt.ylabel('Probability')
    plt.grid(True)

    # Save plot
    output_directory = os.path.join(os.path.dirname(__file__), "..", "exercises", "probabilities")
    plot_file_path = os.path.join(output_directory, "plots", f"binomial_distribution_plot{round(n/p, 1)}.png")
    plt.savefig(plot_file_path)

if __name__ == "__main__":
    main()