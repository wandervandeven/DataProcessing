# # from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
import random
import math
import copy

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

    def getDepth(self):
        return self.depth

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

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

def makeStep (node, grid, netlist, gates, queue, checked, index):
    # check step to the right
    if node.getX() + 1 < grid.width:
        if [node.getX() + 1, node.getY(), node.getZ()] ==  netlist[index][1] or ([node.getX() + 1, node.getY(), node.getZ()] not in checked and grid.grid[node.getX() + 1][node.getY()][node.getZ()] == 'x'):
            # Manhatten distance to goal
            score = abs((node.getX() + 1) - netlist[index][1][0]) + abs(node.getY() - netlist[index][1][1]) + abs(node.getZ() - netlist[index][1][2])                      

            # check for destination
            if [node.getX() + 1, node.getY(), node.getZ()] !=  netlist[index][1] and [node.getX() + 2, node.getY(), node.getZ()] != netlist[index][1] and [node.getX() + 1, node.getY() + 1, node.getZ()] != netlist[index][1] and [node.getX() + 1, node.getY() - 1, node.getZ()] != netlist[index][1] and [node.getX() + 1, node.getY(), node.getZ() + 1] !=  netlist[index][1] and [node.getX() + 1, node.getY(), node.getZ() - 1] !=  netlist[index][1]:
                # check if next point is a docking point and check if next point is not directly above gates on first grid
                if [node.getX() + 2, node.getY(), node.getZ()] in gates or [node.getX() + 1, node.getY() + 1, node.getZ()] in gates or [node.getX() + 1, node.getY() - 1, node.getZ()] in gates or [node.getX() + 1, node.getY(), node.getZ() - 1] in gates or [node.getX() + 1, node.getY(), node.getZ() + 1] in gates:
                    # add 1000 to score if path build on docking point
                    score = score + 10000

            # calculate total score of path build up to now
            score = score + node.getScore()
            # append queue
            queue.append(Point(node.getX() + 1, node.getY(), node.getZ(), score, node))
            # append checked nodes
            checked.append([node.getX() + 1, node.getY(), node.getZ()])
           
    # check step to the left
    if node.getX() - 1 >= 0:
        if [node.getX() - 1, node.getY(), node.getZ()] ==  netlist[index][1] or ([node.getX() - 1, node.getY(), node.getZ()] not in checked and grid.grid[node.getX() - 1][node.getY()][node.getZ()] == 'x'):

            score = abs((node.getX() - 1) - netlist[index][1][0]) + abs(node.getY() - netlist[index][1][1]) + abs(node.getZ() - netlist[index][1][2])                      

            if [node.getX() - 1, node.getY(), node.getZ()] !=  netlist[index][1] and [node.getX() - 2, node.getY(), node.getZ()] !=  netlist[index][1] and [node.getX() - 1, node.getY() + 1, node.getZ()] !=  netlist[index][1] and [node.getX() - 1, node.getY() - 1, node.getZ()] !=  netlist[index][1] and [node.getX() - 1, node.getY(), node.getZ() + 1] !=  netlist[index][1] and [node.getX() - 1, node.getY(), node.getZ() - 1] !=  netlist[index][1]: 
                if [node.getX() - 2, node.getY(), node.getZ()] in gates or [node.getX() - 1, node.getY() + 1, node.getZ()] in gates or [node.getX() - 1, node.getY() - 1, node.getZ()] in gates or [node.getX() - 1, node.getY(), node.getZ() - 1] in gates or [node.getX() - 1, node.getY(), node.getZ() + 1] in gates:
                    score = score + 10000

            score = score + node.getScore()

            queue.append(Point(node.getX() - 1, node.getY(), node.getZ(), score, node))
            checked.append([node.getX() -1, node.getY(), node.getZ()])

    # check step up on current grid
    if node.getY() + 1 < grid.height:
        if [node.getX(), node.getY() + 1, node.getZ()] ==  netlist[index][1] or ([node.getX(), node.getY() + 1, node.getZ()] not in checked and grid.grid[node.getX()][node.getY() + 1][node.getZ()] == 'x'):
            
            score = abs(node.getX() - netlist[index][1][0]) + abs((node.getY() + 1) - netlist[index][1][1]) + abs(node.getZ() - netlist[index][1][2])                      

            if [node.getX(), node.getY() + 1, node.getZ()] !=  netlist[index][1] and [node.getX(), node.getY() + 2, node.getZ()] !=  netlist[index][1] and [node.getX() + 1, node.getY() + 1, node.getZ()] !=  netlist[index][1] and [node.getX() - 1, node.getY() + 1, node.getZ()] !=  netlist[index][1] and [node.getX(), node.getY() + 1, node.getZ() + 1] !=  netlist[index][1] and [node.getX(), node.getY() + 1, node.getZ() - 1] !=  netlist[index][1]:
                if [node.getX(), node.getY() + 2, node.getZ()] in gates or [node.getX() - 1, node.getY() + 1, node.getZ()] in gates or [node.getX() + 1, node.getY() + 1, node.getZ()] in gates or [node.getX(), node.getY() + 1, node.getZ() - 1] in gates or [node.getX(), node.getY() + 1, node.getZ() + 1] in gates:
                    score = score + 10000

            score = score + node.getScore()

            queue.append(Point(node.getX(), node.getY() + 1, node.getZ(), score, node))
            checked.append([node.getX(), node.getY() + 1, node.getZ()])

    # check step down on current grid
    if node.getY() - 1 >= 0:
        if [node.getX(), node.getY() - 1, node.getZ()] ==  netlist[index][1] or ([node.getX(), node.getY() - 1, node.getZ()] not in checked and grid.grid[node.getX()][node.getY() - 1][node.getZ()] == 'x'):

            score = abs(node.getX() - netlist[index][1][0]) + abs((node.getY() - 1) - netlist[index][1][1]) + abs(node.getZ() - netlist[index][1][2])                      

            if [node.getX(), node.getY() - 1, node.getZ()] !=  netlist[index][1] and [node.getX(), node.getY() - 2, node.getZ()] !=  netlist[index][1] and [node.getX() + 1, node.getY() - 1, node.getZ()] !=  netlist[index][1] and [node.getX() - 1, node.getY() - 1, node.getZ()] !=  netlist[index][1] and [node.getX(), node.getY() - 1, node.getZ() + 1] !=  netlist[index][1] and [node.getX(), node.getY() - 1, node.getZ() - 1] !=  netlist[index][1]:
                if [node.getX(), node.getY() - 2, node.getZ()] in gates or [node.getX() - 1, node.getY() - 1, node.getZ()] in gates or [node.getX() + 1, node.getY() - 1, node.getZ()] in gates or [node.getX(), node.getY() - 1, node.getZ() - 1] in gates or [node.getX(), node.getY() - 1, node.getZ() + 1] in gates:
                    score = score + 10000

            score = score + node.getScore()

            queue.append(Point(node.getX(), node.getY() - 1, node.getZ(), score, node))
            checked.append([node.getX(), node.getY() - 1, node.getZ()])
    
    # check step to lower grid
    if node.getZ() + 1 < grid.depth:
        if [node.getX(), node.getY(), node.getZ() + 1] ==  netlist[index][1] or ([node.getX(), node.getY(), node.getZ() + 1] not in checked and grid.grid[node.getX()][node.getY()][node.getZ() + 1] == 'x'):
            
            score = abs(node.getX() - netlist[index][1][0]) + abs(node.getY() - netlist[index][1][1]) + abs((node.getZ() + 1) - netlist[index][1][2])                      

            if [node.getX(), node.getY(), node.getZ() + 1] !=  netlist[index][1] and [node.getX(), node.getY(), node.getZ() + 2] !=  netlist[index][1] and [node.getX() + 1, node.getY(), node.getZ() + 1] !=  netlist[index][1] and [node.getX() - 1, node.getY(), node.getZ() + 1] !=  netlist[index][1] and [node.getX(), node.getY() + 1, node.getZ() + 1] !=  netlist[index][1] and [node.getX(), node.getY() - 1, node.getZ() + 1] !=  netlist[index][1]: 
                if [node.getX() + 1, node.getY(), node.getZ() + 1] in gates or [node.getX() - 1, node.getY(), node.getZ() + 1] in gates or [node.getX(), node.getY() - 1, node.getZ() + 1] in gates or [node.getX(), node.getY() + 1, node.getZ() + 1] in gates or [node.getX(), node.getY(), node.getZ() + 2] in gates:
                    score = score + 10000

            score = score + node.getScore()

            queue.append(Point(node.getX(), node.getY(), node.getZ() + 1, score, node))
            checked.append([node.getX(), node.getY(), node.getZ() + 1])

    # check step to upper grid
    if node.getZ() - 1 >= 0:
        if [node.getX(), node.getY(), node.getZ() - 1] ==  netlist[index][1] or ([node.getX(), node.getY(), node.getZ() - 1] not in checked and grid.grid[node.getX()][node.getY()][node.getZ() - 1] == 'x'):
            
            score = abs(node.getX() - netlist[index][1][0]) + abs(node.getY() - netlist[index][1][1]) + abs((node.getZ() - 1) - netlist[index][1][2])                      

            if [node.getX(), node.getY(), node.getZ() - 1] !=  netlist[index][1] and [node.getX(), node.getY(), node.getZ() - 2] !=  netlist[index][1] and [node.getX() + 1, node.getY(), node.getZ() - 1] !=  netlist[index][1] and [node.getX() - 1, node.getY(), node.getZ() - 1] !=  netlist[index][1] and [node.getX(), node.getY() + 1, node.getZ() - 1] !=  netlist[index][1] and [node.getX(), node.getY() - 1, node.getZ() - 1] !=  netlist[index][1]:
                if [node.getX() + 1, node.getY(), node.getZ() - 1] in gates or [node.getX() - 1, node.getY(), node.getZ() - 1] in gates or [node.getX(), node.getY() - 1, node.getZ() - 1] in gates or [node.getX(), node.getY() + 1, node.getZ() - 1] in gates or [node.getX(), node.getY(), node.getZ() - 2] in gates:
                    score = score + 10000

            score = score + node.getScore()

            queue.append(Point(node.getX(), node.getY(), node.getZ() - 1, score, node))
            checked.append([node.getX(), node.getY(), node.getZ() - 1])

