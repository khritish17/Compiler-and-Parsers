# First we take input from the user
print("Input your expressions containing '<' or '>':")
inp=input()
#print(len(inp))
degree=0
symbol_count=0
largest_prefix=0

for symb in  inp:
    symbol_count+=1
    if degree>=0:
        if symb=='>':
            degree-=1
            if(degree==0):
                largest_prefix=symbol_count
        if symb=='<':
            degree+=1
    else:
        break

print("Largest Prefix:{}".format(largest_prefix))
if degree==0:
    print("Succesfuly compiled, no error.")
else:
    print("Syntax Error,'{}' is not a valid expression".format(inp))

