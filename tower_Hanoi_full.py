"""

This is a program to show the solution
to the towers of hanoi problem.

"""

from turtle import *


SPEED = 2




class disc(Turtle):
    def __init__(self, num):
        Turtle.__init__(self, shape = 'square', visible = False)
        self.pu()
        self.shapesize(1.5,num*1.5,2) ##making the square a rectangle
        self.fillcolor(num/n, 0, 1 - num/n )
        self.st()
        self.speed(SPEED)

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self,x):
        "create an empty tower. x is x-position of peg"
        self.x = x
        
    def push(self, d):
        d.setx(self.x)
        d.sety(-150 +34*len(self))
        self.append(d)

    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d


def towers_hanoi( num, source, destination, extra):
    """
        num -> int: number of disks
        source -> Tower object: starting peg (leftmost peg)
        destination -> Tower object: ending peg (rightmost peg)
        extra -> Tower object: middle peg ( auxiliary peg)

        function:
            find the n - 1 solution and then back propagate it
            to solve the problem.

        output:
            none
    """
    ##base case
    if num > 0:
        ##recursive call, solviog n-1 case
        towers_hanoi( num-1, source, extra, destination )
        ##moving disks from source location to destination
        destination.push( source.pop() )
        
        towers_hanoi( num-1, extra, destination, source )


def play():

    try:
        towers_hanoi( n, t_source, t_dest, t_aux )

    except Terminator:
        #closing the program
        exitonclick()




def main():
    global t_source, t_dest, t_aux
    global n
    n = int(input('Enter number of disks: '))
    ht(); penup(); goto(0, -225)
    
    t_source = Tower(-250)
    t_aux = Tower(0)
    t_dest = Tower(250)

    title('Towers of Hanoi simulated solution')

    #create the stack of disks of size n
    for i in range(n, 0, -1):
        t_source.push(disc(i))

    return "EVENTLOOP"

if __name__ == '__main__':
    main()
    play()
    done()
