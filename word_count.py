"""
This module reads a text file, counts occurrences of each distinct word,
excluding non-alphabetic strings, and writes the counts to a results file.
It also calculates and displays the execution time.
"""
import sys
import time

def read_file(file_path):
    """
    Reads the entire content of a file.

    :param file_path: The path of the file to read.
    :return: The content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except PermissionError:
        print(f"Permission denied: {file_path}")
        sys.exit(1)

def count_words(text):
    """
    Counts the occurrences of each distinct word in a text.

    :param text: The text to analyze.
    :return: A dictionary with words as keys and their counts as values.
    """
    lines = text.split('\n')  # Split the text into lines
    word_count = {"(Blank)": 0}  # Initialize "(Blank)" count
    for line in lines:
        if not line.strip():  # Check if the line is blank
            word_count["(Blank)"] += 1
            continue  # Skip to the next line
        words = line.split()
        for word in words:
            if word.isalpha():  # Check if the word contains only letters
                word_count[word] = word_count.get(word, 0) + 1
            else:
                print(f"Invalid data found and skipped: {word}")
    return word_count

def write_results_to_file(word_count, file_name="WordCountResults.txt"):
    """
    Writes word counts to a specified file.

    :param word_count: Dictionary of word counts.
    :param file_name: The filename to write to.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            file.write(f"{word}: {count}\n")
    print(f"Results written to {file_name}")

def main():
    """
    Main function that orchestrates the reading, counting, and writing operations.
    """
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    text = read_file(file_path)
    word_count = count_words(text)
    sum_of_words=0
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")
        sum_of_words+=count
    print(f"Grand Total: {sum_of_words}")
    word_count["Grand Total"]=sum_of_words
    write_results_to_file(word_count)

    execution_time = time.time() - start_time
    print(f"Execution Time: {execution_time:.2f} seconds")
    with open("WordCountResults.txt", 'a', encoding='utf-8') as file:
        file.write(f"Execution Time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()
