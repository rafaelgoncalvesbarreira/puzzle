from path_item import PathItem
from datetime import datetime
if __name__ == "__main__":
    import astar
    target = PathItem([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    #start = PathItem([[1,2,3],[4,5,6],[0,7,8]]) #ok
    #start = PathItem([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) # not ok 31
    #start = PathItem([[2, 8, 3], [1, 6, 4], [7, 0, 5]]) 
    #start = PathItem([[1,2,3],[4,0,5],[7,8,6]]) # ok
    #start = PathItem([[1, 2, 3], [0, 4, 5], [7, 8, 6]]) #ok
    start = PathItem([[1, 2, 3], [6, 0, 8], [5, 4, 7]]) #ok 11
    print "starting..."
    t1 = datetime.now()
    steps = astar.resolve(start,target)
    t2 = datetime.now()
    
    for step in steps:
        print(step.board)
    print "end with %d steps. started at %s ended at %s" % (len(steps), str(t1), str(t2))