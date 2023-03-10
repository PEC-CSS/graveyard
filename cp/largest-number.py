def positional_yield(x):
  length = len(list(x))
  max = "9" * length
  score = int(x)/int(max)
  return score
  
def yield_map(lst):
  dct = {}
  for item in lst:
    vals = []
    vals.append(item)
    sc = positional_yield(item)
    if sc not in dct.keys():
      dct[sc] = vals
    else:
      dct[sc].append(item)
  return dct
  
def merge(map):
  temp = []
  order = sorted(map.keys())
  j = len(order)-1
  while j >= 0:
    temp.extend(map[order[j]])
    j -= 1
  return "".join(temp)

inp = input().strip("[").strip("]").split(",")
print(merge(yield_map(inp)))
