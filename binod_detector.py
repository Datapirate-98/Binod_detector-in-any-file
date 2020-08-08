import os
import sys

def isbinod(file):
    with open(file, "r") as f:
        file_content = f.read()
    if "binod" in file_content.lower():
        return True
    else:
        return False
        
if __name__ == "__main__":
    dir = os.listdir()
    for i in dir:
        if i.endswith("txt") or i.endswith("html"):
            print(f"Detecting BINOD in {i}")
            flag = isbinod(i)
            if flag:
                print(f"\n\nBHAI BACHKE BINOD HAI ISMEH---------->{i}<-----------\n\n")
            else:
                pass
