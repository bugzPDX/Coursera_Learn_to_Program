
from TurtleWorld import *


world = TurtleWorld()
bob = Turtle()
print(bob)
def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)

    wait_for_user()
#square(bob,125)



def polygon(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t,360/n)

    wait_for_user()
    
#polygon(bob,55,8)


def circle(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t,360/n)

    wait_for_user()
    
circle(bob,5,160)
