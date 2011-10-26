from sys import argv

X = 5

def ham_mu(N):    
    return (X**N)    
    
command = argv[1]
 
words = command.split("_")

# get exp 
exp = int(words[-1])

x = ham_mu(exp)
print x