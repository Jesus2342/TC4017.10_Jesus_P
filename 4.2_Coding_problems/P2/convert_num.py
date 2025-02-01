"""
Instituto Tecnologico y de Estudios Superiores de Monterrey 
Student: Jose de Jesus Pena Rodriguez 
Student ID: A01794940
Programming Exercise: Converter
Description: The program shall convert the numbers to 
             num_bin and num_hex base.

Usage: 
python convert_num.py TC1.txt  
python convert_num.py TC2.txt  
python convert_num.py TC3.txt  
python convert_num.py TC4.txt  
"""""

import sys
import time

def convert_binary(number):
    """Convert a decimal number to num_bin using basic algorithm."""
    if number == 0:
        return "0"
    num_bin = ""
    while number > 0:
        num_bin = str(number % 2) + num_bin
        number //= 2
    return num_bin

def convert_binary_negative(number):
    """Convert a negative decimal number to num_bin (10-bit)"""
    return format(number & 0x3FF, 'b')

def convert_hexadecimal(number):
    """Convert a decimal number to num_hex using basic algorithm."""
    hex_chars = "0123456789ABCDEF"
    if number == 0:
        return "0"
    num_hex = ""
    while number > 0:
        num_hex = hex_chars[number % 16] + num_hex
        number //= 16
    return num_hex

def convert_hexadecimal_negative(number):
    """Convert a negative decimal number to num_hex (32-bit)"""
    return format(number & 0xFFFFFFFF, '08X')

def process_file(file_path):
    """Process the file"""
    results = []
    start_time = time.time()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for index, line in enumerate(lines, start=1):
            line = line.strip()
            try:
                number = int(line)
                num_bin = (convert_binary, convert_binary_negative)[number < 0](number)
                num_hex = (convert_hexadecimal, convert_hexadecimal_negative)[number < 0](number)
                results.append(f"{index}: {number}: BIN = {num_bin}, HEX = {num_hex}")
            except ValueError:
                error_msg = f"{index}: {line} #VALUE! #VALUE!"
                print(error_msg)
                results.append(error_msg)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    elapsed_time = time.time() - start_time
    results.append(f"Execution Time: {elapsed_time:.6f} seconds")
    for result in results:
        print(result)
    with open("ConvertionResults.txt", 'w', encoding='utf-8') as output_file:
        for result in results:
            output_file.write(result + "\n")

def main():
    """Main process to process the file"""
    file_path = sys.argv[1]
    process_file(file_path)

if __name__ == "__main__":
    main()
