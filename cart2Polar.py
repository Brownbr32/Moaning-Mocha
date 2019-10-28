import math

x  = input('x: ')
y  = input('y: ')
x  = float(x)
y  = float(y)
m  = abs(math.sqrt(x*x+y*y))
t1 = math.acos(x/m)
t2 = math.asin(y/m)

if((math.cos(t1) - x/m < .001) and (math.sin(t1) - y/m <.001) and (math.cos(t1) - x/m > -.001) and (math.sin(t1) - y/m > -.001)):
    t = t1
else:
    t = t2

print("")
print("m      = {}".format(m))
print("t      = {}".format(t))
print("cos(t) = {}".format(m*math.cos(t)))
print("sin(t) = {}".format(m*math.sin(t)))