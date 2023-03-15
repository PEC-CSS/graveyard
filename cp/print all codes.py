def print_all_codes(s,s2):
    if(len(s)==1 and 1<=int(s[0])):
        print(s2+chr(int(s[0])+96))
    elif(len(s)==2):
        if(1<=int(s[0]) and 1<=int(s[1])):
            print(s2+chr(int(s[0])+96)+chr(int(s[1])+96))
        if(1<=int(s[0]) and (int(s[0])*10+int(s[1])<=26)):
            print(s2+chr(int(s[0])*10+int(s[1])+96))
    else:
        if(1<=int(s[0])):
            print_all_codes(s[1:],s2+chr(int(s[0])+96))
        if(1<=int(s[0]) and (int(s[0])*10+int(s[1])<=26)):
            print_all_codes(s[2:],s2+chr(int(s[0])*10+int(s[1])+96))
        

s=input()
print_all_codes(s,"")