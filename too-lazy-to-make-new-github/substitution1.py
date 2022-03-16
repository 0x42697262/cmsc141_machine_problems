"""
Author: Will Hong
Description

It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?
"""


s = "v,m,g,k,i,b,t,n,d,e,w,q,c,f,x,p,a,y,u,j,s,h,r,l,z,o"
ctf_keys = s.split(",")

ctf_dictionary = dict()
for c in range(26):
    ctf_dictionary[chr(65+c)] = ctf_keys[c]

ctf_dictionary["{"] = '{'
ctf_dictionary["}"] = '}'
ctf_dictionary["_"] = '_'

for c in range(10):
    ctf_dictionary[str(c)] = str(c)
    print(str(c))

print(ctf_dictionary)

encoded_string = "PEMZMGN{H6W4B_4H41R515_15_73I10S5_8J1FN808}"
decoded_string = ''

for char in encoded_string:
    decoded_string += ctf_dictionary[char]

print(decoded_string)


