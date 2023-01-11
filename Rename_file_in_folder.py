from os import walk
import os

files =[]
dir_path = "C:/Users/Modern/Desktop/Thesis big files/12-12-22 Spheroids FH/Dish 0.3/Segmentation"
# dir_path = "C:/Users/Modern/Desktop/Thesis big files/12-12-22 Spheroids FH/Dish 0.3/"

i = 0

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        old_name = os.path.join(dir_path, path)
        new_name = dir_path + "/" +str(f'{i:03}') + '_Probabilities' + '.png'
        print(old_name)
        print(new_name)
        os.rename(old_name,new_name)
    i = i+1
        

