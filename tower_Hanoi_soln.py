"""
Towers of Hanoi Solver
solved using recursion

USE turtle and tkinter to show solution graphically
"""

def towers_of_hanoi(num, source, destination, auxiliary):
    if num == 1:
        print( "Move disk 1 from source", source, "to destination",
               destination )
        return

    towers_of_hanoi( num-1, source, auxiliary, destination )
    
    print( "Move disk", num, "from source", source,
           "to destination", destination)
    
    towers_of_hanoi( num-1, auxiliary, destination, source )


n = 3
#A, C, B are the names of the rod
towers_of_hanoi(n, 'A', 'C', 'B')
