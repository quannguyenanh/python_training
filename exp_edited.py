from sys import argv

if len(argv) != 3:
    runtimError
else:
    pass
    
X = float(argv[2])

def ham_mu(N):
    def calculate_exp(X):
        val = 1    
        for i in range(N):
            val *= X
        return val
    return calculate_exp                   
    
command = argv[1]
 
words = command.split("_")

# get exp 
exp = int(words[-1])

command = ham_mu(exp)

print "Ham mu :", command(X)
