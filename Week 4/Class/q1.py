# Part I
# message = input("Enter a message: ")
# for characters in message:
#     print(characters, end=" ") 

# Part II
# message = input('Enter a message: ')
# for i, char in enumerate(message):
#     if i == len(message) - 1:
#         print(char)
#         break
#     print(char, end='-')

#Part III
def print_message_with_separators(msg, sep):
    for i, char in enumerate(msg):
        if i == len(msg) - 1:
            print(char)
            break
        print(char, end=sep)

message = input('Enter a message: ')
sep = input('Enter a separator: ')
print_message_with_separators(message, sep)
