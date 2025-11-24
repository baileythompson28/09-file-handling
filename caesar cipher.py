"""
Create a python program that will print out a list of txt files in the current directory.
Allow the user to choose which file to decode.
If the file exists, open the file and print the decoded message.
If the file does not exist, print that it does not exist.
Repeat this process until the user types “q”
"""

import os
def caesar_cipher():
    shift = 3
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    textfiles = [f for f in os.listdir('.') if f.endswith('.txt')] 
    while True:
        print("\nFiles:")
        for f in textfiles:
            print(f)
        filename = input("File to decode ('q' to quit): ")
        if filename.lower() == 'q':
            break
        if filename in textfiles:
            with open(filename, 'r') as file:
                encoded_message = file.read()
            decoded_message = ''
            for char in encoded_message:
                if char in alphabet:
                    index = alphabet.index(char)
                    new_index = (index - shift) % len(alphabet)
                    decoded_message += alphabet[new_index]
                else:
                    decoded_message += char
            print("\nDecoded:")
            print(decoded_message)
        else:
            print(f"The file '{filename}' does NOT exist.")

if __name__ == "__main__": 
    caesar_cipher()
