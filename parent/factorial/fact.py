def fact(n) -> int:
    solution = 1
    for i in range(n, 0, -1):
        solution *= i
    return solution