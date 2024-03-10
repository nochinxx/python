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
        "test",
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

    # Ask the user for the number of classes
    class_num = int(input("Input the number of classes: "))
    if class_num == 0:
        class_width = int(input("Input class width: "))
    else:
        class_width = (max_val - min_val) / class_num
    print("Class Width 0: ", class_width)

    # Calculate class width
    if class_num == 0:
        class_num = math.ceil((max_val - min_val) / class_width)
        print("Class Num: ", class_num)
    elif class_width.is_integer():
        class_width = class_width + 1
    else:
        class_width = math.ceil((max_val - min_val) / class_num)
    print("Class width:", class_width)

    # Compute and store the limits for each class
    limits = []
    # Compute and store the limits for each class
    for i in range(class_num):
        lower_limit = round(
            min_val + (i * class_width),
            -int(math.floor(math.log10(abs(class_width))) - 2),
        )
        upper_limit = round(
            min_val + ((i + 1) * class_width),
            -int(math.floor(math.log10(abs(class_width))) - 2),
        )
        limits.append((lower_limit - 0.5, upper_limit - 0.5))

    # Count the frequency for each class
    frequencies = [0] * len(limits)
    total_data_points = len(data)

    for value in data:
        for i, (lower, upper) in enumerate(limits):
            if lower <= value < upper:
                frequencies[i] += 1

    # Calculate the relative frequency for each class
    relative_frequencies = [freq / total_data_points for freq in frequencies]

    # Calculate the cumulative frequency
    cumulative_frequencies = [
        sum(relative_frequencies[: i + 1]) for i in range(len(relative_frequencies))
    ]

    # Print frequency, relative frequency, and cumulative frequency for each class
    print(
        "{:<20} {:<15} {:<15} {:<15}".format(
            "Class", "Frequency", "Rel. Freq.", "Cum. Freq."
        )
    )
    for i, ((lower, upper), freq, rel_freq, cum_freq) in enumerate(
        zip(limits, frequencies, relative_frequencies, cumulative_frequencies)
    ):
        print(
            f"{lower:.2f} - {upper:.2f}",
            f"{freq:<15}",
            f"{rel_freq:<15.2f}",
            f"{cum_freq:<15.2f}",
        )

    # Get the exercise name
    exercise_name = get_exercise_name(exercise_file)

    # Export frequency table to a text file
    output_directory = os.path.join(
        os.path.dirname(__file__), "..", "test", "answers"
    )
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = os.path.join(
        output_directory,
        f"{get_exercise_name(exercise_file)}_frequency2_table.txt",
    )
    with open(output_file, "w") as f:
        f.write(
            "{:<20} {:<15} {:<15} {:<15}\n".format(
                "Class", "Frequency", "Rel. Freq.", "Cum. Freq."
            )
        )
        for i, ((lower, upper), freq, rel_freq, cum_freq) in enumerate(
            zip(limits, frequencies, relative_frequencies, cumulative_frequencies)
        ):
            f.write(
                f"{lower:.2f} - {upper:.2f} {freq:<15} {rel_freq:<15.2f} {cum_freq:<15.2f}\n"
            )

    print(f"Frequency table exported to '{output_file}'.")

    # Plotting the frequency histogram
    plt.figure(figsize=(10, 6))

    # Create a list of x-axis positions for the ticks
    x_positions = [lower for lower, _ in limits]

    # Create a list of labels for the x-axis ticks representing the range of each class
    x_labels = [f"{lower:.2f} - {upper:.2f}" for lower, upper in limits]

    plt.bar(
        x_positions,  # Use the x-axis positions for the ticks
        frequencies,
        width=class_width,
        align="center",
        alpha=0.7,
        edgecolor="black",
    )
    plt.xlabel("Classes")
    plt.ylabel("Freq")
    plt.title(header[0])
    plt.xticks(
        x_positions,  # Set the x-axis ticks to the lower limit of each class
        x_labels,  # Set the labels for the x-axis ticks
        rotation=45,  # Rotate x-axis labels for better visibility
    )
    plt.grid()
    # Adjust margins to accommodate labels and call tight_layout to automatically adjust subplot parameters
    plt.margins(x=0.05)
    plt.tight_layout()
    plot_file_path = os.path.join(
        output_directory, "plots", f"{exercise_name}_frequency2_histogram.png"
    )
    plt.savefig(plot_file_path)


if __name__ == "__main__":
    main()
