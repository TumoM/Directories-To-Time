#! /usr/bin/env python3
#Tumo Masire 05 Feb 2018

def getLength(my_file):
    #ToDo: extend to support more file types, e.g .mov
    tag = TinyTag.get(my_file)
    return tag.duration
    
def duration(in_user):
    loc_answer_secs = 0
    for root, directories, filenames in os.walk(in_user):
        for filename in filenames:
            full_path = os.path.join(root,filename)
            if filename.endswith((".mp4","mov")):
                loc_answer_secs += getLength(full_path)
    return loc_answer_secs
                
def to_string(s):
    string = ("{}:{}:{}".format(int(s//3600), int(s%3600//60), int(s%60)))
    return string
            
if __name__ == "__main__":
    import sys
    import os
    from tinytag import TinyTag
    
    answer_secs = 0
    user_directs = arguments = sys.argv[1:]
    clear = lambda: os.system('cls')
    clear()
    print("Time Format - hh:mm:ss")
    
    for i in range(len(user_directs)):
        direcs = user_directs[i]
        seconds = duration(direcs)
        print("Folder {} - {}".format(i+1, to_string(seconds)))
        answer_secs += seconds
        
    ANSWER = to_string(answer_secs)
    print("Total: {}".format(ANSWER))