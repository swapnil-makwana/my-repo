def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n_terms = 10
print("Fibonacci sequence up to", n_terms, "terms:")
print(fibonacci(n_terms))
