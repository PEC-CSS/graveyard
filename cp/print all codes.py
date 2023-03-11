def print_all_codes(s,s2):
    if(len(s)==1):
        print(s2+chr(int(s[0])+96))
    elif(len(s)==2):
        print(s2+chr(int(s[0])+96)+chr(int(s[1])+96))
        if(int(s[0])*10+int(s[1])<=26):
            print(s2+chr(int(s[0])*10+int(s[1])+96))
    else:
        print_all_codes(s[1:],s2+chr(int(s[0])+96))
        if(int(s[0])*10+int(s[1])<=26):
            print_all_codes(s[2:],s2+chr(int(s[0])*10+int(s[1])+96))
        
s=[]
s=input()
print_all_codes(s,"")