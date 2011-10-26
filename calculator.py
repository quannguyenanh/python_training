from sys import argv

def add():
    print (int(argv[1]) + int(argv[3]))
def sub():
    print (int(argv[1]) - int(argv[3]))
def mul():
    print (int(argv[1]) * int(argv[3]))         
def div():
    print (int(argv[1]) / int(argv[3]))
def mod():
    print (int(argv[1]) % int(argv[3]))    
for i in argv:
    print i
if argv[2] == "+":
    add()
elif argv[2] == "-":
    sub()
elif argv[2] == "*":
    mul()
    #print argv[2]
    print "Special case, here * is not known as multiply symbol should use \* instead, FTW"
elif argv[2] == "/":
    div()            
elif argv[2] == "%":
    mod()
else:
    print "Express error!"        
    
                
