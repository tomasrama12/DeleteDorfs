import os;
from dotenv import load_dotenv;
load_dotenv()
DIR_TO_CHECK = os.getenv("DIR_PATH_WITH_DORFS")

def checkIfPathExist(path):
    if os.path.exists(path):
        return True
    else:
        print("Path does not exist")
        return False

def moveToDir(path):
    if checkIfPathExist(path):
        os.chdir(path)
        print("Selected path: " + os.getcwd())
        return True
    else:
        return False
    
def countDorfsInDir(path):
    if moveToDir(path):
        count = 0
        files = []
        for file in os.listdir():
            if file.startswith('dorf'):
                count += 1
                files.append(file)
        print(str(count) + " files found, " + str(files))
        return count
    
def deleteDorfsInDir(path):
    if countDorfsInDir(path) > 0:
        userInput = input("Are you sure you want to delete all dorfs in this directory? (y/n)")
        if userInput == 'y':
            for file in os.listdir():
                if file.startswith('dorf'):
                    os.remove(file)
                    print(file + " removed")
            return True
        else:
            print("No dorfs removed")
            return False
    else:
        print("No dorfs found")
        return False
    
deleteDorfsInDir(DIR_TO_CHECK)
    


