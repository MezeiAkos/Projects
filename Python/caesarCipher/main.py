# TODO ask if you want to encode or decode
# TODO wrap z back to a
# TODO make brute force decoder
original_text = input("Write text to encode here:")
key = input("Encoding key: ")
key = int(key)

characters = list(original_text)
characters = [ord(element) for element in characters]
# TODO learn list comprehensions

print(characters)
# TODO learn lambda

