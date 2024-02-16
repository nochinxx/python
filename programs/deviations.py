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
        "Module_3",
        "3.2",
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
        os.path.dirname(__file__), "..", "exercises", "Module_3", "3.2", "answers"
    )
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = os.path.join(
        output_directory,
        f"{get_exercise_name(exercise_file)}_frequency_table.txt",
    )

    # Mode, Mean, and Median
    # Calculate mode, median, and mean
    mode = calculate_mode(data)
    median = calculate_median(data)
    mean = calculate_mean(data)
    range_data = calculate_range(data)
    variance = calculate_variance(data, mean)
    population_variance = calculate_population_variance(data, mean)
    standard_deviation = calculate_standard_dev(variance)
    population_standard_deviation = calculate_pop_standard_dev(population_variance)

    # Print mode, median, and mean
    print("Mode:", mode)
    print("Median:", median)
    print("Mean:", mean)
    print("Range: ", range_data)
    print("Variance:", variance)
    print("Standard Deviation:", standard_deviation)
    print("Population Variance:", population_variance)
    print("Population Standard Deviation:", population_standard_deviation)
    print("Chebyshev 75%: \n", calculate_chebyshev(mean, standard_deviation, 75))
    print("Chebyshev 88.9%: \n", calculate_chebyshev(mean, standard_deviation, 88.9))
    print("Chebyshev 93.8%: \n", calculate_chebyshev(mean, standard_deviation, 93.8))

    # Write mode, median, and mean to the output file with an extra space
    with open(output_file, "a") as f:
        #    f.write(f"Mode: {mode}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Mean: {mean}\n")
        f.write(f"Range: {range_data}\n")
        f.write(f"Variance: {variance}\n")
        f.write(f"Standard Deviation: {standard_deviation}\n")
        f.write(f"Population Variance: {population_variance}\n")
        f.write(f"Population Standard Deviation: {population_standard_deviation}\n")
        f.write(f"Chebyshev 75%: \n {calculate_chebyshev(mean, standard_deviation, 75)}\n")
        f.write(f"Chebyshev 88.9%: \n {calculate_chebyshev(mean, standard_deviation, 88.9)}\n")
        f.write(f"Chebyshev 93.8%: \n {calculate_chebyshev(mean, standard_deviation, 93.8)}\n")

    # Calculate frequencies and x positions
    frequencies = []
    x_positions = sorted(set(data))
    for x in x_positions:
        frequencies.append(data.count(x))

    plt.figure(figsize=(10, 6))

    # Plot data points
    plt.plot(x_positions, frequencies, marker="o", linestyle="-")

    # Annotate mode, median, and mean on the plot
    plt.annotate(
        f"Mode: {mode}",
        xy=(mode, 0),
        xytext=(mode, max(frequencies) // 2),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )
    plt.annotate(
        f"Median: {median}",
        xy=(median, 0),
        xytext=(median, max(frequencies) // 2),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )
    plt.annotate(
        f"Mean: {mean:.2f}",
        xy=(mean, 0),
        xytext=(mean, max(frequencies) // 2),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )

    # Labeling plot
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title(header[0])

    # Adjust margins to accommodate labels and call tight_layout to automatically adjust subplot parameters
    plt.margins(x=0.05)
    plt.tight_layout()

    # Save plot
    plot_file_path = os.path.join(output_directory, "plots", f"{exercise_name}.png")
    plt.savefig(plot_file_path)


if __name__ == "__main__":
    main()
