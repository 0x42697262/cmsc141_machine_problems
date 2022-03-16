"""
Author: Will Hong
Description

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
"""


s = "q,r,g,m,a,p,s,u,y,e,b,o,h,v,j,t,k,w,c,f,l,x,z,i,n,d"
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

encoded_string = "FXSLSPT{5HK5717H710Y_3N0UH710Y_59533E2J}"
decoded_string = ''

for char in encoded_string:
    decoded_string += ctf_dictionary[char]

print(decoded_string)


