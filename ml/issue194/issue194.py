# %% [markdown]
# #issue 194
# 

# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
path1 = 'test.csv'

# %%
data = pd.read_csv(path1,usecols=['Age','Sex'])
#data.head()

# %%
dm = data[data['Sex'] == 'male']
#dm.head()

# %%
df = data[data['Sex'] == 'female']
#print(df)

# %%
plt.style.use('dark_background')
bins = [i*10 for i in range(11)]
plt.hist(dm['Age'],bins = bins, edgecolor ='white')
plt.title('Ages of male passengers')
plt.xlabel('Ages')
plt.ylabel('Total passengers')
plt.show()

# %%
plt.hist(df['Age'],bins = bins, edgecolor ='white')
plt.title('Ages of female passengers')
plt.xlabel('Ages')
plt.ylabel('Total passengers')
plt.show()

