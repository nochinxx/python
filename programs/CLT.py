import math
from scipy.stats import norm

def calculate_probabilities_normal_CLT(mu, sigma, x):
    probabilities = {}
    probabilities['cdf'] = norm.cdf(x, mu, sigma)
    probabilities['lessThan'] = probabilities['cdf']
    probabilities['moreThan'] = 1 - probabilities['cdf']
    probabilities['exactly'] = 0  # Since we're dealing with a continuous distribution, probability of exact value is zero
    probabilities['atLeast'] = probabilities['moreThan']
    probabilities['atMost'] = probabilities['cdf']
    return probabilities

def calculate_value_from_percentage_CLT(mu, sigma, percentage):
    x = norm.ppf(percentage, mu, sigma)
    return x

def calculate_sampling_distribution(n):
    # Calculate mean of the sampling distribution of the sample mean
    mean_sampling_distribution = mu

    # Calculate standard deviation of the sampling distribution of the sample mean
    sigma_sampling_distribution = sigma / math.sqrt(n)

    return mean_sampling_distribution, sigma_sampling_distribution


# input data
mu = float(input("Input the mean: "))  # Mean
sigma = float(input("Input the stamdard deviation: "))  # Standard deviation


def main():
    # Sample sizes
    samples=int(input("How many samples you need? (1,2,3,4...): "))
    sample_sizes =[]
    for i in range(samples):
        sample_sizes.append(int(input(f"Size {i + 1}: ")))

    for n in sample_sizes:
        # Calculate sampling distribution
        mean, std_dev = calculate_sampling_distribution(n)

        # Print results
        print(f"For a sample of size {n}:")
        print(f"Mean of the sampling distribution of the sample mean: {mean}")
        print(f"Standard deviation of the sampling distribution of the sample mean: {std_dev:.2f}\n")
        
        response = input("You need probabilities fro this size? (y/n): ")
        
        if response == "y":
            experiments = int(input("How many experiments you want to do? (1, 2, 3, ...): "))
            for i in range(experiments):
                print(f"\nExperiment {i}_____________________\n")
                x = float(input("Enter the value for which you need the cumulative distribution function (CDF): "))
                # Calculate probabilities
                results = calculate_probabilities_normal_CLT(mu, std_dev, x)
                # Prompt the user for different answers
                lessThan =  results['lessThan']
                moreThan =  results['moreThan']
                exactly =  results['exactly']
                atLeast =  results['atLeast']
                atMost =  results['atMost']
                print(f"LessThan: {round(lessThan, 4)}")
                print(f"MoreThan: {round(moreThan, 4)}")
                print(f"Exactly: {round(exactly, 4)}")
                print(f"AtLeast: {round(atLeast, 4)}")
                print(f"AtMost: {round(atMost, 4)}")
            

if __name__ == "__main__":
    main()