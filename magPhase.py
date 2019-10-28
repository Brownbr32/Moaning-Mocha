import math

m = input('Please give a magnitude:\t')
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
xpos = m*math.cos(tmp)
ypos = m*math.sin(tmp)



print("\n{}*sin({}) = {}".format(int(m),t,m*math.sin(tmp)))
print(  "{}*cos({}) = {}".format(int(m),t,m*math.cos(tmp)))