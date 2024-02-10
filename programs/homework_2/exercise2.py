import os
import sys
import math
import csv
import matplotlib.pyplot as plt


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
    data = [int(row[0]) for row in exercise_data[1:]]

    # Program functionalities:
    # Max and Min:
    max_val = max(data)
    min_val = min(data)
    print("Maximum value:", max_val)
    print("Minimum value:", min_val)

    # Create single value classes
    class_limits = sorted(set(data))

    # Count the frequency for each class
    frequencies = [data.count(value) for value in class_limits]
    total_data_points = len(data)

    # Calculate the relative frequency for each class
    relative_frequencies = [freq / total_data_points for freq in frequencies]

    # Calculate the cumulative frequency
    cumulative_frequencies = [
        sum(relative_frequencies[: i + 1]) for i in range(len(relative_frequencies))
    ]

    # Print frequency, relative frequency, and cumulative frequency for each class
    print(
        "{:<10} {:<10} {:<10} {:<10}".format(
            "Class", "Frequency", "Rel. Freq.", "Cum. Freq."
        )
    )
    for class_val, freq, rel_freq, cum_freq in zip(
        class_limits, frequencies, relative_frequencies, cumulative_frequencies
    ):
        print(f"{class_val:<10} {freq:<10} {rel_freq:<10.2f} {cum_freq:<10.2f}")

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
        f.write(
            "{:<10} {:<10} {:<10} {:<10}\n".format(
                "Class", "Frequency", "Rel. Freq.", "Cum. Freq."
            )
        )
        for class_val, freq, rel_freq, cum_freq in zip(
            class_limits, frequencies, relative_frequencies, cumulative_frequencies
        ):
            f.write(f"{class_val:<10} {freq:<10} {rel_freq:<10.2f} {cum_freq:<10.2f}\n")

    print(f"Frequency table exported to '{output_file}'.")

    # Plotting the frequency histogram
    plt.figure(figsize=(10, 6))
    plt.bar(class_limits, frequencies, align="center", alpha=0.7)
    plt.xlabel("Number of Siblings")
    plt.ylabel("Frequency")
    plt.title(header[0])
    plt.grid(True)
    plot_file_path = os.path.join(
        output_directory, "plots", f"{exercise_name}_frequency2_histogram.png"
    )
    plt.savefig(plot_file_path)


if __name__ == "__main__":
    main()
