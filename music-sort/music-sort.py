# Music Library Organising: 
"""
Music Library Organizer:
- script that organizes your music library by moving multiple files (songs) 
  into appropriate folder, renaming that folder to the album's name and 
  moving the newly created album folder into the appropriate artist
"""

import shutil 
import os

class Project:
    def __init__(self):
        
        
        self.sourceFolder = "sourceFolder" #path to source folder
        self.projectMedium = "projectMedium" #path to the medium folder
    
    def checkFileFunction(self, file):
            if file.startswith("music-for"):
                    
                join_path = os.path.join(self.sourceFolder, file)
                move_path = os.path.join(self.projectMedium, file)
            
                shutil.copy(join_path, move_path)
            
                emptyPath = os.remove(join_path)
                    
                return f"{file} respects the naming convention"
            else:
                os.remove(os.path.join(self.sourceFolder, file))
                return f"{file} does not respect naming conention and will be removed."

    
    def get_List(self):
        
        move_files = os.listdir(self.sourceFolder)
        
        for file in move_files:
            result = self.checkFileFunction(file)
            print(result)
        
    

project_test = Project()
project_test.get_List()


        #for file in move_files:
            
        #    checkFunction()
            
    #def iterate_File(self, get_List):
        
        #for files in self.projectMedium:
        #    return 1

