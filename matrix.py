def print_matrix(array):  
    while array !=[]:    
        print "%s\n" % array[:N]        
        array = array[N:]
        
print ("Input size of a matrix N x N: ")

matrix_size = int(raw_input("Size of matrix: >"))

matrix_array = []
   
print ("You want to creat a matrix of %d x %d") %(matrix_size, matrix_size)
    
input_array = raw_input("Enter number array of the matrix each number is seperated by a space: \n>")

N = matrix_size

words = input_array.split(" ")

for i in words:
    matrix_array.append(i)
    
print matrix_array 

# part a
sum = 0
for i in range(N):
    for j in range(N):
        if i==j:
            sum += int(matrix_array[(i)*(j+N)])
print sum

sum = 0
for i in range(N):
    for j in range(N):
        if i==j:
            sum += int(matrix_array[((i+1)*(j+N) - N - 1)])
print sum
 
print_matrix(matrix_array)

# part b    
out_matrix = []           
for i in words:
    if ((int(i) % 2) == 0) and (int(i) > 0):        
        out_matrix.append(i)
    else:
        out_matrix.append("x")
print_matrix(out_matrix)                    