def queueSorter (queue):
    # sort queue on basis of score
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

# # dataset for visualisation
# datasets = []

def visualizer (datasets):
    # plot build paths
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

    for dataset in datasets:
        ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["colour"])

    plt.savefig('myfig')



def pathRemover(unsolved_paths, solved_paths, grid, costs):
    # select random paths to be removed
    random.shuffle(solved_paths)

    print "hoi"

    # remove 20 % of solved paths in grid
    for l in range(int(len(solved_paths) * 0.20 + 1)):
        for z in range(grid.getDepth()):
            for y in range(grid.getHeight()):
                for x in range(grid.getWidth()):
                    if grid.grid[x][y][z] == str(solved_paths[l]):
                        # remove paths in grid
                        grid.grid[x][y][z] = 'x'
                        # lower costs of total path
                        costs = costs - 1

        # append removed path to unsolved paths
        unsolved_paths.append(solved_paths.pop(l))

    return costs 


def pathfinder (grid, netlist, gates):
    """
    netlist is a lists of lists with gate coordinates which should be connected
    grid is object of class Grid
    """

    # reset grid to start over again
    grid.resetGrid()

    # next iteration
    iteration = 0

    # constant for simulated annealing
    c = 200

    # initial best score
    best_score = 0

    # list for build paths 
    solved_paths = []

    # keep track of path length and thus total costs
    costs = 0 

    # paths still required
    unsolved_paths = [x for x in range(len(netlist))]

    # dataset for visualisation
    datasets = []

    while len(solved_paths) != len(netlist):
       
        # track path placing
        # print len(solved_paths)

        # next iteration
        iteration += 1

        # queue for storing paths during pathsearch
        queue = []

        # list for checked paths
        checked = []

        # save total path to check if destination is reached
        total_path = []

        # index in netlist of path to be build
        index = unsolved_paths.pop(0)

        # start with first path in netlist
        start = Point(netlist[index][0][0], netlist[index][0][1], netlist[index][0][2], 0, None)

        # append start point to queue
        queue.append(start)

        # update total path to startpoint, no paths build yet
        total_path.append(netlist[index][0])
        total_path.append(netlist[index][0])

        # save start point in checked
        checked.append(netlist[index][0])

        # define node in scope of entire function
        node = None

        # start building shortest path
        while len(queue) != 0:

            # pop first element from queue
            node = queue.pop(0)
    
            # update total path
            total_path[1] = [node.getX(), node.getY(), node.getZ()]

            # check if destination is reached
            if total_path == netlist[index]:
                # append path to solved paths
                solved_paths.append(index)
                # start with next path
                break

            # make step
            makeStep(node, grid, netlist, gates, queue, checked, index)
           
            # sort queue for A* algorithm 
            queueSorter(queue)

        print index
        print solved_paths
        print unsolved_paths

        # check if path not found
        if total_path != netlist[index]:

            # place  path back into unsolved paths
            unsolved_paths.append(index)


            # first time path not found
            if best_score == 0:
                best_score = len(solved_paths)
                best_solved = solved_paths[:]
                best_unsolved = unsolved_paths[:]
                best_grid = copy.deepcopy(grid)
                best_costs = costs

            # calculate temperature for simulated annealing
            temperature = c/math.log(iteration + 1)

            # print "solved: %d" % len(solved_paths)
            # print "best: %d" % len(best_score)

            # check if shuffled path leads to better solution
            if len(solved_paths) >= best_score:

                best_score = len(solved_paths)
                
                # save new best score
                best_solved = solved_paths[:]
                best_unsolved = unsolved_paths[:]
                best_grid = copy.deepcopy(grid)
                best_costs = costs

                # remove paths
                # print solved_paths
                # print unsolved_paths
                costs = pathRemover(unsolved_paths, solved_paths, grid, costs)
                # print solved_paths
                # print unsolved_paths

                # continue searching for solution    
                continue

            # shuffled path does not lead to better solution
            else: 
                # acceptance prob for simulated annealing
                a = math.exp((len(solved_paths) - len(best_solved)) / temperature)

                # check if new_score is accepted
                if a > random.random():

                    best_score = len(solved_paths)

                    best_solved = solved_paths[:]
                    best_unsolved = unsolved_paths[:]
                    best_grid = copy.deepcopy(grid)
                    best_costs = costs
                  
                    costs = pathRemover(unsolved_paths, solved_paths, grid, costs)
                
                else:
                    # do not accept new score
                    print "poef"

                    solved_paths = best_solved[:]
                    unsolved_paths = best_unsolved[:]
                    grid = copy.deepcopy(best_grid)
                    costs = best_costs

                    # print "test2:"
                    # print solved_paths
                    # print unsolved_paths
                    costs = pathRemover(unsolved_paths, solved_paths, grid, costs)
                    # print solved_paths
                    # print unsolved_paths
            
                # continue searching for solution    
                continue

        # save last node
        previous = node

        # dataset for visualisation
        dataset = {}

        # list for coordinates of build path
        dataset['x'] = []
        dataset['y'] = []
        dataset['z'] = []
        # select random color for visualising paths
        dataset['colour'] = "#%06x" % random.randint(0, 0xFFFFFF)

        # backtrack until startpoint
        while previous != None:

            # append coordinates for visualisation
            dataset['x'].append(previous.getX())
            dataset['y'].append(previous.getY())
            dataset['z'].append(previous.getZ())

            # print path in grid
            grid.grid[previous.getX()][previous.getY()][previous.getZ()] = str(index)

            # add costs
            costs += 1
            
            # update previous
            previous = previous.getOld()

        # append data of single path to dataset for visualisation
        datasets.append(dataset)

    print "costs %d" % costs
    grid.writeGrid()
    # visualizer(datasets)
    return costs

