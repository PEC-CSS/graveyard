num_of_problems=int(input())
head_or_tail=input()
inputlist=input().split()
for i in range(num_of_problems):
    if(inputlist[i]=="E"):
        inputlist[i]=2
    if(inputlist[i]=="M"):
        inputlist[i]=4
    if(inputlist[i]=="H"):
        inputlist[i]=6

alice=0
bob=0
if(head_or_tail=="T"):
    for i in range(0,num_of_problems,2):
        alice=alice+inputlist[i]
    for i in range(1,num_of_problems,2):
        bob=bob+inputlist[i]
if(head_or_tail=="H"):
    for i in range(0,num_of_problems,2):
        bob=bob+inputlist[i]
    for i in range(1,num_of_problems,2):
        alice=alice+inputlist[i]
if(alice>bob):
    print("Alice")
if(bob>alice):
    print("Bob")