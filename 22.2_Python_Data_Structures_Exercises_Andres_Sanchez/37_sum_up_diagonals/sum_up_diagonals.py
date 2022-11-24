m1 = [
 [1,   2],
[30, 40],
]

m2 = [
 [1, 2, 3],
[4, 5, 6],
[7, 8, 9],
]

def sum_up_diagonals(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total


sum_up_diagonals(m1)
73

sum_up_diagonals(m2)
30





