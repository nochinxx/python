import os
import sys
import math

def calculate_chebyshev(pop_mean, pop_standard_deviation, percentage):
    if percentage == 75:
        return f"Lower Bound: {pop_mean-2*pop_standard_deviation} - Higher Bound: {pop_mean+2*pop_standard_deviation} at least 75%"
    elif percentage == 88.9:
        return f"Lower Bound: {pop_mean-3*pop_standard_deviation} - Higher Bound: {pop_mean+3*pop_standard_deviation} at least 88.9%"
    elif percentage == 93.8:
        return f"Lower Bound: {pop_mean-4*pop_standard_deviation} - Higher Bound: {pop_mean+4*pop_standard_deviation} at least 93.8%"
    else:
        return "Percentage needed in the argument of the function calculate_chebyshev(pop_mean, pop_standard_deviation, 'percentage')'"
    
def main():
    # Check if the exercise file name is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python your_program.py <mean> <deviation>")
        sys.exit(1)

    # Get the exercise file name from the command-line arguments
    mean = float(sys.argv[1])
    standard_deviation = float(sys.argv[2])
    
    print("Chebyshev 75%: \n", calculate_chebyshev(mean, standard_deviation, 75))
    print("Chebyshev 88.9%: \n", calculate_chebyshev(mean, standard_deviation, 88.9))
    print("Chebyshev 93.8%: \n", calculate_chebyshev(mean, standard_deviation, 93.8))
    
if __name__ == "__main__":
    main()
    