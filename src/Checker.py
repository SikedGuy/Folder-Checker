import os
import shutil
from enum import Enum
from pathlib import Path

class ProblemType(Enum):
    NoProblem = 0,
    SubFolders = 1,
    EmptyFolder = 2,

class Checker:
    def __init__(self):
        pass

    def SearchDirectory(self, path: str)-> list[str]:
        folders: list[str] = []

        for item in os.listdir(path):
            i = 0

            if (not os.path.isdir(os.path.join(path, item))):
                continue

            for item2 in os.scandir(os.path.join(path, item)):
                i += 1

            if (i <= 1):
                folders.append(item)

        return folders

    def StartSearch(self, username: str) -> tuple[str, list[str]]:
        directory = f"C:\\Users\\{username}\\AppData\\LocalLow\\Stress Level Zero\\BONELAB\\Mods"
        return (directory, self.SearchDirectory(directory))

    def StartSearchNoGUI(self):
        username = input("<enter your username>")

        (directory, folders) = self.StartSearch(username)

        if (folders.__len__() <= 0):
            print("\nEverything looks good :)")
        else:
            print(f"{folders.__len__()} possible bad folders found in [{directory}]")
            print("|")
            for folder in folders:
                problemType: ProblemType = Checker.GetProblemType(os.path.join(directory, folder))

                print(f"|-> {folder} --> {problemType.name}")

        input("\nenter anything to close")

    def ValidUsername(username: str) -> bool:
        return os.path.exists(f"C:\\Users\\{username}\\AppData\\LocalLow\\Stress Level Zero\\BONELAB\\Mods")
    
    # assumes path actualy exists
    def GetProblemType(path: str) -> ProblemType:
        i = 0
        for item2 in os.scandir(path):
            i += 1

        if (i == 1):
            return ProblemType.SubFolders
        elif (i <= 0):
            return ProblemType.EmptyFolder
        else:
            return ProblemType.NoProblem
    
    # assumes path actualy exists
    def Fix(path: str):
        problemType = Checker.GetProblemType(path)
        subfolderPaths = os.listdir(path)

        p = Path(path)

        match problemType:
            case (ProblemType.SubFolders):
                # move folder up one level
                for folder in subfolderPaths:
                    #print(os.path.join(path, folder))
                    try:
                        shutil.move(os.path.join(path, folder), p.parent)
                        print(f"{os.path.join(path, folder)} moved to {p.parent} sucussfully")
                    except OSError as error:
                        print(error)
                        print("File path can not be moved")
            case (ProblemType.EmptyFolder):
                # delete folder
                try:
                    shutil.rmtree(path)
                    print(f"{path} removed successfully")
                except OSError as error:
                    print(error)
                    print("File path can not be removed")
