from basic.Matrix import Matrix

matrix = Matrix()

formatted_mat = matrix.format((3,3), [1,2,3,5,3,6,7,4,9])
# [1,5,7,2,3,4,3,6,9]
matrix.display(formatted_mat)

# matrix.row_echelon_form(formatted_mat)
print(matrix.transpose(formatted_mat))