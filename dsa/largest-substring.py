string = input()
substrs = []
sub = []
i = 0
if string == "":
    print("0")
else:
    while i < len(string):
        for c in string[i::]:
            if c not in sub:
                sub.append(c)
            else:
                i = string.find(c,i,len(string)-1)
                break
        substrs.append(''.join(sub))
        sub.clear()
        i += 1
    print(len(max(substrs,key=len)))
