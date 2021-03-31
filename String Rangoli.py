import string
import sys

# Method 1
char_list = string.ascii_lowercase[:5][::-1]
char_len = (len(char_list)*2-1)*2-1
for i in range(-4, 4):
    i = 4-i if i > -1 else i
    print ("-".join(char_list[:i]+char_list[:i][::-1][1:]).center(char_len, '-'))

    
    
# Method 2
def print_rangoli(s):

    alpha = string.ascii_lowercase

    for i in range(s - 1, 0, -1):
        r = ["-"] * (s * 2 - 1)
        for j in range(0, s - i):
            r[s - 1 - j] = alpha[j + i]
            r[s - 1 + j] = alpha[j + i]
        print("-".join(r))

    for i in range(0, s):
        r = ["-"] * (s * 2 - 1)
        for j in range(0, s - i):
            r[s - 1 - j] = alpha[j + i]
            r[s - 1 + j] = alpha[j + i]
        print("-".join(r))
print_rangoli(5)

"""
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
