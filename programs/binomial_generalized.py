from scipy.stats import binom

def calculate_probabilities(n, p, x):
    probabilities = {}
    # pmf gets the binomial prob
    # cdf sums
    probabilities['pmf'] = binom.pmf(int(x), n, p)
    probabilities['cdf'] = binom.cdf(int(x), n, p)

    return probabilities

def main():
    # Given data
    experiments = int(input("How many experiments you want to do?(1,2,3...) "))
    n = int(input("Enter the number of trials (people chosen): "))
    p = float(input("Enter the probability of success (in favor of building project): "))
    for i in range(experiments):
        x = input("To what number you need the binomial probability (Probability Mass Function pmf) and the Cumulative Distribution Function (cdf): ")
        # Calculate probabilities
        results = calculate_probabilities(n, p, x)

        # Print results
        print(results)
        
        # Prompt the user for different answers
        exactly = input("you need the probability for the event exactly happening for that value (y/n): ")
        exactly = float(0) if exactly == "n" else float(results['pmf'])
        lessThan = input("you need the probability for the event happening for less than the value (y/n): ")
        lessThan = float(0) if lessThan == "n" else float(binom.cdf(int(x) - 1, n, p))
        moreThan = input("you need the probability for the event happening for more than the value (y/n): ")
        moreThan = float(0) if moreThan == "n" else 1 - float(results['cdf'])
        atLeast = input("you need the probability for the event happening for at least the value (y/n): ") 
        atLeast = float(0) if atLeast == "n" else float(1 - binom.cdf(int(x) - 1, n, p))
        atMost = input("you need the probability for the event happening for atMost the value (y/n): ")
        atMost = float(0) if atMost == "n" else float(results['cdf'])
        
        
        print(f"Exactly: {round(exactly,4)} \nLessThan: {round(lessThan,4)} \nMoreThan: {round(moreThan,4)} \nAtLeast: {round(atLeast,4)}\nAtMost: {round(atMost,4)}\n")
        
    

if __name__ == "__main__":
    main()