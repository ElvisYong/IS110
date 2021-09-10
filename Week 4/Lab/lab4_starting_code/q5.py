def pad_message(msg: str, width: int) -> str:
    """
    Pads a message with spaces to make it width characters wide.
    """
    if len(msg) < width:
        return msg.rjust(width)
    else:
        return msg[:width]

print(pad_message("IS111 Lab 5", 20))
print(pad_message("IS111 Lab 5", 8))
print(pad_message("hello", 20))
print(pad_message("python programmming", 20))
print(pad_message("Hello World! I enjoy programming in Python.", 20))