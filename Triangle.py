# Lower Triangle
def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

# Example usage:
lower_triangular(5)

# Upper Triangle
def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage:
upper_triangular(5)

# Pyramid
def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Example usage:
pyramid(5)
