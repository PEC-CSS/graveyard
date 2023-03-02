def sort_stack(S):
    if len(S) > 0:
        temp = S.pop()
        sort_stack(S)
        insert_in_sorted_order(S, temp)
 
def insert_in_sorted_order(S, element):
    if len(S) == 0 or S[-1] < element:
        S.append(element)
    else:
        temp = S.pop()
        insert_in_sorted_order(S, element)
        S.append(temp)
def reverse_stack(S):
    if len(S) > 0:
        temp = S.pop()
        reverse_stack(S)
        insert_at_bottom(S, temp)
def insert_at_bottom(S, element):
    if len(S) == 0:
        S.append(element)
    else:
        temp = S.pop()
        insert_at_bottom(S, element)
        S.append(temp)
# First I have arranged the stack in increasing order and then reversed it to get the answer in decreasing order
S = [5, 3, 8, 1, 2]
print("Stack before sorting:", S)
sort_stack(S)
reverse_stack(S)
print("Stack after sorting:", S)
