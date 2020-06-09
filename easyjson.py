import os
import json
import copy



class Utilize_file():
    
    Skeleton = {}
    Skeleton["catalog"] = {}    
    
    def __init__(self,File):
        self.File = File
        self.check()
    #################################
    
    def check(self): #checks if the file in question exist and if it does but is empty writes a empty dictionary to it to avoid errors
        if not os.path.isfile(self.File): #check if file exist if it doesn't make a new one with empty dictionary
            self.write_file() 
            pass
        elif not os.path.getsize(self.File): #check if it's empty if it is then write empty dictionary to it
            self.write_file()
            pass
        else:
            self.load_file()
    
    ##################################  
    
    def load_file(self):
        with open(self.File, "r") as i_stream:
            temp = json.load(i_stream)
            self.Skeleton = copy.deepcopy(temp) #deepcopy actually copies the object where as copy just makes a reference to whatever
            print(self.Skeleton)
            
    ##################################
    
    def write_file(self):
        with open(self.File, "w") as f_stream:
            json.dump(self.Skeleton, f_stream)
            
    ###################################        
            
    def new_entry(self):
        clear()
        key = input("Please enter the key\n")
        val = input("Please enter the value\n")
        print("enter ^done after submitting an entry to exit")
        self.Skeleton["catalog"].update({key : val})
        self.write_file()
        
    ####################################
    