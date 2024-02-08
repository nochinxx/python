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
    #for item in data:
    #    print(item)

    # Program functionalities:
    
    # Max and Min:
    max_val = max(data)
    min_val = min(data)
    print("Maximum value:", max_val)
    print("Minimum value:", min_val)
    
    # Class width
    class_num = int(input("Input the number of classes: "))
    class_width = math.ceil((max_val - min_val) / class_num)
    print("Class Width:", class_width)
    
    # Compute and store the limits for each class
    limits = []
    for i in range(class_num + 1):
        limit = min_val + (i * class_width)
        limits.append(limit)

    print("Limits:", limits)
    
    
if __name__ == "__main__":
    main()
