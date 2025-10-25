# E14.py
# Author: [Your Name]
# Date: [Insert Date]
# Description: This program allows the user to input a list of words repeatedly until a blank input is entered.
#              It then creates a single string with all the words separated by commas and prints it.

def main():
    # Initialize an empty list to store words
    words = []
    word = "placeholder"  # LCV to start the loop

    print("Enter words one at a time. Press Enter on a blank line to stop.")

    # Use a while loop with a loop control variable
    while word != "":
        word = input("Enter a word: ").strip()
        if word != "":
            words.append(word)

    # Build the result string manually
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i < len(words) - 1:  # Add a comma except for the last word
            result += ", "

    # Print the result
    print("The words you entered are:")
    print(result)

# Call the main function
main()
