#! /usr/bin/env python3
#Tumo Masire 05 Feb 2018

def hello(a,b,c):
    print ("hello and that's your sum:")
    sum=int(a)+int(b)+int(c)
    print (sum)
    
def getLength(file):
    tag = TinyTag.get(file)
    return tag.duration
    

def duration(in_user):
    answer_secs = 0
    for root, directories, filenames in os.walk(in_user):
        for filename in filenames:
            full_path = os.path.join(root,filename)
            if filename.endswith(".mp4"):
                #print("{}".format(full_path))
                answer_secs += getLength(full_path)
    return answer_secs
                
def to_string(s):
    string = ("{}:{}:{}".format(int(s//3600), int(s%3600//60), int(s%60)))
    return string
            

if __name__ == "__main__":
    import sys
    import os
    import datetime
    from tinytag import TinyTag
    
    answer_secs = 0
    user_directs = arguments = sys.argv[1:]
    
    for i in range(len(user_directs)):
        print(i)
        direcs = user_directs[i]
        answer_secs += (duration(direcs))
    ANSWER = to_string(answer_secs)
    print(ANSWER)