import java.math.BigDecimal as bd
import random

# engine : this variable is defined and set by the groovy shim wrapper.

x = []
y = []
dx = []
dy = []
c = []

for i in range(0, 10):
    x.append(random.randint(0, 230))
    y.append(random.randint(0, 150))
    dy.append(1)
    dx.append(-1)
    c.append(random.randint(12, 30))

def create():
    print "Python Success"
#

def update(delta):
    global x, y, dx, dy

    for i in range(0, 10):
        if(x[i] < 0):
            dx[i] = 1

        if(x[i] > 230):
            dx[i] = -1

        if(y[i] < 0):
            dy[i] = 1

        if(y[i] > 150):
            dy[i] = -1

        x[i] = x[i] + dx[i]
        y[i] = y[i] + dy[i]
#

def render():
    for i in range(0, 10):
        engine.setColor(c[i])
        engine.fillRect(bd(x[i]), bd(y[i]), bd(10), bd(10))
#
