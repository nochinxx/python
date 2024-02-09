import os
import sys
import math


def read_exercise(exercise_file):
    # Define the path to the exercise file
    exercise_file_path = os.path.join(
        os.path.dirname(__file__), "..", "exercises", exercise_file
    )

    # Check if the exercise file exists
    if not os.path.exists(exercise_file_path):
        print(f"Error: Exercise file '{exercise_file}' not found.")
        sys.exit(1)

    # Open the exercise file for reading
    with open(exercise_file_path, "r") as file:
        # Read the contents of the exercise file
        exercise_data = file.readlines()

    return exercise_data


def main():
    # Check if the exercise file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python your_program.py <exercise_file>")
        sys.exit(1)

    # Get the exercise file name from the command-line arguments
    exercise_file = sys.argv[1]

    # Read the exercise file
    exercise_data = read_exercise(exercise_file)

    # Initialize an empty list to store the data
    data = []

    # Iterate over the lines in the exercise data and convert them to integers
    for line in exercise_data:
        # Remove any leading/trailing whitespace and convert to integer
        item = int(line.strip())
        # Append the integer to the data list
        data.append(item)

    # Now you can use the contents of the exercise file as needed
    # for item in data:
    #    print(item)

    # Program functionalities:

    # Max and Min:
    max_val = max(data)
    min_val = min(data)
    print("Maximum value:", max_val)
    print("Minimum value:", min_val)

    # Class width

    class_num = int(input("Input the number of classes: "))
    if class_num == 0:
        class_width = int(input("Input class width: "))
    else:
        class_width = (max_val - min_val) / class_num
    print(class_width)

    if class_num == 0:
        class_width = class_width + 1
        class_num=5
    elif class_width.is_integer():
        class_width = class_width + 1
    else:
        class_width = math.ceil((max_val - min_val) / class_num)
    print("Class Width:", class_width)

    # Compute and store the limits for each class
    limits = []
    for i in range(class_num):
        lower_limit = min_val + (i * class_width) - 0.5
        upper_limit = min_val + ((i + 1) * class_width) - 0.5
        limits.append((lower_limit, upper_limit))

    # print("Limits:", limits)

    # Count the frequency for each class
    frequencies = [0] * len(limits)
    total_data_points = len(data)

    for value in data:
        for i, (lower, upper) in enumerate(limits):
            if lower <= value < upper:
                frequencies[i] += 1

    # Calculate the relative frequency for each class
    relative_frequencies = [freq / total_data_points for freq in frequencies]

    # Print frequency and relative frequency for each class
    for i, ((lower, upper), freq, rel_freq) in enumerate(
        zip(limits, frequencies, relative_frequencies)
    ):
        print(f"Class {i+1}: Lower Limit = {lower}, Upper Limit = {upper}")
        print(f"Frequency: {freq}")
        print(f"Relative Frequency: {rel_freq}")
        print()


if __name__ == "__main__":
    main()
