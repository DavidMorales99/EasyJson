import os
import json
import copy


class easyjson():
    
    
    def __init__(self, file , memory): #memory is dictionary you put in to access the memory during runtime without keeping the file open
        self.file = file
        self.memory = memory
        self.check()
        
    def check(self): #checks if the specified file exist and if it doesn't or is empty writes a structure into it and if memory is a dict
        if not os.path.isfile(self.file):
            self.write()
        elif os.path.getsize(self.file) == 0:
            self.write()
        else:
            self.read()
        
    def write(self): #writes to the json file
        with open(self.file, "w") as f_stream:
            json.dump(self.memory, f_stream)
    
    def read(self): #takes a copy of the json file into the memory so you don't have to keep reading the json file
        with open(self.file, "r") as  i_stream:
            temp = json.load(i_stream)
            memory = copy.deepcopy(temp)
            
            
    def new_entry(self, directory, key, value): # set directory to None if you don't want it to be like key : {key : value } in the json file
        if not directory:
            self.memory.update({key : value})
            self.write()
        else:
            self.memory[directory].update({key : value})
            print(self.memory)
            self.write()
