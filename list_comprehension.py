#!/usr/bin/python3

square = [ i*i for i in range(10)]

print(square)

matrix_sq = [[j * j for j  in range (3)] for i in range(10)]

print(matrix_sq)

"""Nested list comprehension"""

matrix = [[ j for j in range (3)] for i in range (5)]

print(matrix)

matrix3x3 = [[ j for j in range (3)] for i in range(3)]
print(matrix3x3)
