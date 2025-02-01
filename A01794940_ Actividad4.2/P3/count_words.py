"""
Instituto Tecnologico y de Estudios superiores de Monterrey 
Student: Jose de Jesus Pena Rodriguez 
Student ID: A01794940
Programming Exercise: Count Words 
Description: The program shall identify all distic words and the 
             frequency of them.

Usage: 
python count_words.py TC1.txt  
python count_words.py TC2.txt  
python count_words.py TC3.txt  
python count_words.py TC4.txt  
python count_words.py TC5.txt  
"""""

import sys
import time


def read_file(filename):
    """Read the file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)


def count_words(text):
    """ Function to count occurrences of each word"""
    words = text.split()
    word_count = {}
    for word in words:
        clean_word = ''.join(char.lower() for char in word if char.isalnum())
        if clean_word:
            if clean_word in word_count:
                word_count[clean_word] += 1
            else:
                word_count[clean_word] = 1
    return word_count


def write_results(word_count, elapsed_time):
    """Function to print number of ocurrences per word."""
    with open("WordCountResults.txt", "w", encoding='utf-8') as file:
        for word, count in sorted(word_count.items()):
            file.write(f"{word}: {count}\n")
        file.write(f"\nTime elapsed: {elapsed_time:.4f} seconds\n")


def main():
    """Main function to execute the program"""
    filename = sys.argv[1]
    start_time = time.time()
    text = read_file(filename)
    word_count = count_words(text)
    elapsed_time = time.time() - start_time
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")
    print(f"\nTime elapsed: {elapsed_time:.4f} seconds")
    write_results(word_count, elapsed_time)


if __name__ == "__main__":
    main()
