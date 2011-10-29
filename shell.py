from sys import argv

input_file = "/etc/passwd"   
       
current_file = open(input_file)

def break_words(stuff):
    words = stuff.split(":")
    return words    

while True:
    line = current_file.readline()
    if not line:
        break
    words = break_words(line)
  
    if len(argv) < 2:
        print "%s -> :%s" %(words[0], words[-1])               
    else:
        if(argv[1] == words[0]): #(username != ' ') and
            print "Shell of user %s: %s" %(words[0],words[-1]) 
            break
            
current_file.close()            
