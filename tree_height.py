# python3

import sys
import threading

def compute_height(node_skaits, parent_input):
    # Write this function
    max_height = 0
    apskatitie = {}

    def kartas_nr(index):
        #print("index ir -->", index)

        if index == -1:
            return 0
        if index in apskatitie:
            return apskatitie[index]
        
        augstums = kartas_nr(parent_input[index]) + 1
        apskatitie[index] = augstums
        return augstums
        
    skaits = (int)(node_skaits)

    for i in range (skaits):
        #print("nr ir -->", i)
        max_height = max(max_height, kartas_nr(i))
    
    return max_height


def main():

    ievade = input()
    # implement input form keyboard and from files
    if 'I' in ievade:
        node_skaits = input()
        parent_input = list(map(int,input().split()))
        print(compute_height(node_skaits, parent_input))

    if 'F' in ievade:
        file = input()
        if "a" not in file:
            with open ("./test/"+file,'r') as fails:
                 node_skaits = int(fails.readline())
                 parent_input = list(map(int,fails.readline().split()))
                 print(compute_height(node_skaits, parent_input))


    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
