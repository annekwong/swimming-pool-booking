from zipfile import ZipFile
from glob import glob
from datetime import datetime
import os

def Timestamp():
    return datetime.now().strftime("%d-%m-%y_%H-%M-%S")

def PackTemp():
    to_zip = glob(".\\temp\\*")
    to_zip.append(glob("log_*.txt")[0])
    
    # daystamp = datetime.now().strftime("%d-%m-%y")
    # filename = "session_{:s}.zip".format(daystamp)
    filename = "session_{:s}.zip".format(Timestamp())
    
    zf = ZipFile(filename, "w")
    for tz in to_zip:
        zf.write(tz)
    zf.close()
    print("> wrote {:s}".format(filename))
    
    # delete everything in temp
    for t in to_zip:
        os.remove(t)

if __name__ == "__main__":
    PackTemp()