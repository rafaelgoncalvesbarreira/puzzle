from path_item import PathItem
from datetime import datetime
if __name__ == "__main__":
    import astar
    target = PathItem([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    start = PathItem([[1,2,3],[4,5,6],[0,7,8]]) #ok
    #start = PathItem([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) # ok 23
    #start = PathItem([[2, 8, 3], [1, 6, 4], [7, 0, 5]]) 
    #start = PathItem([[1,2,3],[4,0,5],[7,8,6]]) # ok
    #start = PathItem([[1, 2, 3], [0, 4, 5], [7, 8, 6]]) #ok
    #start = PathItem([[1, 2, 3], [6, 0, 8], [5, 4, 7]]) #ok 11
    #start = PathItem([[7, 2, 4 ], [5, 0, 6], [8, 3, 1]] ) # ok 21
    #start=PathItem( [[6, 4, 7], [8, 5, 0], [3, 2, 1]]  ) # =(
    #start = PathItem([[7, 2, 4], [5, 0, 6], [8, 3, 1]] )
    print("starting...")
    t1 = datetime.now()
    steps = astar.resolve(start,target)
    t2 = datetime.now()
    
    for step in steps:
        print(step.board)
    print("end with {0} steps. started at {1} ended at {2}".format(len(steps), str(t1), str(t2)))