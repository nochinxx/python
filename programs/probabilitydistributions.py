import csv
import os
import sys
import matplotlib.pyplot as plt
from toCsv import read_data_from_file

# Read data from CSV file
def read_data(filename):
    
    # Define the path to the exercise file
    exercise_file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "exercises",
        "probabilities",
        filename,
    )

    # Check if the exercise file exists
    if not os.path.exists(exercise_file_path):
        print(f"Error: Exercise file '{filename}' not found.")
        sys.exit(1)
        
    days = []
    probabilities = []
    reader = read_data_from_file(exercise_file_path)
    for row in reader:
        try:
            # If it fails, try converting to float
            float(row[0])
        except ValueError:
            # If both fail, skip this row
            continue
        days.append(int(row[0]))
        probabilities.append(float(row[1]))
    return days, probabilities

# Calculate mean
def calculate_mean(days, probabilities):
    mean = sum(days[i] * probabilities[i] for i in range(len(days)))
    return mean

# Calculate standard deviation
def calculate_std_dev(days, probabilities, mean):
    variance = sum(probabilities[i] * (days[i] - mean)**2 for i in range(len(days)))
    std_dev = variance ** 0.5
    return std_dev

# Main function
def main():
    
    # Check if the exercise file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python your_program.py <exercise_file>")
        sys.exit(1)

    # Get the exercise file name from the command-line arguments
    exercise_file = sys.argv[1]

    # Read the exercise file
    days, probabilities = read_data(exercise_file)

    # Calculate mean
    mean = calculate_mean(days, probabilities)
    print("Mean number of days to fix defects:", round(mean, 3))

    # Calculate standard deviation
    std_dev = calculate_std_dev(days, probabilities, mean)
    print("Standard deviation of number of days to fix defects:", round(std_dev, 3))

    output_directory = os.path.join(
        os.path.dirname(__file__), "..", "exercises", "probabilities",
    ) 
    
    # Plot histogram
    plt.hist(days, bins=10, weights=probabilities, edgecolor='black')
    plt.title('Histogram of Days to Fix Defects')
    plt.xlabel('Days')
    plt.ylabel('Probability')
    plt.grid(True)
    # Save plot
    plot_file_path = os.path.join(output_directory, "plots", f"{exercise_file}_histogram.png")
    plt.savefig(plot_file_path)

if __name__ == "__main__":
    main()
