players = {}
answers = []

def one(x):
  if x not in players.keys():
    players[x] = 1
  else:
    players[x] += 1

def two(x):
  if x not in players.keys():
    players[x] = 2
  else:
    players[x] += 2

def three(x):
  if x in players.keys() and players[x] >= 2:
    return "Yes"
  else:
    return "No"

num, events = map(int, input().split(" "))

for i in range(0, events):
  event, person = map(int, input().split(" "))
  if event == 1:
    one(person)
  elif event == 2:
    two(person)
  elif event == 3:
    answers.append(three(person))

for ans in answers:
  print(ans)