grid_1 = Grid(18, 13, 7)

# grid_2 = 

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

netlist_2 = [  [[16, 5, 0], [1, 9, 0]], [[1, 11, 0], [1, 9, 0]], 
             [[14, 2, 0], [1, 5, 0]], [[2, 8, 0], [4, 5, 0]], 
             [[16, 5, 0], [13, 7, 0]], [[8, 4, 0], [11, 8, 0]], 
             [[6, 1, 0], [9, 10, 0]], [[4, 5, 0], [1, 9, 0]], 
             [[3, 2, 0], [15, 1, 0]], [[4, 5, 0], [12, 2, 0]], 
             [[9, 8, 0], [11, 5, 0]], [[6, 1, 0], [2, 10, 0]], 
             [[9, 10, 0], [8, 4, 0]], [[9, 10, 0], [4, 5, 0]], 
             [[15, 8, 0], [8, 4, 0]], [[13, 7, 0], [15, 8, 0]], 
             [[4, 5, 0], [3, 2, 0]], [[1, 5, 0], [1, 11, 0]], 
             [[9, 10, 0], [11, 8, 0]], [[6, 8, 0], [2, 10, 0]], 
             [[3, 2, 0], [1, 1, 0]], [[11, 8, 0], [2, 10, 0]], 
             [[12, 2, 0], [9, 8, 0]], [[8, 4, 0], [1, 11, 0]], 
             [[11, 8, 0], [13, 7, 0]], [[13, 7, 0], [11, 5, 0]], 
             [[11, 5, 0], [12, 3, 0]], [[16, 7, 0], [12, 3, 0]], 
             [[16, 7, 0], [14, 2, 0]], [[16, 7, 0], [6, 1, 0]],
             [[1, 12, 0], [16, 5, 0]], [[11, 5, 0], [2, 8, 0]], 
             [[10, 1, 0], [12, 2, 0]], [[11, 5, 0], [16, 5, 0]], 
             [[1, 1, 0], [2, 8, 0]], [[16, 7, 0], [12, 2, 0]], 
             [[2, 8, 0], [3, 2, 0]], [[15, 8, 0], [1, 5, 0]], 
             [[15, 1, 0], [1, 1, 0]], [[2, 8, 0], [13, 7, 0]]
            ]

