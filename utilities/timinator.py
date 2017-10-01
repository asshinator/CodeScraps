import sys
import timeit; 

#Construct the code block to execute the string.
stringerino = r'exec(open(r'
stringerino += "'"
stringerino += sys.argv[1]
stringerino += "'"
stringerino += r').read())'

#Print out the name of the script we're executing
print("ScriptName: "+sys.argv[1])
#Mention what the script outputs, so we can always use this.
print("Execution: ",end='')
out = exec(stringerino)
if type(out)!=type(None):
    print(str(out))
#mention Execution time.
print("Execution time over 100 runs:"+str(timeit.timeit(stringerino, number=100)))