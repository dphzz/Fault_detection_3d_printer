import os, time



def file_added_function():
    print("This is the function run when new file is added")







if __name__ == "__main__":
    path_to_watch = "./test_folder"
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    while 1:
        #   time.sleep (10)
        dir_index = sorted(os.listdir(path_to_watch), key=lambda f: os.path.getmtime(os.path.join(path_to_watch, f)))
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        recent1 = dir_index[len(dir_index) - 1]
        recent2 = dir_index[len(dir_index) - 2]
        if added: 
            print("Added: ", ", ".join (added))
            print("Path to file: " + (path_to_watch + '/' + added[0]))
        if removed: 
            print("Removed: ", ", ".join (removed))
        before = after