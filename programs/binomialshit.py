from scipy.stats import binom

def main():
    # Given data
    n = int(input("Enter the number of trials (people chosen): "))
    p = float(input("Enter the probability of success (in favor of building project): "))
    
    # pmf gets the binomial prob
    # cdf sums

    # d) Probability that exactly 61 of them are in favor
    x_1 = input("Probability that exactly x of them are in favor (x): ")
    prob_exactly_61 = binom.pmf(int(x_1), n, p)

    # e) Probability that less than 61 of them are in favor
    x_2 = input("Probability that less than x of them are in favor (x): ")
    prob_less_than_61 = binom.cdf(int(x_2)-1, n, p)

    # f) Probability that more than 61 of them are in favor
    x_3 = input("Probability that more than x of them are in favor (x): ")
    prob_more_than_61 = 1 - binom.cdf(int(x_3), n, p)

    # g) Probability that exactly 67 of them are in favor
    x_4 = input("Probability that exactly x of them are in favor: ")
    prob_exactly_67 = binom.pmf(int(x_4), n, p)

    # h) Probability that at least 67 of them are in favor
    x_5 = input("Probability that less than x of them are in favor (x): ")
    prob_at_least_67 = 1 - binom.cdf(int(x_5)-1, n, p)

    # i) Probability that at most 67 of them are in favor
    x_6 = input("Probability that at most x of them are in favor ")
    prob_at_most_67 = binom.cdf(int(x_6), n, p)

    # Print results
    print("Probability that exactly 61 of them are in favor:", round(prob_exactly_61, 4))
    print("Probability that less than 61 of them are in favor:", round(prob_less_than_61, 4))
    print("Probability that more than 61 of them are in favor:", round(prob_more_than_61, 5))
    print("Probability that exactly 67 of them are in favor:", round(prob_exactly_67, 4))
    print("Probability that at least 67 of them are in favor:", round(prob_at_least_67, 4))
    print("Probability that at most 67 of them are in favor:", round(prob_at_most_67, 4))
    
if __name__ == "__main__":
    main()