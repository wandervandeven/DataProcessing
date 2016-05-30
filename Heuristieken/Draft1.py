# Draft 1
# Wessel de Jong
import random
class Point(object):
    def __init__(self, x, y, z, score, point_old):
        self.x = x
        self.y = y
        self.z = z
        self.score = score
        self.point_old = point_old
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    def getScore(self):
        return self.score
    def getOld(self):
        return self.point_old
    def __str__(self):
        return "x %d, y %d, z %d, score %d" % (self.x, self.y, self.z, self.score)
class Grid(object):
    """
    Represents a grid with specified gates to be connected
    
    Positions all gates at specified locations
    """
    
    def __init__(self, width, height, depth):
        """
        Initializes grid with given width, height and depth
        
        Positions all gates at specified locations
        
        Gates is a list of gate  
        
        width: an integer > 0
        height: an integer > 0
        depth: an integer > 0
        """
        # absolute values to ensure positive integers
        self.width = abs(width)
        self.height = abs(height)
        self.depth = abs(depth)
        # list for saving grid
        self.grid = []
        # for each row
        for x in range(self.width):
            self.grid.append([])
            # for each column
            for y in range(self.height):
                self.grid[x].append([])
                for z in range(self.depth):
                    self.grid[x][y].append('x')
                    print ''
    def writeGrid(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    print self.grid[x][y][z],
                print ''
            print ''
    def resetGrid(self):
        self.grid = []
        for x in range(self.width):
            self.grid.append([])
            # for each column
            for y in range(self.height):
                self.grid[x].append([])
                for z in range(self.depth):
                    self.grid[x][y].append('x')
                    print ''
def sorter (netlist):
    """
    sorts the netlist from short to longer paths
    """
    # selection sort with Manhattan distance on netlist
    for i in range(len(netlist)):
        positionMin = i
        for j in range(i, len(netlist)):
            distance_1 = (abs(netlist[positionMin][0][0] - netlist[positionMin][1][0])) + (abs(netlist[positionMin][0][1] - netlist[positionMin][1][1]))
            distance_2 = (abs(netlist[j][0][0] - netlist[j][1][0])) + (abs(netlist[j][0][1] - netlist[j][1][1]))
            # check if distance between gates of second path is smaller
            if distance_1 > distance_2:
                positionMin = j
        # change position
        temp = netlist[i]
        netlist[i] = netlist[positionMin]
        netlist[positionMin] = temp
        print netlist[i]
        
def pathfinder (grid, netlist, gates):
    """
    netlist is a lists of lists with gate coordinates which should be connected
    grid is object of class Grid
    """
    # list for paths visited
    visited = []
    # list for checked paths
    checked = []
    counter = 0
    # append start of path to queue
    for i in range(len(netlist)):
        
        # queue for breadth first search
        queue = []
        # list for checked paths
        checked = []
        # save total path for comparing with netlist
        total_path = []
        # start point
        start = Point(netlist[i][0][0], netlist[i][0][1], netlist[i][0][2], 0, None)
        # save start of path to be searched in queueu
        queue.append(start)
        #save total path for comparing with netlist
        total_path.append(netlist[i][0])
        total_path.append(netlist[i][0])
        # save start point in visited
        checked.append(netlist[i][0])
        # define node in scope of entire function
        node = None
        # check possible steps for queue
        while len(queue) != 0:
            # pop first element
            node = queue.pop(0)
    
            # update total path
            total_path[1] = [node.getX(), node.getY(), node.getZ()]
            # check if path is in netlist
            if total_path == netlist[i]:
                print str(counter)
                counter = counter + 1
                break
            # check step to the right
            if node.getX() + 1 < grid.width:
                if [node.getX() + 1, node.getY(), node.getZ()] ==  netlist[i][1] or ([node.getX() + 1, node.getY(), node.getZ()] not in checked and grid.grid[node.getX() + 1][node.getY()][node.getZ()] == 'x'):
                    # Manhatten distance to goal
                    score = abs((node.getX() + 1) - netlist[i][1][0]) + abs(node.getY() - netlist[i][1][1]) + abs(node.getZ() - netlist[i][1][2])                      
                    # check for destination
                    if [node.getX() + 1, node.getY(), node.getZ()] !=  netlist[i][1] and [node.getX() + 2, node.getY(), node.getZ()] != netlist[i][1] and [node.getX() + 1, node.getY() + 1, node.getZ()] != netlist[i][1] and [node.getX() + 1, node.getY() - 1, node.getZ()] != netlist[i][1] and [node.getX() + 1, node.getY(), node.getZ() + 1] !=  netlist[i][1] and [node.getX() + 1, node.getY(), node.getZ() - 1] !=  netlist[i][1]:
                        # check for docking point
                        if [node.getX() + 2, node.getY(), node.getZ()] in gates or [node.getX() + 1, node.getY() + 1, node.getZ()] in gates or [node.getX() + 1, node.getY() - 1, node.getZ()] in gates or [node.getX() + 1, node.getY(), node.getZ() - 1] in gates or [node.getX() + 1, node.getY(), node.getZ() + 1] in gates:
                            # print 'hoi'
                            score = score + 1000
                    # add score up to now
                    score = score + node.getScore()
                    # append queue
                    queue.append(Point(node.getX() + 1, node.getY(), node.getZ(), score, node))
                    # append checked nodes
                    checked.append([node.getX() + 1, node.getY(), node.getZ()])
                   
            # check step to the left
            if node.getX() - 1 >= 0:
                if [node.getX() - 1, node.getY(), node.getZ()] ==  netlist[i][1] or ([node.getX() - 1, node.getY(), node.getZ()] not in checked and grid.grid[node.getX() - 1][node.getY()][node.getZ()] == 'x'):
                    # Manhatten distance to goal
                    score = abs((node.getX() - 1) - netlist[i][1][0]) + abs(node.getY() - netlist[i][1][1]) + abs(node.getZ() - netlist[i][1][2])                      
                    if [node.getX() - 1, node.getY(), node.getZ()] !=  netlist[i][1] and [node.getX() - 2, node.getY(), node.getZ()] !=  netlist[i][1] and [node.getX() - 1, node.getY() + 1, node.getZ()] !=  netlist[i][1] and [node.getX() - 1, node.getY() - 1, node.getZ()] !=  netlist[i][1] and [node.getX() - 1, node.getY(), node.getZ() + 1] !=  netlist[i][1] and [node.getX() - 1, node.getY(), node.getZ() - 1] !=  netlist[i][1]: 
                        # check for docking point
                        if [node.getX() - 2, node.getY(), node.getZ()] in gates or [node.getX() - 1, node.getY() + 1, node.getZ()] in gates or [node.getX() - 1, node.getY() - 1, node.getZ()] in gates or [node.getX() - 1, node.getY(), node.getZ() - 1] in gates or [node.getX() - 1, node.getY(), node.getZ() + 1] in gates:
                            # print 'hoi'
                            score = score + 1000
                    # add score up to now
                    score = score + node.getScore()
                    queue.append(Point(node.getX() - 1, node.getY(), node.getZ(), score, node))
                    checked.append([node.getX() -1, node.getY(), node.getZ()])
            # check step up
            if node.getY() + 1 < grid.height:
                if [node.getX(), node.getY() + 1, node.getZ()] ==  netlist[i][1] or ([node.getX(), node.getY() + 1, node.getZ()] not in checked and grid.grid[node.getX()][node.getY() + 1][node.getZ()] == 'x'):
                    
                    # Manhatten distance to goal
                    score = abs(node.getX() - netlist[i][1][0]) + abs((node.getY() + 1) - netlist[i][1][1]) + abs(node.getZ() - netlist[i][1][2])                      
                    if [node.getX(), node.getY() + 1, node.getZ()] !=  netlist[i][1] and [node.getX(), node.getY() + 2, node.getZ()] !=  netlist[i][1] and [node.getX() + 1, node.getY() + 1, node.getZ()] !=  netlist[i][1] and [node.getX() - 1, node.getY() + 1, node.getZ()] !=  netlist[i][1] and [node.getX(), node.getY() + 1, node.getZ() + 1] !=  netlist[i][1] and [node.getX(), node.getY() + 1, node.getZ() - 1] !=  netlist[i][1]:
                        # check for docking point
                        if [node.getX(), node.getY() + 2, node.getZ()] in gates or [node.getX() - 1, node.getY() + 1, node.getZ()] in gates or [node.getX() + 1, node.getY() + 1, node.getZ()] in gates or [node.getX(), node.getY() + 1, node.getZ() - 1] in gates or [node.getX(), node.getY() + 1, node.getZ() + 1] in gates:
                            # print 'hoi'
                            score = score + 1000
                    # add score up to now
                    score = score + node.getScore()
                    queue.append(Point(node.getX(), node.getY() + 1, node.getZ(), score, node))
                    checked.append([node.getX(), node.getY() + 1, node.getZ()])
            # check step down
            if node.getY() - 1 >= 0:
                if [node.getX(), node.getY() - 1, node.getZ()] ==  netlist[i][1] or ([node.getX(), node.getY() - 1, node.getZ()] not in checked and grid.grid[node.getX()][node.getY() - 1][node.getZ()] == 'x'):
                    
                    # Manhatten distance to goal
                    score = abs(node.getX() - netlist[i][1][0]) + abs((node.getY() - 1) - netlist[i][1][1]) + abs(node.getZ() - netlist[i][1][2])                      
                    if [node.getX(), node.getY() - 1, node.getZ()] !=  netlist[i][1] and [node.getX(), node.getY() - 2, node.getZ()] !=  netlist[i][1] and [node.getX() + 1, node.getY() - 1, node.getZ()] !=  netlist[i][1] and [node.getX() - 1, node.getY() - 1, node.getZ()] !=  netlist[i][1] and [node.getX(), node.getY() - 1, node.getZ() + 1] !=  netlist[i][1] and [node.getX(), node.getY() - 1, node.getZ() - 1] !=  netlist[i][1]:
                        # check for docking point
                        if [node.getX(), node.getY() - 2, node.getZ()] in gates or [node.getX() - 1, node.getY() - 1, node.getZ()] in gates or [node.getX() + 1, node.getY() - 1, node.getZ()] in gates or [node.getX(), node.getY() - 1, node.getZ() - 1] in gates or [node.getX(), node.getY() - 1, node.getZ() + 1] in gates:
                            # print 'hoi'
                            score = score + 1000
                    # add score up to now
                    score = score + node.getScore()
                    queue.append(Point(node.getX(), node.getY() - 1, node.getZ(), score, node))
                    checked.append([node.getX(), node.getY() - 1, node.getZ()])
            
            # check step to lower grid
            if node.getZ() + 1 < grid.depth:
                if [node.getX(), node.getY(), node.getZ() + 1] ==  netlist[i][1] or ([node.getX(), node.getY(), node.getZ() + 1] not in checked and grid.grid[node.getX()][node.getY()][node.getZ() + 1] == 'x'):
                    
                    # Manhatten distance to goal
                    score = abs(node.getX() - netlist[i][1][0]) + abs(node.getY() - netlist[i][1][1]) + abs((node.getZ() + 1) - netlist[i][1][2])                      
                    if [node.getX(), node.getY(), node.getZ() + 1] !=  netlist[i][1] and [node.getX(), node.getY(), node.getZ() + 2] !=  netlist[i][1] and [node.getX() + 1, node.getY(), node.getZ() + 1] !=  netlist[i][1] and [node.getX() - 1, node.getY(), node.getZ() + 1] !=  netlist[i][1] and [node.getX(), node.getY() + 1, node.getZ() + 1] !=  netlist[i][1] and [node.getX(), node.getY() - 1, node.getZ() + 1] !=  netlist[i][1]: 
                        # check for docking point
                        if [node.getX() + 1, node.getY(), node.getZ() + 1] in gates or [node.getX() - 1, node.getY(), node.getZ() + 1] in gates or [node.getX(), node.getY() - 1, node.getZ() + 1] in gates or [node.getX(), node.getY() + 1, node.getZ() + 1] in gates or [node.getX(), node.getY(), node.getZ() + 2] in gates:
                            # print 'hoi'
                            score = score + 1000
                    # add score up to now
                    score = score + node.getScore()
                    queue.append(Point(node.getX(), node.getY(), node.getZ() + 1, score, node))
                    checked.append([node.getX(), node.getY(), node.getZ() + 1])
            # check step to upper grid
            if node.getZ() - 1 >= 0:
                if [node.getX(), node.getY(), node.getZ() - 1] ==  netlist[i][1] or ([node.getX(), node.getY(), node.getZ() - 1] not in checked and grid.grid[node.getX()][node.getY()][node.getZ() - 1] == 'x'):
                    
                     # Manhatten distance to goal
                    score = abs(node.getX() - netlist[i][1][0]) + abs(node.getY() - netlist[i][1][1]) + abs((node.getZ() - 1) - netlist[i][1][2])                      
                    if [node.getX(), node.getY(), node.getZ() - 1] !=  netlist[i][1] and [node.getX(), node.getY(), node.getZ() - 2] !=  netlist[i][1] and [node.getX() + 1, node.getY(), node.getZ() - 1] !=  netlist[i][1] and [node.getX() - 1, node.getY(), node.getZ() - 1] !=  netlist[i][1] and [node.getX(), node.getY() + 1, node.getZ() - 1] !=  netlist[i][1] and [node.getX(), node.getY() - 1, node.getZ() - 1] !=  netlist[i][1]:
                        # check for docking point
                        if [node.getX() + 1, node.getY(), node.getZ() - 1] in gates or [node.getX() - 1, node.getY(), node.getZ() - 1] in gates or [node.getX(), node.getY() - 1, node.getZ() - 1] in gates or [node.getX(), node.getY() + 1, node.getZ() - 1] in gates or [node.getX(), node.getY(), node.getZ() - 2] in gates:
                            # print 'hoi'
                            score = score + 1000
                    # add score up to now
                    score = score + node.getScore()
                    queue.append(Point(node.getX(), node.getY(), node.getZ() - 1, score, node))
                    checked.append([node.getX(), node.getY(), node.getZ() - 1])
            # sort queue
            for j in range(len(queue)):
                scoreMin = j
                for k in range(j, len(queue)):
                    score_1 = queue[scoreMin].getScore()
                    score_2 = queue[k].getScore()
                    # check for minimum score
                    if score_1 > score_2:
                        scoreMin = k
                # change position
                temp = queue[j]
                queue[j] = queue[scoreMin]
                queue[scoreMin] = temp
        # if path not found stop
        if total_path != netlist[i]:
            return counter;
            
        # save last node
        previous = node
        # backtrack until start
        while previous != None:
            # print path
            grid.grid[previous.getX()][previous.getY()][previous.getZ()] = str(counter)
            
            # update previous
            previous = previous.getOld()
def swapper (grid, netlist, gates):
   
    # save original netlist
    best_netlist = netlist[:]
    best_score = pathfinder(grid, best_netlist, gates)
    # check if all paths were linked
    while best_score < len(netlist):
        # update netlist
        netlist = best_netlist[:]
        # five random shuffles
        for _ in range(5):
            random_1 = random.randrange(len(netlist))
            random_2 = random.randrange(len(netlist))
            temp = netlist[random_1]
            netlist[random_1] = netlist[random_2]
            netlist[random_2] = temp
        # reset grid
        grid.resetGrid()
        # save paths of new netlist
        new_score = pathfinder(grid, netlist, gates)
        # check if new score is better
        if best_score < new_score:
            # save new score as best score
            best_score = new_score
            # save new netlist as best netlist
            best_netlist = netlist[:]
    print netlist
    grid.writeGrid()
    
grid = Grid(18, 13, 7)
netlist_1 = [  [[1, 11, 0], [3, 2, 0]], [[12, 2, 0], [12, 3, 0]], 
             [[6, 1, 0], [1, 1, 0]], [[2, 8, 0], [2, 10, 0]], 
             [[15, 1, 0], [12, 2, 0]], [[12, 3, 0], [13, 7, 0]], 
             [[15, 1, 0], [1, 11, 0]], [[1, 11, 0], [8, 4, 0]], 
             [[9, 10, 0], [13, 7, 0]], [[2, 8, 0], [9, 8, 0]], 
             [[1, 9, 0], [4, 5, 0]], [[2, 8, 0], [8, 4, 0]], 
             [[13, 7, 0], [11, 8, 0]], [[15, 8, 0], [10, 1, 0]], 
             [[9, 10, 0], [11, 5, 0]], [[4, 5, 0], [3, 2, 0]], 
             [[11, 5, 0], [1, 12, 0]], [[15, 1, 0], [2, 8, 0]], 
             [[10, 1, 0], [1, 9, 0]], [[15, 1, 0], [3, 2, 0]], 
             [[1, 9, 0], [15, 8, 0]], [[6, 8, 0], [1, 5, 0]], 
             [[15, 8, 0], [12, 2, 0]], [[15, 1, 0], [1, 1, 0]], 
             [[2, 8, 0], [12, 2, 0]], [[14, 2, 0], [16, 7, 0]], 
             [[12, 3, 0], [1, 5, 0]], [[1, 5, 0], [13, 7, 0]], 
             [[9, 10, 0], [6, 8, 0]], [[4, 5, 0], [12, 3, 0]]
            ]
gates_1 = [[1, 1, 0], [3, 2 ,0], [6, 1, 0], [10, 1, 0], [15, 1, 0], [12, 2, 0], [14, 2 ,0],
           [12, 3 ,0], [8, 4 ,0], [1, 5, 0], [4, 5, 0], [11, 5 , 0], [16, 5 ,0], [13, 7 ,0],
           [16, 7, 0], [2, 8, 0], [6, 8 ,0], [9, 8 ,0], [11, 8 , 0], [15, 8 , 0], [1, 9, 0], 
           [2, 10 , 0], [9, 10 , 0], [1, 11, 0], [1, 12, 0] ]
# grid = Grid(5, 5, 1)
# netlist_1 = [ [[0, 2, 0], [4, 2, 0]] ]
# gates_1 = [ [0, 2, 0], [4, 2, 0],  [2, 2, 0]]

sorter(netlist_1)
# random.shuffle(netlist_1)
swapper(grid, netlist_1, gates_1)
print ''
# grid.grid[15][1][0] = "B"
# grid.grid[2][8][0] = "B"