import sys
import numpy as np
from numpy.typing import NDArray
from common_classes import MathException

class Matrix:

    def __init__(self):
        pass

    def format(self, dimension : tuple, value_list : list[int]) -> NDArray:
        """
        Funtion to convert list of integers to ndarray based on dimensions 
        ^^^^^
        Args:
            dimension (tuple) : row and column length for ndarray
            value_list (list) : list of values for the ndarray
        
        Returns:
            NDArray : matrix of given dimension as ndarray
        """
        row,col = dimension

        if row*col != len(value_list):
            raise MathException.ValueMismatch("Number of rows or columns does not match with value list")
        
        nd_matrix = np.array(value_list, dtype=float)

        return nd_matrix.reshape(row,col)
    
    # def row_operation(self, operation, equation):
    #     return
    
    # def col_operation(self, operation, equation):
    #     return
    
    def is_ref(self, matrix : NDArray) -> bool:
        """
        Funtion to check whether a matrix is in Row Echelon Form (REF)
        ^^^^^
        Args:
            matrix (NDArray) : matrix to be checked
        
        Returns:
            bool : whether or not given matrix is in REF
        """
        pivot_list = []
        all_zero_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    pivot_list.append((i,j))
                    break
            if np.sum(matrix[i] == 0) == len(matrix[i]):
                all_zero_list.append(i) #rows containing only zeros

        pivot_row_list = [pivot_pos[0] for pivot_pos in pivot_list]
        pivot_col_list = [pivot_pos[1] for pivot_pos in pivot_list]

        # condition 1 : all zero rows are at the bottom
        # condition_1 = True
        for row_idx in all_zero_list:
            for pivot_idx in pivot_row_list:
                if row_idx < pivot_idx:
                    # condition_1 = False
                    return False
                    # break
            # if not condition_1:
            #     break

        # condition 2 : Pivots are to the right of ones in the previous row
        idx = 0
        while idx < (len(pivot_list)-1) :
            if pivot_list[idx] < pivot_list[idx+1] and pivot_list[idx][0] != pivot_list[idx+1][0] and pivot_list[idx][1] != pivot_list[idx+1][1]:
                # condition_2 = True
                pass
            else:
                # condition_2 = False
                return False
                # break

            idx+=1

        # condition 3 : zeros are below the pivot
        # condition_3 = True
        for i,j in pivot_list:
            idx = i+1
            while idx < len(matrix):
                if matrix[idx][j] != 0:
                    # condition_3 = False
                    return False
                    # break

                idx+=1
                

        return True
    
    def is_identity(self, matrix):
        
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if i == j:
                    if matrix[i][j] == 1:
                        pass
                    else:
                        return False
                else:
                    if matrix[i][j] == 0:
                        pass
                    else:
                        return False
                    
        return True
    
    def row_echelon_form(self, matrix : NDArray) -> NDArray:
        """
        Funtion to transform a matrix into Row Echelon Form (REF)
        ^^^^^
        Args:
            matrix (NDArray) : matrix to be transformed
        
        Returns:
            NDArray : transformed matrix
        """
        ref = self.is_ref(matrix)
        # ref_matrix = matrix[:] #create a copy of matrix
        counter = 0
        while not ref and counter < len(matrix):
            # perform row operations to make row echelon form

            i = counter
            while i < len(matrix):
                if matrix[i][counter] != 0:
                    matrix[i] = matrix[i] / matrix[i][counter]
                i+=1

            j = counter
            while j < len(matrix)-1:
                if np.sum(matrix[j+1] == 0) != len(matrix[j+1]):
                    matrix[j+1] = matrix[j+1] - matrix[counter]
                j+=1

            counter+=1
            print(matrix)
            ref = self.is_ref(matrix)
            # break
        return matrix

    def rank(self, matrix):
        if not self.is_ref(matrix):
            matrix = self.row_echelon_form(matrix)
        
        pivot_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    pivot_list.append((i,j))
                    break

        matrix_rank = len(pivot_list)

        return matrix_rank 
    
    def transpose(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        transpose_list = []

        for j in range(col):
            for i in range(row):
                transpose_list.append(matrix[i][j])

        transpose_matrix = self.format((col,row), transpose_list)
        # print(transpose_list)
        return transpose_matrix
    
    def inverse(self, matrix):
        
        return

    def eigen_value():
        return
    

    
    def multiply(self):

        return
    
    def add(self):

        return
    
    def subtract(self):

        return

    def display(self, matrix):
        for row in matrix:
            for col in row:
                print(col, end=" ")
            print()
        return
    # def divide()

if __name__  == "__main__":
    
    matrix = Matrix()

    formatted_mat = matrix.format((3,2), [1,2,3,5,3,6,7,4,9])

    matrix.display(formatted_mat)

    # matrix.row_echelon_form(formatted_mat)
    print(matrix.row_echelon_form(formatted_mat))
    # mat_rank = matrix.rank(formatted_mat)

    # print(mat_rank)
