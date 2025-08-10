# Check if a string is a palindrome
text = input("Enter a word: ")
if text.lower() == text.lower()[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")