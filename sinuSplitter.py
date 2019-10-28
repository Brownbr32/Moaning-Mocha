import math

def cos():
    print ("cos")

def sin():
    print ("sin")
funCall = {"cos":cos, "sin":sin}

arg = input('Please give the sinusoid to split: ')
print('')
arg = arg.split('(')
for i in range(0,len(arg)):
    arg[i] = arg[i].replace(')','')
#print (arg)
interior = arg[1].split('+')
sign = 1
if(len(interior) == 1):
    interior = interior[0].split('-')
    sign = -1
print(interior)
print(sign)
funCall.get(arg[0])()


