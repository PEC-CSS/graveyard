def tictactoe_board(list1,list2,list3,i):
    i=i+1
    if(i%2==0):
        n=int(input("x turn. Enter location in 1-9 where you want to enter:"))
        if (n == 1 or n == 2 or n == 3):
            list1[n-1]="x"
        if (n == 4 or n == 5 or n == 6):
            list2[n-4]="x"
        if (n == 7 or n == 8 or n == 9):
            list3[n-7]="x"
    elif(i%2!=0):
        n=int(input("o turn. Enter location in 1-9 where you want to enter:"))
        if (n == 1 or n == 2 or n == 3):
            list1[n-1]="o"
        if (n == 4 or n == 5 or n == 6):
            list2[n-4]="o"
        if (n == 7 or n == 8 or n == 9):
            list3[n-7]="o"
    print(list1[0], list1[1], list1[2], sep="")
    print(list2[0], list2[1], list2[2], sep="")
    print(list3[0], list3[1], list3[2], sep="")
    if ((list1[0] == list1[1] == list1[2] == "x") or (list2[0] == list2[1] == list2[2] == "x") or (
            list2[0] == list2[1] == list2[2] == "x") or (list1[0] == list2[0] == list3[0] == "x") or (
            list1[1] == list2[1] == list3[1] == "x") or (list1[2] == list2[2] == list3[2] == "x") or (
            list1[2] == list2[1] == list3[0] == "x") or (list1[0] == list2[1] == list3[2] == "x")):
        print("Player 2 Wins")
        return 2
    elif ((list1[0] == list1[1] == list1[2] == "o") or (list2[0] == list2[1] == list2[2] == "o") or (
            list2[0] == list2[1] == list2[2] == "o") or (list1[0] == list2[0] == list3[0] == "o") or (
            list1[1] == list2[1] == list3[1] == "o") or (list1[2] == list2[2] == list3[2] == "o") or (
            list1[2] == list2[1] == list3[0] == "o") or (list1[0] == list2[1] == list3[2] == "o")):
        print("Player 1 Wins")
        return 2
    elif(i==9):
        print("Draw")
        return 2
    if(tictactoe_board(list1, list2, list3, i)==2):
        return 2
list1=["-","-","-"]
list2=["-","-","-"]
list3=["-","-","-"]
print(list1[0],list1[1],list1[2],sep="")
print(list2[0],list2[1],list2[2],sep="")
print(list3[0],list3[1],list3[2],sep="")
i=0
tictactoe_board(list1,list2,list3,i)
