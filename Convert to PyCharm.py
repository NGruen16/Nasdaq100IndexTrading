import pandas
import pandas as pd

df = pd.read_csv("Scrap.csv")
list = []
list2 = df.Numbers
for i in list2:
    list.append(i)

print(list)