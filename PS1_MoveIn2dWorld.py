colors = [['red', 'green', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7
# sensor_right = 1.0

p_move = 0.8
# p_move = 1.0


def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

size_p = len(colors)*len(colors[0])
p = [[1.0/size_p for i in range(0, len(colors[j]))] for j in range(0, len(colors))]
print p


def sense(p, Z):
    s = 0.0
    temp = [[0.0 for i in range(len(p[0]))] for j in range(len(p))]
    for j in range(len(p)):
        for i in range(len(p[j])):
            hit = (Z == colors[j][i])
            temp[j][i] = p[j][i] * (hit * sensor_right + ((1-hit) * (1-sensor_right)))
            s += temp[j][i]
    for j in range(len(p)):
        for i in range(len(p[j])):
            temp[j][i] /= s
    return temp


def move(p, U):
    temp = [[0.0 for i in range(len(p[0]))] for j in range(len(p))]
    for j in range(len(p)):
        for i in range(len(p[j])):
            s = p_move * p[j-U[0] % len(p)][(i-U[1]) % len(p[j])]
            #Cannot overshoot
            #s = s + pOvershoot * p[(i-U-1) % len(p)]
            s = s + (1-p_move) * p[j][i]
            temp[j][i] = s

    return temp

for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])
#Your probability array must be printed
#with the following code.
show(p)
