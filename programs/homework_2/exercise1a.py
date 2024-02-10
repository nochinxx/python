import os
import sys
import math
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def read_exercise(exercise_file):
    # Define the path to the exercise file
    exercise_file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "exercises",
        "homework_2",
        "data",
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
    data = [row[0] for row in exercise_data[1:]]

    # Create a dictionary mapping from abbreviations to full names
    mapping = {}
    for item in data:
        if item not in mapping:
            user_input = input(f"Enter full name for '{item}': ")
            mapping[item] = user_input

    # Replace abbreviations with full names
    data = [mapping.get(item, item) for item in data]

    # Program functionalities:
    # Count the frequency for each class
    frequencies = {item: data.count(item) for item in data}
    total_data_points = len(data)

    # Calculate the relative frequency for each class as percentages
    relative_frequencies_percentage = {item: (freq / total_data_points) * 100 for item, freq in frequencies.items()}

    # Print frequency and relative frequency for each class
    print("{:<15} {:<10} {:<10}".format("Class", "Frequency", "Rel. Freq."))
    for item, freq in frequencies.items():
        rel_freq_percentage = relative_frequencies_percentage[item]
        print(f"{item:<15} {freq:<10} {rel_freq_percentage:<10.2f}%")

    # Get the exercise name
    exercise_name = get_exercise_name(exercise_file)

    # Export frequency table to a text file
    output_directory = os.path.join(
        os.path.dirname(__file__), "..", "..", "exercises", "homework_2"
    )
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = os.path.join(
        output_directory,
        "answers",
        f"{get_exercise_name(exercise_file)}_frequency_table.txt",
    )
    with open(output_file, "w") as f:
        f.write("{:<15} {:<10} {:<10}\n".format("Class", "Frequency", "Rel. Freq."))
        for item, freq in frequencies.items():
            rel_freq_percentage = relative_frequencies_percentage[item]
            f.write(f"{item:<15} {freq:<10} {rel_freq_percentage:<10.2f}%\n")

    print(f"Frequency table exported to '{output_file}'.")

    # Plotting the relative frequency histogram
    plt.figure(figsize=(10, 6))
    plt.bar(relative_frequencies_percentage.keys(), relative_frequencies_percentage.values(), align="center", alpha=0.7)
    plt.xlabel("Eye Color")
    plt.ylabel("Relative Frequency (%)")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))
    plt.title(header[0])
    plt.grid(True)
    plot_file_path = os.path.join(
        output_directory, "plots", f"{exercise_name}_relative_frequency_histogram.png"
    )
    plt.savefig(plot_file_path)
    print(f"Plot exported to '{plot_file_path}'.")


if __name__ == "__main__":
    main()
