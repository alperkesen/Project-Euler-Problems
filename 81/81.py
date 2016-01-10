#! /usr/bin/env python
# coding: utf-8

matrix_txt = open("p081_matrix.txt")
matrix_read = matrix_txt.read()
matrix = [rows.split(",") for rows in matrix_read.split("\n")]

matrix_size = range(len(matrix))

for x in matrix_size:
	for y in matrix_size:
		if x == 0 and y == 0:
			pass
		elif x == 0:
			matrix[x][y] = int(matrix[x][y]) + int(matrix[x][y-1])
		elif y == 0:
			matrix[x][y] = int(matrix[x][y]) + int(matrix[x-1][y])
		else:
			if matrix[x-1][y] < matrix[x][y-1]:
				matrix[x][y] = int(matrix[x][y]) + int(matrix[x-1][y])			
			elif matrix[x][y-1] < matrix[x-1][y]:
				matrix[x][y] = int(matrix[x][y]) + int(matrix[x][y-1])
			else:
				matrix[x][y] = int(matrix[x][y]) + int(matrix[x-1][y])

print matrix[79][79]