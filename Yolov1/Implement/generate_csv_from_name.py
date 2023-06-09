import pandas as pd
import os
import csv

PATH_TO_WATCH_DATA = r"G:\Shared drives\Ngo_Duc_Phu\Do_an_1\Dataset\Data"
PATH_TO_CSV = r"G:\Shared drives\Ngo_Duc_Phu\Do_an_1\Python_code\Yolov1\Implement\dataset.csv"
#Get the list of files in the folder
file_ls = os.listdir(PATH_TO_WATCH_DATA)
# print(file_ls)
formatted_data = []
# i = 0

#Grag the name of the .jpg file and add .txt to the name of the file
for name in file_ls:
    tmp_formatted_data = [1,2]
    tmp_formatted_data[0] = name
    txt_name = os.path.splitext(name)[0] + '.' + 'txt'
    tmp_formatted_data[1] = txt_name
    # i = i + 1
    formatted_data.append(tmp_formatted_data)


#Get all the file name and put it into a csv file. 
with open(PATH_TO_CSV, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["img", "label"])
    for row in formatted_data:
        writer.writerow(row)

print("New csv file created sucessfully")


