"""
Author: Will Hong
Description

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
"""

message = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"

# [heT][fl ][g a][s i][icp][CTo][{7F][4NR][P05][1N5][_16][_35][P3X][51N][3_V][6E5][926][A}4]
# [The][ fl][ag ][ is] ....
# swap 3 and 1, swap 2 and 3, repeat

grouped_message = list()
for group in range(0,54,3):
    grouped_message.append(message[group:group+3])


decoded_group = list()
for group in grouped_message:
    a = group[0]
    b = group[1]
    c = group[2]
    a,c = c,a
    b,c = c,b
    decoded_group.append(str(a+b+c))

flag = ''
for group in decoded_group:
    flag += group

print(flag) # picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
