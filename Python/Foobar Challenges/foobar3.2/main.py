# You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape
# pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The
# door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).
#
# Write a function solution(map) that generates the length of the shortest path from the station door to the escape
# pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number
# of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always
# passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and
# width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Python cases --
# Input:
# solution.solution([[0, 1, 1, 0],                      [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
#                    [0, 0, 0, 1],
#                    [1, 1, 0, 0],
#                    [1, 1, 1, 0]])
# Output:
#    7
#
# Input: solution.solution([[0, 0, 0, 0, 0, 0],
#                           [1, 1, 1, 1, 1, 0],
#                           [0, 0, 0, 0, 0, 0],
#                           [0, 1, 1, 1, 1, 1],
#                           [0, 1, 1, 1, 1, 1],
#                           [0, 0, 0, 0, 0, 0]])
#                           Output: 11

def solution(map):
    def solve(map):
        # create matrix of same size with zeroes
        width = len(map[0])
        length = len(map)
        zeros_matrix = []
        for i in range(length):
            zeros_matrix.append([])
            for j in range(width):
                zeros_matrix[-1].append(0)
        zeros_matrix[i][j] = 0
        # put 1 on starting point
        zeros_matrix[0][0] = 1
        width = len(map[0])
        length = len(map)

        def make_step(k):  # a step is looking around the current point, if there are no walls, assign k+1 to it
            if k > width * length:
                return 999  # solve the edge case when length is 2 and there is no solution without removing a wall
            for i in range(len(zeros_matrix)):
                for j in range(len(zeros_matrix[i])):
                    if zeros_matrix[i][j] == k:
                        if i > 0 and zeros_matrix[i - 1][j] == 0 and map[i - 1][j] == 0:
                            zeros_matrix[i - 1][j] = k + 1
                        if j > 0 and zeros_matrix[i][j - 1] == 0 and map[i][j - 1] == 0:
                            zeros_matrix[i][j - 1] = k + 1
                        if i < len(zeros_matrix) - 1 and zeros_matrix[i + 1][j] == 0 and map[i + 1][j] == 0:
                            zeros_matrix[i + 1][j] = k + 1
                        if j < len(zeros_matrix[i]) - 1 and zeros_matrix[i][j + 1] == 0 and map[i][j + 1] == 0:
                            zeros_matrix[i][j + 1] = k + 1

        def take_all_steps():  # take steps until a solution is found
            k = 0
            while zeros_matrix[length - 1][width - 1] == 0:
                k += 1
                if make_step(k) == 999:
                    return 999
            return max(zeros_matrix[length - 1])

        return take_all_steps()
    # check if there are walls at all
    width = len(map[0])
    length = len(map)
    sums = []
    for item in map:
        sums.append(sum(item))
    if sum(sums) == 0:  # edge case when there are no walls
        return (width + length) - 1



    solutions = []
    for i in range(len(map)):  # replacing every wall with an empty space, one by one
        for j in range(len(map[i])):
            if map[i][j] == 1:
                map[i][j] = 0
                temp_solution = solve(map)
                if temp_solution == (width + length) - 1:
                    return temp_solution  # if the path is already the shortest path, return it
                else:
                    solutions.append(temp_solution)  # put all solution lengths into an array
                map[i][j] = 1
    return min(solutions)  # return the shortest path's length





print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))

print(solution([[0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0]]))

print(solution([[0, 1, 1],
                [0, 1, 0]]))