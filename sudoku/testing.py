from functions import random_number
import pandas as pd

a = pd.Series([0,0,0,4,5,6,0,0,0])
b = pd.Series([1,2,3,0,0,0,0,0,0])


for i in range(50):
    print(random_number(a, b), sep=" ")


print(a)
print(b)
