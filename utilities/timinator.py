import sys
import timeit; 
if len(sys.argv) < 1:
    raise AssertionError("No Script specified to time!")
scriptToExecute = sys.argv[1]
numberOfIterations = int(sys.argv[2]) if len(sys.argv) > 2 else 100

if "timinator" not in scriptToExecute:
    #Construct the code block to execute the string.
    stringerino = r'exec(open(r'
    stringerino += "'"
    stringerino += scriptToExecute
    stringerino += "'"
    stringerino += r').read())'
    #Print out the name of the script we're executing
    print("ScriptName:\t"+sys.argv[1])
    #Mention what the script outputs, so we can always use this.
    print("PythonSnippet:\t"+stringerino)
    print("Execution:\t",end='')
    out = exec(stringerino)
    if type(out)!=type(None):
        print(str(out))
    #mention Execution time.
    print("Execution time over 100 runs:\t"+str(timeit.timeit(stringerino, number=numberOfIterations)))
else:
    print("timinator can't time itself. That's a conundrum!")
    