netlist_3 = [  [[1, 1, 0], [13, 7, 0]], [[1, 1, 0], [16, 7, 0]], 
             [[1, 1, 0], [9, 10, 0]], [[8, 4, 0], [12, 3, 0]], 
             [[6, 1, 0], [14, 2, 0]], [[10, 1, 0], [15, 8, 0]], 
             [[10, 1, 0], [1, 5, 0]], [[15, 1, 0], [8, 4, 0]], 
             [[15, 1, 0], [1, 5, 0]], [[12, 2, 0], [16, 7, 0]], 
             [[14, 2, 0], [15, 1, 0]], [[15, 1, 0], [3, 2, 0]], 
             [[12, 3, 0], [1, 11, 0]], [[4, 5, 0], [1, 1, 0]], 
             [[4, 5, 0], [3, 2, 0]], [[8, 4, 0], [3, 2, 0]], 
             [[12, 3, 0], [12, 2, 0]], [[16, 5, 0], [16, 7, 0]], 
             [[13, 7, 0], [6, 1, 0]], [[8, 4, 0], [4, 5, 0]], 
             [[11, 5, 0], [1, 1, 0]], [[11, 5, 0], [9, 8, 0]], 
             [[11, 5, 0], [10, 1, 0]],  [[8, 4, 0], [1, 5, 0]],  
             [[16, 5, 0], [1, 12, 0]], [[13, 7, 0], [15, 1, 0]], 
             [[13, 7, 0], [15, 8, 0]], [[2, 8, 0], [2, 10, 0]], 
             [[4, 5, 0], [10, 1, 0]], [[11, 8, 0], [4, 5, 0]], 
             [[1, 12, 0], [1, 11, 0]], [[6, 8, 0], [12, 3, 0]],
             [[9, 8, 0], [2, 8, 0]], [[9, 8, 0], [2, 10, 0]], 
             [[9, 8, 0], [1, 5, 0]], [[11, 8, 0], [1, 9, 0]], 
             [[11, 8, 0], [6, 1, 0]], [[16, 5, 0], [1, 5, 0]], 
             [[3, 2, 0], [13, 7, 0]], [[15, 8, 0], [2, 10, 0]], 
             [[1, 9, 0], [14, 2, 0]], [[3, 2, 0], [2, 8, 0]], 
             [[6, 1, 0], [6, 8, 0]], [[1, 9, 0], [6, 8, 0]], 
             [[9, 10, 0], [11, 5, 0]], [[9, 10, 0], [11, 8, 0]], 
             [[6, 1, 0], [10, 1, 0]], [[12, 2, 0], [16, 5, 0]], 
             [[1, 12, 0], [2, 8, 0]], [[1, 12, 0], [6, 8, 0]]
            ]

# netlist_4 = 

# netlist_5 = 

# netlist_6 = 

gates_1 = [[1, 1, 0], [3, 2 ,0], [6, 1, 0], [10, 1, 0], [15, 1, 0], [12, 2, 0], [14, 2 ,0],
           [12, 3 ,0], [8, 4 ,0], [1, 5, 0], [4, 5, 0], [11, 5 , 0], [16, 5 ,0], [13, 7 ,0],
           [16, 7, 0], [2, 8, 0], [6, 8 ,0], [9, 8 ,0], [11, 8 , 0], [15, 8 , 0], [1, 9, 0], 
           [2, 10 , 0], [9, 10 , 0], [1, 11, 0], [1, 12, 0] ]

# gates_2 = 

# sorter(netlist_1)
# random.shuffle(netlist_1)
# pathfinder(grid_1, netlist_1, gates_1)


cost = []
for i in range(1):
    sorter(netlist_3)
    cost.append(pathfinder(grid_1, netlist_3, gates_1))
print cost


# bins = [i for i in range(0, 1010, 10)]

# plt.hist(cost, bins)
# plt.title("costs")
# plt.xlabel("costs")
# plt.ylabel("Frequency")
# plt.legend()
# plt.show()
