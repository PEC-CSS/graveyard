def merge_intervals(intervals):
    
    intervals.sort()

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

n = int(input())
intervals = []
for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])


result = merge_intervals(intervals)
print(result)
