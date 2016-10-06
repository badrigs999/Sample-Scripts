N = input()
tup = raw_input()
out = tuple(tup.replace(' ',''))
a = out[:N]
mytuple = tuple(map(int, a))
print hash(mytuple)