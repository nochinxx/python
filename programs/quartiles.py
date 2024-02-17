import csv
import os
import sys
import math
import matplotlib.pyplot as plt


def read_exercise(exercise_file):
    # Define the path to the exercise file
    exercise_file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "exercises",
        "homework_3",
        exercise_file,
    )

    # Check if the exercise file exists
    if not os.path.exists(exercise_file_path):
        print(f"Error: Exercise file '{exercise_file}' not found.")
        sys.exit(1)

    # Open the exercise file for reading
    with open(exercise_file_path, "r") as file:
        # Read the contents of the exercise file
        exercise_data = list(csv.reader(file))

    return exercise_data


def get_exercise_name(exercise_file):
    # Extract the exercise name from the file name
    exercise_name = os.path.splitext(exercise_file)[0]
    return exercise_name


def calculate_mode(data):
    # Calculate the mode
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    mode = max(frequency, key=frequency.get)
    return mode


def calculate_median(data):
    # Calculate the median
    sorted_data = sorted(data)
    n = len(sorted_data)
    median = (
        sorted_data[n // 2]
        if n % 2 != 0
        else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    )
    return median


def calculate_mean(data):
    # Calculate the mean
    mean = sum(data) / len(data)
    return mean


def calculate_range(data):
    range = max(data) - min(data)
    return range


def calculate_variance(data, mean):
    variance = 0
    for value in data:
        variance = variance + (value - mean) ** 2
    n = len(data)
    variance = variance / (n - 1)
    return variance


def calculate_standard_dev(variance):
    return math.sqrt(variance)


def calculate_population_variance(data, population_mean):
    pop_variance = 0
    for value in data:
        pop_variance = pop_variance + (value - population_mean) ** 2
    N = len(data)
    pop_variance = pop_variance / (N)
    return pop_variance


def calculate_pop_standard_dev(population_variance):
    return math.sqrt(population_variance)


def calculate_quartiles(data):
    # Sort the data in ascending order
    sorted_data = sorted(data)

    # Calculate the minimum
    minimum = min(sorted_data)
    maximum = max(sorted_data)

    # Calculate the median (Q2)
    n = len(sorted_data)
    median = calculate_median(sorted_data)

    # Calculate the index of the median
    median_index = n // 2

    # If the number of data points is odd, exclude the median
    if n % 2 != 0:
        lower_half = sorted_data[:median_index]
        upper_half = sorted_data[median_index + 1 :]
    else:
        lower_half = sorted_data[:median_index]
        upper_half = sorted_data[median_index:]

    # Calculate the first quartile (Q1)
    q1 = calculate_median(lower_half)

    # Calculate the third quartile (Q3)
    q3 = calculate_median(upper_half)

    # Calculate interquartile range
    iqr = q3 - q1

    # Calculate the probable outliers
    low_fence = q1 - (1.5) * iqr
    high_fence = q3 + (1.5) * iqr

    return minimum, q1, median, q3, maximum, iqr, low_fence, high_fence


def main():
    # Check if the exercise file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python your_program.py <exercise_file>")
        sys.exit(1)

    # Get the exercise file name from the command-line arguments
    exercise_file = sys.argv[1]

    # Read the exercise file
    exercise_data = read_exercise(exercise_file)

    # Extract header and data separately
    header = exercise_data[0]
    data = [float(row[0]) for row in exercise_data[1:]]

    # Get the exercise name
    exercise_name = get_exercise_name(exercise_file)

    # Export frequency table to a text file
    output_directory = os.path.join(
        os.path.dirname(__file__), "..", "exercises", "homework_3", "answers"
    )
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = os.path.join(
        output_directory,
        f"{get_exercise_name(exercise_file)}_quartiles.txt",
    )

    # Calculate quartiles
    minimum, q1, median, q3, maximum, iqr, low_fence, high_fence = calculate_quartiles(
        data
    )

    # Print quartile values
    print("Minimum:", minimum)
    print("Q1:", q1)
    print("Median:", median)
    print("Q3:", q3)
    print("Maximum:", maximum)
    print("Interquartile Range (IQR):", iqr)
    print("Low Fence:", low_fence)
    print("High Fence:", high_fence)

    # Write quartile values to the output file with an extra space
    with open(output_file, "a") as f:
        f.write(f"Minimum: {minimum}\n")
        f.write(f"Q1: {q1}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Q3: {q3}\n")
        f.write(f"Maximum: {maximum}\n")
        f.write(f"Interquartile Range (IQR): {iqr}\n")
        f.write(f"Low Fence: {low_fence}\n")
        f.write(f"High Fence: {high_fence}\n")

    # Create box plot
    plt.figure(figsize=(8, 6))
    plt.boxplot(data, vert=False, patch_artist=True, showfliers=False)
    plt.title(header[0])
    plt.xlabel("Values")
    plt.grid(axis='x')
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    boxplot_file_path = os.path.join(
        output_directory, "plots", f"{exercise_name}_boxplot_test.png"
    )
    plt.savefig(boxplot_file_path)


if __name__ == "__main__":
    main()
