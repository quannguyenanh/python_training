from __future__ import print_function
import math
 
def create_matrix(size, array):
    square_matrix = []
    k = 0
    for i in range(size):  
        square_matrix.append([])
        for j in range(size):
            square_matrix[i].append(int(array[k]))
            k += 1
    return square_matrix    
		
matrix_array = []

input_array = raw_input("Enter number array of the matrix each number is seperated by a space: \n>")

words = input_array.split(" ")

N = int(math.sqrt(len(words)))

print (words)

matrix = create_matrix(N, words)
          
# part a
sum = 0
for i in range(N):
    sum += int(matrix[i][i])
print (sum)

sum = 0

for i in range(N):
    sum += int(matrix[N-i-1][i])
print (sum)
 
# part b    
for i in range(N):
    for j in range(N):
        if ((matrix[i][j] % 2) == 0) and (matrix[i][j] > 0):        
            pass
        else:
            matrix[i][j] = "x"
        print('{0:>4}'.format(str(matrix[i][j])), end='')
    print("")                      
