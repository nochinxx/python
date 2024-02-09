import os
import sys
import matplotlib.pyplot as plt

# Lists to store x and y values
x = []
y = []

def read_exercise(exercise_file):
    # Define the path to the exercise file
    exercise_file_path = os.path.join(
        os.path.dirname(__file__), "..", "exercises", "2.3", exercise_file
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
    # Read data from text file
    for line in exercise_data:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))
    
     # Get the exercise name
    exercise_name = get_exercise_name(exercise_file)
    
    # Define the directory to save the plot
    output_directory = os.path.join(
        os.path.dirname(__file__), "..", "exercises", "2.3","plots",
    )
    
    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color="blue", marker="o")
    plt.title("Scatter Plot")
    plt.xlabel("Prenatal Care Percentage")
    plt.ylabel("Health exp % of GDP")
    plt.grid(True)
    # Save plot in the same directory as the exercises
    plot_file_path = os.path.join(output_directory, f'{exercise_name}_scatter_plot.png')
    plt.savefig(plot_file_path)
    
if __name__ == "__main__":
    main()