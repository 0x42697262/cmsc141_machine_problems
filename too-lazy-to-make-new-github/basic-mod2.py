"""
    Author: Will Hong

    A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
"""

# list all characters that we need for mapping

character_set = []
for c in range(26):
    character_set.append(chr(65+c))

for c in range(10):
    character_set.append(c)

character_set.append("_")


# read the file as input

message = None

with open("basic-mod2-message.txt", "r") as message_file:
    temp = None
    for line in message_file.readlines():
        temp = line
    message = temp.split()

# use modulo inverse maths to map the input

decoded = list()

for chars in message:
    decoded.append(pow(int(chars), 41-2, 41)) # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python


# then we decode

final_message = ''

for dc in decoded:
    final_message += str(character_set[dc-1])

print(final_message)            # 1NV3R53LY_H4RD_C680BDC1

