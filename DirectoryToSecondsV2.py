#! /usr/bin/env python3
#Tumo Masire 05 Feb 2018

def get_length_easy(my_file):
    #ToDo: extend to support more file types, e.g .mov
    tag = TinyTag.get(my_file)
    return tag.duration
    
def duration(in_user, j):
    loc_answer_secs = 0
    for root, directories, filenames in os.walk(in_user):
        [j] = root
        for filename in filenames:
            full_path = os.path.join(root,filename)
            if full_path.endswith(('.mp4')):
                loc_answer_secs += get_length_easy(full_path)
            elif full_path.endswith(('.mov', '.mkv')):
                loc_answer_secs += get_length_harder(full_path)
    return loc_answer_secs
                
def to_string(s):
    string = ("{}:{}:{}".format(int(s//3600), int(s%3600//60), int(s%60)))
    return string

def get_length_harder(my_file):
    answer = 0
    from hachoir.parser import createParser
    from hachoir.metadata import extractMetadata
    from sys import argv, stderr, exit

    filename = my_file
    parser = createParser(filename)
    try:
        with parser:
             metadata = extractMetadata(parser)
    except Exception as err:
        print("Metadata extraction error: %s" % err)
        metadata = None    
    if not metadata:
        print("Unable to extract metadata")
        exit(1)
    try:
        for line in metadata.exportPlaintext():
            if "Duration:" in line:
                answer = string_parser(line)
    except Exception:
        pass
    return answer

def string_parser(line_in):
    line_mid = line_mid = line_in[12:]
    answer = 0
    if line_in.endswith(" ms"):
        if "sec" in line_in and (len(line_in[line_in.index('c'):])) < 8:
            line_mid = line_mid[0:-6]
        else:
            line_mid = line_mid[0:-7]
    if "hour" not in line_mid:
        line_mid = ("0 hour " + line_mid)
    if "sec" not in line_mid:
        line_mid = (line_mid + " 0 sec")
    if 'min' not in line_mid:
        hour_index = (line_mid.index('r') + 1)
        temp_mid = line_mid[:hour_index] + ' 0 min' + line_mid[hour_index:]
        line_mid = temp_mid
    try: 
        line_mid.index('c')
    except Exception:
        line_mid += 'c'
    x = time.strptime('{}'.format(line_mid) ,'%H hour %M min %S sec')
    answer = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    return answer     
                        
if __name__ == "__main__":
    import sys
    import os
    import datetime
    import time
    from tinytag import TinyTag
    
    answer_secs = 0
    user_directs = arguments = sys.argv[1:]
    num_folders = len(user_directs)
    clear = lambda: os.system('cls')
    clear()
    print("Time Format - hh:mm:ss")
    
    for i in range(num_folders):
        directs = user_directs[i]
        seconds = duration(directs,j = i)
        print("Folder: {} \n- {}".format(user_directs[i], to_string(seconds)))
        answer_secs += seconds
        
    ANSWER = to_string(answer_secs)
    #clear()
    print("Total: {}".format(ANSWER))