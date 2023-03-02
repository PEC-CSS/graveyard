def gascheck(j, counter, remaining_gas, cost_for_next_station,n):
    if (counter == n):
        return 106
    elif (remaining_gas >= cost_for_next_station):
        j = j + 1
        if (j >= n):
            j = j - n
        remaining_gas = gas[j] + remaining_gas - cost_for_next_station
        cost_for_next_station = cost[j]
        counter = counter + 1
        if((gascheck(j, counter, remaining_gas, cost_for_next_station,n))==106):
            return 106
gas = list(map(int, input()))
cost = list(map(int, input()))
n = len(gas)
index = -1
for i in range(n):
    if (gascheck(i, 0, gas[i], cost[i],n) == 106):
        index = i
        break
print(index)