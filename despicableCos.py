import math

m = input('Please give a magnitude:\t')
m = float(m)
xpos = 0
ypos = 0
while(m != 0):
    t = input('Please give a phase (rad):\t')
    t2 = t.split('*')
    i = 0

    tmp = 1
    for item in t2:
        if item == 'pi':
            tmp *= math.pi
        else:
            tmp *= float(item)
    xpos += m*math.cos(tmp)
    ypos += m*math.sin(tmp)
    m = input('Please give a magnitude:\t')
    m = float(m)





print("\nx = {}".format(xpos))
print("y = {}".format(ypos))

x  = xpos
y  = ypos
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
print("t/pi   = {}".format(t/3.14159265358979))
print("cos(t) = {}".format(m*math.cos(t)))
print("sin(t) = {}".format(m*math.sin(t)))



# print("\n{}sin({}) = {}".format(m,t,m*math.sin(tmp)))
# print("{}cos({}) = {}".format(m,t,m*math.cos(tmp)))