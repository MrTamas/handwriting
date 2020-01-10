import pandas as pd
from random import randrange, choice


diagonal_list = [(0, 0), (0, 1), (0, 2),
                 (1, 0), (1, 1), (1, 2),
                 (2, 0), (2, 1), (2, 2),
                 (3, 3), (3, 4), (3, 5),
                 (4, 3), (4, 4), (4, 5),
                 (5, 3), (5, 4), (5, 5),
                 (6, 6), (6, 7), (6, 8),
                 (7, 6), (7, 7), (7, 8),
                 (8, 6), (8, 7), (8, 8)]


def print_square(df):
    for i in range(9):
        for j in range(9):
            if j == 8:
                print(df.iloc[i, j], end="\n")
            elif j % 3 == 2:
                print(df.iloc[i, j], end=" | ")
            else:
                print(df.iloc[i, j], end="   ")
        if i == 8:
            print()
        elif i % 3 == 2:
            print(10*'-', 11*'-', 11*'-', sep=' ', end='\n')
        else:
            pass  # print('\n')


def random_number(seq1, seq2):
    num = randrange(1, 10)
    if (num in seq1) or (num in seq2):
        num = random_number(seq1, seq2)
    return num


def random_number2(seq1, seq2):
    num = randrange(1, 10)
    if (num in seq1) or (num in seq2):
        return num, True
    else:
        return num, False


def check_contains(num, seq1, seq2):
    return (num in seq1) or (num in seq2)


def sequence(l):
    seq = []
    for i in range(l):
        r = random_number(seq, [0 for x in range(9)])
        seq.append(r)
    return seq


def create_3by3(seq):
    lists = []
    for i in range(0, 9, 3):
        lists.append(seq[i:i+3])
    df = pd.DataFrame(lists)
    return df


def fill_diagonal():
    df = pd.DataFrame([[0 for x in range(9)] for x in range(9)])
    for h in range(0, 9, 3):
        seq = sequence(9)
        box = create_3by3(seq)
        for i in range(0, 3):
            for j in range(0, 3):
                df.iloc[i + h, j + h] = box.iloc[i, j]
    return df


def fill_recursively(df, i, j):
    seq1 = list(df.iloc[i, :])
    seq2 = list(df.iloc[:, j])
    num = random_number2(seq1, seq2)
    return num


def fill_rest(df):
    for i in range(6):
        for j in range(6):
            if (i, j) not in diagonal_list:
                value = fill_recursively(df, i, j)
                df.iloc[i, j] = value
    return df


def fill_square(df, dim):
    options = [x for x in range(1, 10)]
    for i in range(dim[0], dim[1]):
        for j in range(dim[2], dim[3]):
            check = True
            op = options.copy()
            while check:
                seq1 = list(df.iloc[i, :])
                seq2 = list(df.iloc[:, j])
                num = choice(op)
                check = check_contains(num, seq1, seq2)
                # print(seq1, seq2, check, num, op, options)
                op.remove(num)
            df.iloc[i, j] = num
            options.remove(num)
    return df


"""
def random_number2(seq1, seq2, options):  # df, dim
    num = choice(options)
    if (num in seq1) or (num in seq2):
        options.remove(num)
        num = random_number2(seq1, seq2, options)
    return num
"""


"""
d = fill_diagonal()
print_square(d)
f = fill_rest(d)
print_square(f)
"""

def create_sudoku(counter):
    print(counter)
    try:
        a = fill_diagonal()
        b = fill_square(a, [3, 6, 0, 3])
        c = fill_square(b, [0, 3, 3, 6])
        d = fill_square(c, [6, 8, 3, 6])
        e = fill_square(d, [3, 6, 6, 8])
        f = fill_square(e, [6, 8, 0, 3])
        g = fill_square(f, [0, 3, 6, 8])
        print_square(g)
        print(counter)
    except IndexError:
        counter += 1
        create_sudoku(counter)


create_sudoku(0)
