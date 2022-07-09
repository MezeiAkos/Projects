# TODO make brute force decoder
# TODO learn frequency analysis
# TODO handle negative keys, typos

original_text = input("Write text to encode here:")


def key_shifter(encoding_or_decoding, left_or_right, key):
    if encoding_or_decoding == "encode":
        if left_or_right == "left":
            return 26 - key
        else:
            return key
    else:
        if left_or_right == "left":
            return key
        else:
            return 26 - key


coding = input("Do you want to encode or decode?")
direction = input("Do you want to shift left or right?")
key = int(input("Key: "))
if key > 25:
    key = key - (int(key / 25) * 25)
key_shifter(coding, direction, key)
characters = list(original_text)
characters = [ord(element) for element in characters]  # change characters into integers

for index, character in enumerate(characters):
    if 65 <= character <= 90:  # uppercase letters
        if character + key <= 90:
            characters[index] = character + key
        else:
            characters[index] = 64 + ((character + key) - 90)
    if 97 <= character <= 122:  # lowercase letters
        if character + key <= 122:
            characters[index] = character + key
        else:
            characters[index] = 96 + ((character + key) - 122)

print(''.join(chr(character) for character in characters))  # change integers back into characters
