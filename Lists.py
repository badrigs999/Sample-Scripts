#learn list

n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"   # or eval("l."+"insert(0,5)")
        eval("l."+cmd)
    else:
        print l

