"""
This module computes descriptive statistics 
(mean, median, mode, standard deviation, and variance)
for a list of numbers provided in a file. It handles invalid 
data gracefully, calculates the statistics
using basic algorithms without relying on external libraries, 
and writes the results to both the console
and a file named StatisticsResults.txt. 
It also measures and reports the execution time.
"""

import sys
import time


def read_file(file_path):
    """
    Reads a file and attempts to convert each line to a float.

    :param file_path: Path to the file to be read.
    :return: List of valid float numbers found in the file. Skips invalid data.
    """
    valid_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                try:
                    number = float(stripped_line)
                    valid_data.append(number)
                except ValueError:
                    print(f"Invalid data found and skipped: {stripped_line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return []
    return valid_data

def compute_mean(data):
    """
    Calculates the mean of a list of numbers.

    :param data: List of numbers.
    :return: The mean of the list.
    """
    return sum(data) / len(data) if data else 0

def compute_median(data):
    """
    Calculates the median of a list of numbers.

    :param data: List of numbers.
    :return: The median of the list.
    """
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    return (sorted_data[mid] + sorted_data[-mid-1]) / 2 if n % 2 == 0 else sorted_data[mid]

def compute_mode(data):
    """
    Calculates the mode(s) of a list of numbers.

    :param data: List of numbers.
    :return: The mode of the list, or "NA" if no mode found.
    """
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    max_frequency = max(frequency.values(), default=0)
    modes = [key for key, val in frequency.items() if val == max_frequency]

    if len(data)==len(modes):
        return "NA"
    return modes[0]

def compute_variance(data, mean):
    """
    Calculates the variance of a list of numbers.

    :param data: List of numbers.
    :param mean: The mean of the list.
    :return: The variance of the list.
    """
    #return statistics.variance(data)
    return sum((x - mean) ** 2 for x in data) / (len(data)-1) if data else 0
def compute_std_dev(variance):
    """
    Calculates the standard deviation from the variance.

    :param variance: The variance of a list of numbers.
    :return: The standard deviation.
    """
    return variance ** 0.5
def write_results_to_file(results, file_name="StatisticsResults.txt"):
    """
    Writes the calculated statistics results to a file.

    :param results: Dictionary of statistics results.
    :param file_name: Name of the file to write the results to.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")
    print(f"Results written to {file_name}")

def main():
    """
    Main function to execute the program workflow.
    """
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    data = read_file(file_path)
    if not data:
        print("No valid data found.")
        sys.exit(2)
    count=len(data)
    mean = compute_mean(data)
    median = compute_median(data)
    mode = compute_mode(data)
    variance = compute_variance(data, mean)
    std_dev = compute_std_dev(variance)
    results = {
        "Count":count,
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Standard Deviation": std_dev,
        "Variance": variance,
        "Execution Time": f"{time.time() - start_time:.2f} seconds"
    }
    for key, value in results.items():
        print(f"{key}: {value}")
    write_results_to_file(results)

if __name__ == "__main__":
    main()
