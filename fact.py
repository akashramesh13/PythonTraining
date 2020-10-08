def fact(n):
    solution = 1
    for i in range(n, 0, -1):
        solution *= i
    return solution


if __name__ == "__main__":
    print("Hello from fact.py")