# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# row2 = matrix[1]
# cell = row2[2]

# print(matrix[2][0])


def max_sum(matrix):
    result = [0, 0]

    for i in range(len(matrix)):
        row_length = len(matrix[i])
        sum_numbers = 0

        for j in range(row_length):
            sum_numbers += matrix[i][j]
        
        if sum_numbers > result[0]:
            result[0] = sum_numbers
            result[1] = i + 1
    
    return result


def sum_matrixies(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix

def create_matrix(rows, cols):
    return [[None for _ in range(cols)] for _ in range(rows)]

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Неправильный ввод")
        return

    result_matrix = create_matrix(len(matrix1), len(matrix2[0]))

    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[0])):
            sum_multiplies = 0

            for k in range(len(matrix1[0])):
                sum_multiplies += matrix1[i][k] * matrix2[k][j]

            result_matrix[i][j] = sum_multiplies

    return result_matrix

def sum_diagonals_matrix(matrix):
    sum_diagonals = 0

    # прямая диагональ
    for i in range(len(matrix)):
        sum_diagonals += matrix[i][i]

    # обратная диагональ
    for i in range(len(matrix)):
        sum_diagonals += \
            matrix[i][len(matrix) - i - 1]

    return sum_diagonals

empty_field = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1],
]

draw_field = [
    [1, 0, 1],  
    [1, 1, 0],   
    [0, 1, 0],   
]

O_winer = [
    [0, 1, -1],
    [1, 0, -1],
    [-1, 1, 0],
]

X_winer = [
    [-1, 0, 1],
    [-1, 1, 0],
    [1, -1, -1],
]

# res = multiply_matrices(input_matrix, input_matrix2)
# print(res)

# res = create_matrix(4, 8)
# print(res)

# res = sum_matrixies(input_matrix, input_matrix)
# print(res)

# res = max_sum(input_matrix)
# print(res)
