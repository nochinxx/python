from scipy.stats import norm

def calculate_probabilities_normal(mu, sigma, x):
    probabilities = {}
    probabilities['cdf'] = norm.cdf(x, mu, sigma)
    probabilities['lessThan'] = probabilities['cdf']
    probabilities['moreThan'] = 1 - probabilities['cdf']
    probabilities['exactly'] = 0  # Since we're dealing with a continuous distribution, probability of exact value is zero
    probabilities['atLeast'] = probabilities['moreThan']
    probabilities['atMost'] = probabilities['cdf']
    return probabilities

def calculate_value_from_percentage(mu, sigma, percentage):
    x = norm.ppf(percentage, mu, sigma)
    return x

def main():
    # Given data
    experiments = int(input("How many experiments you want to do? (1, 2, 3, ...): "))
    mu = float(input("Enter the mean: "))
    sigma = float(input("Enter the standard deviation: "))
    for i in range(experiments):
        print(f"\nExperiment {i}_____________________\n")
        x = float(input("Enter the value for which you need the cumulative distribution function (CDF): "))
        # Calculate probabilities
        results = calculate_probabilities_normal(mu, sigma, x)
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

    # Calculate between a range
    response = input("\nYou need the value in a range y/n? ")
    if (response == "y"):
        value1 = float(input("Input the first value for the range: "))
        value2 = float(input("Input the second value for the range: "))
        dif = abs(value1 - value2)
        print(f"Range: {dif}\n")
    
    
    # Calculate value from percentage
    percentage = float(input("Enter the percentage for which you need the value: "))/100
    if percentage == 0:
        print("Goodbye")
    else:
        value = calculate_value_from_percentage(mu, sigma, percentage)
        print(f"The value for below which {percentage*100}%  fall is approximately {value:.2f} ")
        value = calculate_value_from_percentage(mu, sigma, 1- percentage)
        print(f"The value for more than which {percentage*100}%  fall is approximately {value:.2f} ")
        

if __name__ == "__main__":
    main()