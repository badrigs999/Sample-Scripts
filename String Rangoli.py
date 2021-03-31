import string
import sys
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
