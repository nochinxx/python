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
    data = [int(row[0]) for row in exercise_data[1:]]

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
        f"{get_exercise_name(exercise_file)}_mmm_table.txt",
    )

    # Mode, Mean, and Median
    # Calculate mode, median, and mean
    mode = calculate_mode(data)
    median = calculate_median(data)
    mean = calculate_mean(data)

    # Print mode, median, and mean
    print("Mode:", mode)
    print("Median:", median)
    print("Mean:", mean)

    # Write mode, median, and mean to the output file with an extra space
    with open(output_file, "a") as f:
        f.write("\n")  # Add a new line before printing mode, median, and mean
        f.write(f"Mode: {mode}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Mean: {mean}\n")

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
