import math

x = 0
y = 0
m = input('Please give a magnitude:\t')
while (m != "q"):
    m = float(m)
    t = input('Please give a phase (rad):\t')
    t2 = t.split('*')
    i = 0

    tmp = 1
    for item in t2:
        if item == 'pi':
            tmp *= math.pi
        else:
            tmp *= float(item)
    x += m*math.cos(tmp)
    y += m*math.sin(tmp)
    m = input('Please give a magnitude:\t')

m = abs(math.sqrt(x*x+y*y))
t1 = math.acos(x/m)
print("X = {}".format(x))
print("Y = {}".format(y))
print("m = {}".format(m))
print("t = {}*pi".format(t1/math.pi))
#print("\n{}*sin({}) = {}".format(int(m),t,m*math.sin(tmp)))
#print(  "{}*cos({}) = {}".format(int(m),t,m*math.cos(tmp)))