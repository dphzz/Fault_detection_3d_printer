import Segmentation_py.Doan1 as Doan1  #Chuong trinh xu li anh
import os
from octorest import OctoRest


def make_client(url, apikey):
     """Creates and returns an instance of the OctoRest client.

     Args:
         url - the url to the OctoPrint server
         apikey - the apikey from the OctoPrint server found in settings
     """
     try:
         client = OctoRest(url=url, apikey=apikey)
         return client
     except ConnectionError as ex:
         # Handle exception as you wish
         print(ex)


if __name__ == "__main__":
    #this section is for the octoprintAPI------------------------------
    api_key = '8F42025DDA1C4CBE9C27398BEE3162A7'
    url = 'http://192.168.1.7' 
    prusa_printer = make_client(url, api_key)
    
    #OctoprintAPI section end------------------------------------------

    #This section is for file control-----------------------------
    path_to_watch = "./test_folder"
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    #File control section end-------------------------------------
    while 1:
        #   time.sleep (10)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: 
            #print("Added: ", ", ".join (added))
            #print("Path to file: " + (path_to_watch + '/' + added[0]))
            #Get the array of the directory
            dir_index = sorted(os.listdir(path_to_watch), key=lambda f: os.path.getmtime(os.path.join(path_to_watch, f)))
            recent1 = path_to_watch + '/' + dir_index[len(dir_index) - 1]
            recent2 = path_to_watch + '/' + dir_index[len(dir_index) - 2]
            
            print(recent1 + ' ' + recent2)
            
            s1, s2, center1, center2, white1, white2 = Doan1.Img_processing(recent1, recent2)
            center_distance, ratio, hieu = Doan1.Caculate(s1, s2, center1, center2, white1, white2)
            print_status = Doan1.Compare(center_distance, ratio, hieu)
            
            #Determine whether to stop the print or not.
            if print_status != 0:
                #prusa_printer.pause()
                print("Error has occured, pause print!")
                break
            else:
                print("Within normal bound, continue")


        if removed: 
            print("Removed: ", ", ".join (removed))
        before = after