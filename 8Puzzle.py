import math
import copy

class A_star_search:
    def __init__(self, initial_state=None):
        self.state = initial_state
        self.h = 0
        self.g = 0
        self.f = 0
        self.parent = None
        self.action = None
    def next(self, state):
        accepted_steps = []
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    r,c = i, j

        if r > 0:
            node = copy.deepcopy(state)
            r1 = r - 1
            node[r][c] = node[r1][c]
            node[r1][c] = 0
            accepted_steps.append((node, 'up'))
        if c > 0:
            node = copy.deepcopy(state)
            c1 = c -1
            node[r][c] = node[r][c1]
            node[r][c1] = 0
            accepted_steps.append((node, 'left'))
        if r < 2:
            node = copy.deepcopy(state)
            r1 = r + 1
            node[r][c] = node[r1][c]
            node[r1][c] = 0
            accepted_steps.append((node, 'down'))
        if c < 2:
            node = copy.deepcopy(state)
            c1 = c + 1
            node[r][c] = node[r1][c1]
            node[r][c1] = 0
            accepted_steps.append((node, 'right'))
        return accepted_steps

    def Path(self, node):
        actions = []
        path = []
        pathCost = node.g
        while node:
            path.append(node.state)
            actions.append(node.action)
            node  =node.parent
        actions.remove(None)
        print("Path is givem as : ")
        for node in reversed(path):
            printState(node)
        print("Operations performed are: ")
        actions = reversed(actions)
        actionSequence = ", ".join(actions)
        print(actionSequence)
        print("Path cost is :", pathCost)

    def solve(self, initial, goal, func='Manhattan'):
        generated_nodes_count = 0
        expanded_nodes_count = 0
        fringe = []
        expanded = []
        if initial.state == goal.state:
            print("Solution found: ")
            self.Path(initial)
            print("Generated nodes count: ", generated_nodes_count)
            print("Expanded nodes count: ", expanded_nodes_count)
            return
        if func == 'misplacedTiles':
            return
        if func == 'misplacedTiles':
            initial.h = misplaced(initial.state, goal.state)
        else:
            initial.h = manh(initial.state, goal.state)
        initial.f = initial.g + initial.h
        initial.parent = None
        initial.action = None
        fringe.append(initial)
        while fringe:
            curr = fringe.pop(0)
            neighbors =  self.next(curr.state)
            expanded.append(curr)
            expanded_nodes_count += 1
            for neighbor in neighbors:
                child = A_star_search()
                child.state = neighbor[0]
                child.action = neighbor[1]
                child.g = curr.g + 1
                if func == 'misplacedTiles':
                    child.h = misplaced(child.state, goal.state)
                else:
                    child.h = manh(child.state, goal.state)
                child.f = child.g + child.h
                child.parent = curr
                generated_nodes_count += 1
                if child.state == goal.state:
                    print("Solution found.")
                    self.Path(child)
                    print("Generated nodes count: ", generated_nodes_count)
                    print("Expaneded nodes count: ", expanded_nodes_count)
                    return

                isExpanded = False
                try:
                    expanded.index(child.state, )
                except ValueError:
                    isExpanded = False

                if not isExpanded:
                    found = False
                    k = 0
                    for item in fringe:
                        if item.state == child.state:
                            found = True
                            if child.f < item.f:
                                item.f = child.f
                                fringe[k] = item
                                break
                        k += 1

                    if not found:
                        fringe.append(child)
                fringe = sorted(fringe, key=lambda x: x.f)
        print("No Solution")
        return

def manh(state1, state2):
        arr = []
        manh_dist = 0
        for i in range(0, 3):
            for j in range(0, 3):
                arr.append((state2[i][j]))

        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                current_ij = state1[i][j]
                i_current = i
                j_current = j
                index = arr.index(current_ij)
                i_goal, j_goal = index // 3, index % 3
                if current_ij != 0:
                    manh_dist += (math.fabs(i_goal - i_current) + math.fabs(j_goal - j_current))
        return manh_dist

def misplaced(state1, state2):
    h = 0
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if state1[i][j] != state2[i][j] and state1[i][j] != 0:
                h += 1
    return h

def printState(state):
    for i in range(3):
        result = ""
        for j in range(3):
            result += str(state[i][j]) + " "
        print(result)
    print("")

def userInput():
    print("Enter the initial state: ")
    input_arr = []
    goal_arr = []
    element = input().split(" ")
    k = 0
    try:
        for i in range(0, 3):
            input_arr += [0]
        for i in range(0, 3):
            input_arr[i] = [0] * 3
        for i in range(0, 3):
            for j in range(0, 3):
                input_arr[i][j] = int(element[k])
                k += 1
    except (ValueError, IndexError):
        print("Please input the values using space seperation")
        return [], []
    #print("Enter the goal state")
     #   return [], []
    print("Enter the goal state")
    element = input().split(" ")
    k = 0
    try:
        for i in range(0, 3):
            goal_arr += [0]
        for i in range(0, 3):
            goal_arr[i] = [0]*3
        for i in range(0, 3):
             for j in range(0, 3):
                goal_arr[i][j] = int(element[k])
                k += 1
    except (ValueError, IndexError):
        print("Please input the value using space seperation: ")
        return  input_arr, []
    return input_arr, goal_arr



def main():
    input_arr, goal_arr = userInput()
    if input_arr and goal_arr:
        print("Initial state is: ")
        printState(input_arr)
        print("Goal state is: ")
        printState(goal_arr)
        initial = A_star_search(input_arr)
        goal = A_star_search(goal_arr)
        print("A star algorithm for the 8 puzzle problem using Manhattan Distance is: ")
        initial.solve(initial, goal)
        print("\nA star algorithm for the 8 puzzle problem using Misplaced Tiles is: ")
        initial.solve(initial, goal, 'misplacedTiles')

main()