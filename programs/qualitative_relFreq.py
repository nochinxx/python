import os
import sys
import csv
import matplotlib.pyplot as plt


def read_exercise(exercise_file):
    # Define the path to the exercise file
    exercise_file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "exercises",
        "dataTransformed",
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

    # Calculate the relative frequency for each class
    relative_frequencies = {item: freq / total_data_points for item, freq in frequencies.items()}

    # Calculate cumulative frequency
    cumulative_frequency = 0
    cumulative_frequencies = {}
    for item, freq in sorted(frequencies.items()):
        cumulative_frequency += freq
        cumulative_frequencies[item] = cumulative_frequency

    # Print frequency, relative frequency, and cumulative frequency for each class
    print("{:<15} {:<10} {:<15} {:<15}".format("Class", "Frequency", "Rel. Freq.", "Cum. Freq."))
    for item in sorted(frequencies.keys()):
        freq = frequencies[item]
        rel_freq = relative_frequencies[item]
        cum_freq = cumulative_frequencies[item]
        print(f"{item:<15} {freq:<10} {rel_freq:<15.2f} {cum_freq:<15}")

    # Get the exercise name
    exercise_name = get_exercise_name(exercise_file)

    # Export frequency table to a text file
    output_directory = os.path.join(
        os.path.dirname(__file__), "..", "exercises", "answers_from_dataTransformed"
    )
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = os.path.join(
        output_directory,
        f"{get_exercise_name(exercise_file)}_cum_frequency_table.txt",
    )
    with open(output_file, "w") as f:
        f.write("{:<15} {:<10} {:<15} {:<15}\n".format("Class", "Frequency", "Rel. Freq.", "Cum. Freq."))
        for item in sorted(frequencies.keys()):
            freq = frequencies[item]
            rel_freq = relative_frequencies[item]
            cum_freq = cumulative_frequencies[item]
            f.write(f"{item:<15} {freq:<10} {rel_freq:<15.2f} {cum_freq:<15}\n")

    print(f"Frequency table exported to '{output_file}'.")
    xLabel=input("input x label: ")
    # Plotting the relative frequency histogram
    plt.figure(figsize=(10, 6))
    plt.bar(relative_frequencies.keys(), relative_frequencies.values(), align="center", alpha=0.7)
    plt.xlabel(xLabel)
    plt.ylabel("Relative Frequency")
    plt.title(header[0])
    plt.grid(True)
    plot_file_path = os.path.join(
        output_directory, "plots", f"{exercise_name}_relative_frequency3_histogram.png"
    )
    plt.savefig(plot_file_path)
    print(f"Plot exported to '{plot_file_path}'.")


if __name__ == "__main__":
    main()
