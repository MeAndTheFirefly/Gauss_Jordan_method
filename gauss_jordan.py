import numpy as np

#matrix = np.array([[1, 1, 1, 5], [2, 3, 5, 8], [4, 0, 5, 2]], dtype=float)
#matrix = np.array([[1, 2, -3, 2], [6, 3, -9, 6], [7, 14, -21, 13]], dtype=float)
matrix = np.array([[2, 6, -2, 3], [4, 8, -5, 4], [0, 4, 1, 2]], dtype=float)


def obtain_echelon_form(m):
    i = 0
    j = 0
    while i < len(m) - 1:
        while j < len(m) - 1:
            if m[j + 1][i] == 0.0:
                break
            else:
                # m[j+1] -= m[j+1][i] / m[i][i] * m[i]
                m[j + 1] = m[j + 1] * m[i][i] - m[i] * m[j + 1][i]
                j += 1
        i += 1
        j = i
    return m


def reduced_echelon_form(m):
    i = len(m) - 1
    j = len(m) - 1

    obtain_echelon_form(m)

    if not detect_non_solution(m) and not detect_infinite_solutions(m):
        m[len(m) - 1] /= m[len(m) - 1][m.shape[1] - 2]
        while i > 0:
            while j > 0:
                m[j - 1] = m[j - 1] * m[i][i] - m[i] * m[j - 1][i]
                j -= 1
            i -= 1
            j = i
    elif detect_non_solution(m):
        print("This matrix has no solutions")

    elif detect_infinite_solutions(m):
        print("This matrix has many solutions")
    return m


def detect_non_solution(m):
    return any(np.array_equal(row[:m.shape[1] - 1], [0.] * (m.shape[1] - 1)) and row[m.shape[1] - 1] != 0 for row in m)


def detect_infinite_solutions(m):
    return any(np.array_equal(row[:m.shape[1]], [0.] * (m.shape[1])) for row in m)


print(reduced_echelon_form(matrix))







