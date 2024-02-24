import csv
import os
import sys

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
        print(data)
    return data

def write_to_csv(data, header,data_file):
    directory = os.path.join(
        os.path.dirname(__file__),
        "..",
        "exercises",
        "homework_3",
    )
    csv_file_name = f"{os.path.splitext(data_file)[0]}.csv"
    csv_file_path = os.path.join(directory, csv_file_name)
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([header])
        writer.writerows(map(lambda x: [x], data))

def main():
    if len(sys.argv) != 2:
        print("Usage: python your_program.py <exercise_file>")
        sys.exit(1)
        
    # Get the exercise file name from the command-line arguments
    data_file = sys.argv[1]
    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "exercises",
        "homework_3",
        data_file,
    )
    
    if not os.path.exists(file_path):
        print(f"Error: Exercise file '{data_file}' not found in '{file_path}'")
        sys.exit(1)

    header = input("Enter the header for the CSV file: ")
    data = read_data_from_file(file_path)
    write_to_csv(data, header,data_file)
    print("Data has been written to 'data.csv' with the specified header.")

if __name__ == "__main__":
    main()