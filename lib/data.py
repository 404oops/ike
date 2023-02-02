print("Initializing verb 'dataproc'")
import os
import string
import random

def checkvideo(path):
    if os.path.isfile(path):
        # maybe check real mimetype/format in contents too
        if path.split('.')[-1] in ["mp4", "webm", "ogg", "avi", "wmv", "mov", "flv", "mkv"]:
            return path
        else:
            return False
    else:
        return Exception(FileNotFoundError)

def reencode(path, checkvideo=False):
    if checkvideo:
        return path
    else:
        os.system("ffmpeg -i" + path + " " + os.path.splitext(os.path.basename(path))[0] + ".webm")
        return os.path.splitext(os.path.basename(path))[0] + ".webm" # substitute path for this

def uuidgen(): return "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(10))