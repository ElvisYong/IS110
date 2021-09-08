word = input("Enter a word: ")
# Reverse operator
if word == word[::-1]:
    print("Palindrome")


# iteration
length = len(word)
start = 0
end = length - 1
palindrome = True

while start < end:
    if word[start] != word[end]:
        palindrome = False
        break
    start += 1
    end -= 1

print(f"{word} is {'NOT' if not palindrome else ''} a palindrome")