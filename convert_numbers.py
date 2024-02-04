"""
This module converts numbers from a file to binary and hexadecimal format,
then writes the conversion results to 'ConversionResults.txt'.
"""
import sys
import time

def read_file(file_path):
    """
    Reads integers from a file, skipping invalid data.

    :param file_path: The path to the file to be read.
    :return: A list of integers found in the file.
    """
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                try:
                    number = int(stripped_line)
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid data found and skipped: {stripped_line}")
        return numbers
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def to_twos_complement(binary_str, bits=32):
    """
    Converts a binary string to two's complement form of specified bit length.

    :param binary_str: The binary string to convert.
    :param bits: The bit length for the two's complement form.
    :return: A two's complement binary string.
    """
    if len(binary_str) > bits:
        # If the binary string exceeds the desired bit length, trim it
        return binary_str[-bits:]
    while len(binary_str) < bits:
        # Extend the binary string to the desired bit length by prefixing with the sign bit
        binary_str = '1' + binary_str
    return binary_str

def convert_to_binary(number):
    """
    Converts an integer to its binary representation, handling negative numbers.

    :param number: The integer to convert.
    :return: The binary representation of the integer.
    """
    if number >= 0:
        binary_representation = bin(number)[2:]  # strip off the '0b' prefix
    else:
        # Calculate the two's complement for negative numbers manually
        positive_binary = bin(number & 0xffffffff)[2:]  # Convert to binary and keep last 32 bits
        binary_representation = to_twos_complement(positive_binary)
    return binary_representation[-10:]

def convert_to_hexadecimal(number):
    """
    Converts an integer to its hexadecimal representation, handling negative numbers.

    :param number: The integer to convert.
    :return: The hexadecimal representation of the integer.
    """
    hexadecimal=format(number & 0xffffffff, 'X')
    if number<0:
        return "FF"+str(hexadecimal)
    return hexadecimal

def write_results_to_file(results, file_name="ConversionResults.txt"):
    """
    Writes the conversion results to a specified file.

    :param results: A list of dictionaries with conversion results.
    :param file_name: The name of the file to write to.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("Number, Binary, Hexadecimal\n")
        for result in results:
            file.write(f"{result['number']}, {result['binary']}, {result['hexadecimal']}\n")
    print(f"Results written to {file_name}")

def main():
    """
    Main function to read numbers from a file, convert them to binary and hexadecimal,
    and write the results to a file.
    """
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    numbers = read_file(file_path)
    if not numbers:
        print("No valid data found.")
        sys.exit(2)

    results = []
    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)
        results.append({
            "number": number,
            "binary": binary,
            "hexadecimal": hexadecimal
        })
        print(f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}")

    write_results_to_file(results)

    execution_time = time.time() - start_time
    print(f"Execution Time: {execution_time:.2f} seconds")
    with open("ConversionResults.txt", 'a', encoding='utf-8') as file:
        file.write(f"Execution Time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()
