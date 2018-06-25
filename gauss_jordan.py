import numpy as np

#matrix = np.array([[1, 1, 1, 5], [2, 3, 5, 8], [4, 0, 5, 2]], dtype=float)
#matrix = np.array([[1, 2, -3, 2], [6, 3, -9, 6], [7, 14, -21, 13]], dtype=float)
#matrix = np.array([[2, 6, -2, 3], [4, 8, -5, 4], [0, 4, 1, 2]], dtype=float)
#matrix = np.array([[0, 4, 1, 2], [2, 6, -2, 3], [4, 8, -5, 4]], dtype=float)


def echelon_form_forward(m):
    m = sort_array_de(m)
    i = 0
    j = 0
    while i < len(m) - 1:
        while j < len(m) - 1:
            if m[j + 1][i] == 0.0:
                j += 1
                continue
            else:
                m[j + 1] = m[j + 1] * m[i][i] - m[i] * m[j + 1][i]
                j += 1
        i += 1
        j = i
    return m


def echelon_form_backward(m):
    i = len(m) - 1
    j = len(m) - 1
    m = echelon_form_forward(m)

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


def sort_array_de(m):
    return m[m[:, 0].argsort()[::-1]]


def reduced_echelon_form(m):
    m = echelon_form_backward(m)
    for i in range(len(m) - 1):
        m[i] /= m[i][i]
    return m


print(reduced_echelon_form(matrix))








