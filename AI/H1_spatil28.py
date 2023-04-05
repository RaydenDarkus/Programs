# Shreyas Patil
# G01382371
# Trying A* algorithm implementation using pyamaze module and Priority Queue
# Homework 1 CS580

#importing the modules

from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue

#It is the manhattan distance from the goal cell to the current cell
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x2-x1) + abs(y2-y1))
    
def aStar(m,start=None):

    # start variable is a tuple which represents cell 10,10 in this case
    start=(10,10)
    open = PriorityQueue()
    open.put((h(start, (1,1)), h(start, (1,1)), start))
    aPath = {}
    #It is the Euclidean distance from the start cell
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    #It is the Manhattan distance from the goal cell
    h_score = {cell: float('inf') for cell in m.grid}
    h_score[start] = h(start, (1,1))
    #start is in searchpath initially but add different cells later
    searchPath=[start]

    while not open.empty():
        #Remove all the neighbouring cells out of the queue
        currCell = open.get()[2]
        searchPath.append(currCell)
        #If Current Cell is the goal then stop
        if currCell == (1,1):
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_h_score = temp_g_score + h(childCell, (1,1))

                if temp_h_score < h_score[childCell]:   
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    h_score[childCell] = temp_g_score + h(childCell,(1,1))
                    open.put((h_score[childCell], h(childCell, (1,1)), childCell))

    #The path is stored in backwards, so we need to change it
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath


#rows and cols must are variables, so factual values are needed to avoid errors
if __name__=='__main__':
    rows,cols = 10,10
    m=maze(rows,cols)
    #Create a random maze with more than one path as loop percent is 20
    m.CreateMaze(loopPercent=20,theme=COLOR.light)

    searchPath,aPath,fwdPath=aStar(m)

    # Fill the path and add footprints, shape='arrow' for movement in arrow 
    a=agent(m,footprints=True,color=COLOR.blue,filled=True,shape='arrow')
    #The goal sets back to the start state
    b=agent(m,1,1,footprints=True,color=COLOR.red,filled=True,goal=(10,10))
    c=agent(m,footprints=True,color=COLOR.green)

    m.tracePath({a:searchPath},delay=100)
    m.tracePath({b:aPath},delay=100)
    m.tracePath({c:fwdPath},delay=100)

    #Display the cost of the solution in the box above the maze
    l=textLabel(m,'A Star Path Length',len(fwdPath)+1)
    l=textLabel(m,'A Star Search Length',len(searchPath))

    #It tells the closed and open walls of each cell in the maze at all coordinates
    print(m.maze_map)
    m.run()

#     PS D:\Documents\MS-2nd Sem\AI> & D:/Python/python.exe "d:/Documents/MS-2nd Sem/AI/new1.py"
# {(1, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0}, (2, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, 
#  (3, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (4, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (5, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, 
#  (6, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (7, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (8, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, 
#  (9, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (10, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0}, (1, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, 
#  (2, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (3, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (4, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, 
#  (5, 2): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (6, 2): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (7, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 0}, 
#  (8, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (9, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (10, 2): {'E': 0, 'W': 1, 'N': 1, 'S': 0},
#  (1, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 3): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, (3, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, 
#  (4, 3): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (5, 3): {'E': 0, 'W': 0, 'N': 1, 'S': 0}, (6, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, 
#  (7, 3): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (8, 3): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, (9, 3): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, 
#  (10, 3): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (1, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 4): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
#  (3, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (4, 4): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (5, 4): {'E': 1, 'W': 0, 'N': 0, 'S': 1},
#  (6, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (7, 4): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (8, 4): {'E': 1, 'W': 0, 'N': 1, 'S': 1},
#  (9, 4): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, (10, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (1, 5): {'E': 1, 'W': 1, 'N': 0, 'S': 0},
#  (2, 5): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (3, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, (4, 5): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, 
#  (5, 5): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (6, 5): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (7, 5): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, 
#  (8, 5): {'E': 0, 'W': 1, 'N': 0, 'S': 0}, (9, 5): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (10, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, 
#  (1, 6): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (2, 6): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (3, 6): {'E': 0, 'W': 0, 'N': 1, 'S': 0}, 
#  (4, 6): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (5, 6): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (6, 6): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, 
#  (7, 6): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (8, 6): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (9, 6): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, 
#  (10, 6): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (1, 7): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, (2, 7): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, 
#  (3, 7): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (4, 7): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (5, 7): {'E': 0, 'W': 0, 'N': 1, 'S': 0}, 
#  (6, 7): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (7, 7): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (8, 7): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, 
#  (9, 7): {'E': 0, 'W': 1, 'N': 0, 'S': 0}, (10, 7): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (1, 8): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, 
#  (2, 8): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (3, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (4, 8): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, 
#  (5, 8): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (6, 8): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (7, 8): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, 
#  (8, 8): {'E': 1, 'W': 0, 'N': 1, 'S': 1}, (9, 8): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (10, 8): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, 
#  (1, 9): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (2, 9): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (3, 9): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, 
#  (4, 9): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (5, 9): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (6, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, 
#  (7, 9): {'E': 0, 'W': 1, 'N': 0, 'S': 0}, (8, 9): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (9, 9): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, 
#  (10, 9): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, (1, 10): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (2, 10): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, 
#  (3, 10): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (4, 10): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (5, 10): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, 
#  (6, 10): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (7, 10): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (8, 10): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, 
#  (9, 10): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (10, 10): {'E': 0, 'W': 0, 'N': 1, 'S': 0}}
