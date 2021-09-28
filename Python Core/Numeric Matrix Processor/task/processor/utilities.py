import inflect

p = inflect.engine()


def get_matrices(n):
    matrices = []
    ordinals = [p.number_to_words(p.ordinal(ordinal)) for ordinal in range(1, n + 1) if n > 1]
    for k in range(n):
        good_input = False
        dims = []
        print(f'Enter size of {ordinals[k]} matrix:' if n > 1 else 'Enter size of matrix:', end=' ')
        while not good_input:
            dims += [int(dim) for dim in input().split()]
            if len(dims) == 2:
                good_input = True

        good_input = False

        values = []
        print(f'Enter {ordinals[k]} matrix:' if n > 1 else 'Enter matrix:')
        while not good_input:
            values += [float(val) for val in input().split()]
            if len(values) == dims[0] * dims[1]:
                good_input = True

        values = [int(val) if int(val) == float(val) else float(val) for val in values]
        matrix = []
        for i in range(dims[0]):
            row = []
            for j in range(dims[1]):
                row.append(values[i * dims[1] + j])
            matrix.append(row)
        matrices.append(matrix)
    return matrices


def matrix_sum(mat_1, mat_2):
    n_1 = len(mat_1)
    m_1 = len(mat_1[0])
    n_2 = len(mat_2)
    m_2 = len(mat_2[0])
    if n_1 != n_2 or m_1 != m_2:
        return False
    else:
        result = []
        for i in range(n_1):
            row = []
            for j in range(m_1):
                row.append(mat_1[i][j] + mat_2[i][j])
            result.append(row)
        return result


def matrix_to_str(mat):
    result = ''
    for row in mat:
        result += ' '.join([f'{int(val) if int(val) == float(val) else float(val)}' for val in row]) + '\n'
    return result


def scalar_multiplication(mat, scal):
    result = []
    for row in mat:
        result_row = []
        for val in row:
            result_row.append(val * scal)
        result.append(result_row)
    return result


def matrix_multiplication(mat_1, mat_2):
    n_1 = len(mat_1)
    m_1 = len(mat_1[0])
    n_2 = len(mat_2)
    m_2 = len(mat_2[0])
    if m_1 != n_2:
        return False
    else:
        product = []
        for i in range(n_1):
            row = []
            for j in range(m_2):
                element = 0
                for k in range(m_1):
                    element += mat_1[i][k] * mat_2[k][j]
                row.append(element)
            product.append(row)
        return product


def transpose_main(mat):
    m, n = len(mat), len(mat[0])
    result = [m * [0] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][i] = mat[i][j]
    return result


def transpose_side(mat):
    m, n = len(mat), len(mat[0])
    result = [m * [0] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[n - j - 1][m - i - 1] = mat[i][j]
    return result


def transpose_vertical(mat):
    m, n = len(mat), len(mat[0])
    result = [n * [0] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][n - j - 1] = mat[i][j]
    return result


def transpose_horizontal(mat):
    m, n = len(mat), len(mat[0])
    result = [n * [0] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[m - i - 1][j] = mat[i][j]
    return result


def determinant(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    else:
        result = 0
        for k in range(n):
            minor = []
            for i in range(1, n):
                for j in range(n):
                    if j != k:
                        minor.append(mat[i][j])
            right = n - 1
            minor = [minor[left:left + right] for left in range(0, right ** 2, right)]
            result += mat[0][k] * determinant(minor) * (-1) ** k
        return result


def inverse(mat):
    n = len(mat)
    det = determinant(mat)
    result = False
    if det != 0:
        cofactors = []
        for i in range(n):
            for j in range(n):
                minor = []
                for k in range(n):
                    for l in range(n):
                        if k != i and l != j:
                            minor.append(mat[k][l])
                right = n - 1
                minor = [minor[left:left + right] for left in range(0, right ** 2, right)]
                cofactors.append(determinant(minor) * (-1) ** (i + j))
        right = n
        result = [val / det for val in cofactors]
        result = [result[left:left + right] for left in range(0, right ** 2, right)]
        result = transpose_main(result)
    return result
