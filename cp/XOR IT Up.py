def func(lis):
    answer=lis[0]^lis[1]
    for i in range(2,len(lis)):
        answer=answer^lis[i]
    return answer

no_of_testcases=int(input())
dictionary=dict()
for i in range(no_of_testcases):
    length=int(input())
    arri=list(map(int,input().split()))
    dictionary.update({i:arri})
for i in range(no_of_testcases):
    combined_array=dictionary[i]
    for j in range(len(combined_array)):
        x = combined_array.pop(j)
        if(func(combined_array)==x):
            print(x)
            break
        else:
            combined_array.insert(j,x)