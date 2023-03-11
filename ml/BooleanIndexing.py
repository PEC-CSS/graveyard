import numpy as np

names = np.array(["Roxana", "Statira", "Roxana", "Statira", "Roxana"])
score = np.array([126, 115, 130, 141, 132])

scores_lt_130 = score[score < 130]
print(scores_lt_130)


scores_statira = score[names == "Statira"]
print(scores_statira)

roxana_scores = score[names == "Roxana"]
roxana_scores += 10
score[names == "Roxana"] = roxana_scores
print(roxana_scores)
