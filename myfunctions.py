import numpy as np
import ast

def myinitarray(init, size): 
    init_ar = np.array(init) 
    zero_ar = np.zeros((size,size), dtype=int)
    final_ar = zero_ar[init_ar[:,0], init_ar[:,1]]  = 1       
    
    return zero_ar

def deletion(array,position):
    if array[position] == 0:
        print("Cannot remove tube: No tube found at"+str(position))
    else:
        array[position] = 0
        print(str(position)+" Removed")
        
    return

def move_tube(array,origin,destination):
    if array[destination] == 1:
        print("Cannot move tube at position "+str(destination)+" because it is already occupied")
    else:
        array[destination] = 1
        array[origin] = 0
        print("Tube moved from "+str(origin)+" to "+str(destination))   
        
    return 

def main(file_path):
    with open(file_path, 'r') as input_file:
        size = int(input_file.readline())
        lines = input_file.readlines()
        for line in lines[0:3]:
            if line.count("(") > 2: 
                line = line.strip("\n")
                line = line.split(" ")
                positions = []
                for l in line:
                    positions.append(ast.literal_eval(l))
                    
                ones = myinitarray(positions,size) 
                
            if line.count("(") == 2:
                line = line.strip("\n")
                line = line.split(" ")
                positions = []
                for l in line:
                    positions.append(ast.literal_eval(l))
                origin = positions[0]
                destination = positions[1]
                move_tube(ones,origin,destination)

            if line.count("(") == 1:
                line = line.strip("\n")
                line = line.split(" ")
                positions = []
                for l in line:
                    positions.append(ast.literal_eval(l))
                positions = positions[0]
                deletion(ones,positions)
                
    return 

        

            

        
    

