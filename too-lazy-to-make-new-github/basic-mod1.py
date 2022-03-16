"""
Author: Will Hong

We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message here. Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

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

with open("basic-mod1-message.txt", "r") as message_file:
    temp = None
    for line in message_file.readlines():
        temp = line
    message = temp.split()


# use modulo maths to map the input

decoded = list()

for chars in message:
    decoded.append(int(chars) % 37)


# then we decode

final_message = ''

for dc in decoded:
    final_message += str(character_set[dc])

print(final_message)            # R0UND_N_R0UND_79C18FB3

