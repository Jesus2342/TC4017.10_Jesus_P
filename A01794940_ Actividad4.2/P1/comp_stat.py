"""
Instituto Tecnologico y de Estudios Superiores de Monterrey 
Student: Jose de Jesus Pena Rodriguez 
Student ID: A01794940
Programming Exercise: Compute statistics
Description: The program shall compute all descriptive 
             statistics from a file containing numbers. 

Usage: 
Type the name of the text file in INPUT_FILE then 
run --->  python comp_stat.py  
"""""


import os
import time


INPUT_FILE = "TC1.txt"
OUTPUT_FILE = "statisticsResults_test.txt"

def validate_number(value):
    """Validates if a value is a valid number."""
    try:
        return float(value)
    except ValueError:
        return None

def read_numbers_from_file(file_path):
    """Reads valid numbers from a file"""
    numbers = []
    total_elements = 0

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        for _, line in enumerate(file, start=1):
            line = line.strip()
            total_elements += 1
            number = validate_number(line)
            if number is not None:
                numbers.append(number)

    return numbers, total_elements

def compute_mean(numbers):
    """Computes the average."""
    total_sum = sum(numbers)
    return total_sum / len(numbers)

def compute_median(numbers):
    """Computes the median."""
    numbers_sorted = sorted(numbers)
    aux_n = len(numbers_sorted)
    middle = aux_n // 2
    if aux_n % 2 == 0:
        return (numbers_sorted[middle - 1] + numbers_sorted[middle]) / 2
    return numbers_sorted[middle]

def compute_mode(numbers):
    """Computes the mode"""    
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_frequency = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == max_frequency]

    if len(modes) == 1:
        return modes[0]
    if len(modes) > 1:
        return modes[0]
    return "#NA"

def compute_variance(numbers):
    """Computes variance."""
    mean = compute_mean(numbers)
    variance_sum = sum((number - mean) ** 2 for number in numbers)
    return variance_sum / len(numbers)

def compute_standard_deviation(numbers):
    """Computes standard deviation."""
    return round(compute_variance(numbers) ** 0.5, 6)

def print_variance(numbers):
    """Prints variance using standard deviation"""
    return pow(compute_standard_deviation(numbers), 2)

def count_numbers(numbers):
    """Counts the total number of valid values in the list."""
    return len(numbers)

def compute_statistics(numbers, total_elements):
    """Computes statistics from text file"""
    stats = {
        "Count": total_elements,
        "Mean": round(compute_mean(numbers),4),
        "Median": compute_median(numbers),
        "Mode": compute_mode(numbers),
        "Standard deviation": round(compute_standard_deviation(numbers),4),
        "Variance": round(print_variance(numbers),4)        
    }
    return stats

def write_results_to_file(output_path, stats, execution_time):
    """Writes the results to a file."""
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("Statistical Results:\n")
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")

        file.write(f"\nExecution time: {execution_time:.6f} seconds\n")

def main():
    """Main process"""
    start_time = time.time()

    try:
        numbers, total_elements = read_numbers_from_file(INPUT_FILE)

        if not numbers:
            print("No valid numbers in text file")
            return

        stats = compute_statistics(numbers, total_elements)
        execution_time = time.time() - start_time

        print("Statistical Results:")
        for key, value in stats.items():
            print(f"{key}: {value}")

        print(f"\nExecution time: {execution_time:.6f} seconds")
        write_results_to_file(OUTPUT_FILE, stats, execution_time)

    except FileNotFoundError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
