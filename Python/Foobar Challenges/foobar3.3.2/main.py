def solution(m):
    matrix = list(m)
    for i, item in enumerate(matrix):
        item[i] = 0
    sums = [sum(i) for i in matrix]
    terminal_states = [i for i, item in enumerate(sums) if item == 0]
    non_terminal_states = list((set(range(len(m))) - set(terminal_states)))

    for i in range(0, len(non_terminal_states) - 1):
        index1 = non_terminal_states[len(non_terminal_states) - i - 1]
        for j in range(0, len(non_terminal_states) - 1):
            index2 = non_terminal_states[j]
            matrix[index2] = combine(matrix[index2], index2, matrix[index1], index1)
    solution = []
    for i in terminal_states:
        solution.append(matrix[0][i])
    tot = sum(solution)
    solution.append(tot)
    if tot == 0:
        solution = [1 for i in terminal_states]
        solution.append(len(terminal_states))
    return solution

def greatest_common_divisor(number1, number2):
    if number2 == 0:
        return number1
    else:
        return greatest_common_divisor(number2, number1 % number2)


def list_of_greatest_common_divisors(lst):
    out = 0
    for i in range(0, len(lst)):
        out = greatest_common_divisor(out, lst[i])
    return out


def combine(v1, i1, v2, i2):
    length = len(v1)
    indexes = (set(range(length)) - {i1, i2})
    sum2 = sum(v2)
    out = [0 for i in v1]
    for i in indexes:
        out[i] = sum2 * v1[i] + v1[i2] * v2[i]
    gc = list_of_greatest_common_divisors(out)
    solution = [int(i / gc) for i in out]
    return solution





print solution([[0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])

print solution([[0, 0, 0, 0, 0],
                [0, 2, 1, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])
