from functions import print_square, sequence, create_3by3
import pandas as pd

r1 = [x for x in range(1, 10)]
r2 = [4, 5, 6, 7, 8, 9, 1, 2, 3]
r3 = [7, 8, 9, 1, 2, 3, 4, 5, 6]
r4 = [2, 3, 4, 5, 6, 7, 8, 9, 1]
r5 = [5, 6, 7, 8, 9, 1, 2, 3, 4]
r6 = [8, 9, 1, 2, 3, 4, 5, 6, 7]
r7 = [3, 4, 5, 6, 7, 8, 9, 1, 2]
r8 = [6, 7, 8, 9, 1, 2, 3, 4, 5]
r9 = [9, 1, 2, 3, 4, 5, 6, 7, 8]

square = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

frame = pd.DataFrame(square)

print_square(frame)


seq1 = sequence(9)
print(create_3by3(seq1))

