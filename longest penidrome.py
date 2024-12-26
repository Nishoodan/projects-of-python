def longest_palindrome(string):
    # Split the string into words
    words = string.split()
    longest = ""  # Initialize the longest palindrome variable

    for word in words:
        # Check if the word is a palindrome
        if word == word[::-1]:
            # Update longest if the current palindrome is longer
            if len(word) > len(longest):
                longest = word

    if longest:  # If a palindrome was found
        print(f"The longest palindrome is: {longest}")
    else:  # No palindrome found
        print("No palindromes found in the string.")

# Input from the user
string = input("Enter a string: ").lower()
longest_palindrome(string)
